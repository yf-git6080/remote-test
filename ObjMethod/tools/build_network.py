import torch.nn.functional as F
import torchvision
from mmengine.model import BaseModel
import torch.nn as nn
from mmrotate.models.builder import ROTATED_HEADS
import torch
from torch import nn
import numpy as np
@ROTATED_HEADS.register_module()
class EagleNet(BaseModel):
    def __init__(self):
        super().__init__()
        self.resnet = torchvision.models.resnet50()

    def forward(self, imgs, labels, mode):
        x = self.resnet(imgs)
        if mode == 'loss':
            return {'loss': F.cross_entropy(x, labels)}
        elif mode == 'predict':
            return x, labels


    # 模型基类 `train_step` 等效代码
    def train_step(self, data, optim_wrapper):
        data = self.data_preprocessor(data)
        loss_dict = self(*data, mode='loss')
        loss_dict['loss1'] = loss_dict['loss1'].sum()
        loss_dict['loss2'] = loss_dict['loss2'].sum()
        loss = (loss_dict['loss1'] + loss_dict['loss2']).sum()
        #调用优化器封装更新模型参数
        optim_wrapper.update_params(loss)
        return loss_dict

    def val_step(self, data, optim_wrapper):
        data = self.data_preprocessor(data)
        outputs = self(*data, mode='predict')
        return outputs

    def test_step(self, data, optim_wrapper):
        data = self.data_preprocessor(data)
        outputs = self(*data, mode='predict')
        return outputs
class MixUpDataPreprocessor(nn.Module):
    def __init__(self, num_class, alpha):
        self.alpha = alpha

    def forward(self, data, training=True):
        data = tuple(_data.cuda() for _data in data)
        # 验证阶段无需进行 MixUp 数据增强
        if not training:
            return data

        img, label = data
        label = F.one_hot(label)  # label 转 onehot 编码
        batch_size = len(label)
        index = torch.randperm(batch_size)  # 计算用于叠加的图片数
        lam = np.random.beta(self.alpha, self.alpha)  # 融合因子

        # 原图和标签的 MixUp.
        img = lam * img + (1 - lam) * img[index, :]
        label = lam * batch_scores + (1 - lam) * batch_scores[index, :]
        # 由于此时返回的是 onehot 编码的 label，model 的 forward 也需要做相应调整
        return tuple(img, label)