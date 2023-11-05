import torch
import torch.nn as nn
import torch.nn.functional as F
import time
import torch.optim as optim

class GAT(nn.Module):
    def __init__(self, in_features, out_features, num_heads, dropout, alpha):
        super(GAT, self).__init__()

        # Multi-head attention mechanism
        self.heads = nn.ModuleList([
            GraphAttentionLayer(in_features, out_features, dropout, alpha) for _ in range(num_heads)
        ])

    def forward(self, x, adj):
        head_out = [head(x, adj) for head in self.heads]
        # Stack the outputs of multiple heads
        out = torch.stack(head_out, dim=1)
        # Sum the outputs of different heads
        out = out.sum(dim=1)
        return F.log_softmax(out, dim=1)

class GraphAttentionLayer(nn.Module):
    def __init__(self, in_features, out_features, dropout, alpha):
        super(GraphAttentionLayer, self).__init__()
        self.dropout = dropout
        self.in_features = in_features
        self.out_features = out_features
        self.alpha = alpha

        self.W = nn.Parameter(torch.empty(size=(32, in_features, out_features)))
        nn.init.xavier_uniform_(self.W.data, gain=1.414)

        self.a = nn.Parameter(torch.empty(size=(32, 2 * out_features, 1)))
        nn.init.xavier_uniform_(self.a.data, gain=1.414)

        self.leakyrelu = nn.LeakyReLU(self.alpha)
        self.fc = nn.Linear(14*out_features, out_features)

    def forward(self, h, adj):
        Wh = torch.bmm(h, self.W)
        e = self._prepare_attentional_mechanism_input(Wh, h, adj)

        zero_vec = -9e15 * torch.ones_like(e)
        attention = torch.where(adj > 0, e, zero_vec)
        attention = F.softmax(attention, dim=1)
        attention = F.dropout(attention, self.dropout, training=self.training)
        h_prime = torch.bmm(attention, Wh).view(32, -1)
        h_prime = self.fc(h_prime)
        return h_prime

    def _prepare_attentional_mechanism_input(self, Wh, h, adj):
        Wh1 = torch.bmm(Wh, self.a[:, :self.out_features, :])
        Wh2 = torch.bmm(Wh, self.a[:, self.out_features:, :])
        e = Wh1 + Wh2.transpose(1,2)
        return self.leakyrelu(e)


def accuracy(output, labels):
    preds = output.max(1)[1].type_as(labels)
    correct = preds.eq(labels).double()
    correct = correct.sum()
    return correct / len(labels)


# 定义模型
model = GAT(in_features=2048, out_features=702, num_heads=2, dropout=0.5, alpha=0.2).cuda()

# 输入特征和邻接矩阵
features = torch.randn((32, 14, 2048)).cuda()
adj = torch.randn((32, 14, 14)).cuda()
labels = torch.randint(low=0, high=702, size=(32,), dtype=torch.long).cuda()
# 前向传播
optimizer = optim.Adam(model.parameters(),
                       lr=0.01,
                       weight_decay=0.5)
criterion = nn.CrossEntropyLoss(reduce=True).cuda()

acc = 0
all_loss = 0
for epoch in range(100000):
    t = time.time()
    model.train()
    optimizer.zero_grad()
    output = model(features, adj)
    loss = F.cross_entropy(output, labels)
    all_loss += loss
    acc += accuracy(output, labels)
    loss.backward()
    optimizer.step()
    if epoch %100 == 0:
        acc/=100
        all_loss/=100
        print('Epoch: {:04d}'.format(epoch + 1),
              'loss_train: {:.4f}'.format(loss.data.item()),
              'acc_train: {:.4f}'.format(acc.data.item()),
              'time: {:.4f}s'.format(time.time() - t))
        acc=0
        all_loss=0