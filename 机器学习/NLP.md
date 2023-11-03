大纲：

![image-20231006163517658](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20231006163517658.png)

参考网站：

[第一章:文本预处理 - 文本预处理](http://121.199.45.168:8003/1/)

# 文本预处理

## jieba的使用

~~~python
import jieba
content=""
# 精确模式
jieba.cut(content,cut_all=False)
jieba.lcut(content,cut_all=False)
# 全模式
jieba.cut(content,cut_all=True)
jieba.lcut(content,cut_all=True)
# 搜索
jieba.cut_for_search(content)
jieba.lcut_for_search(content)
# 导入自己的包
jieba.load_userdict()
~~~



~~~python
# 命名实体
# hanlp中存在已有的训练模型，有中文也有英文
recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)

# 词性标注
tagger = hanlp.load(hanlp.pretrained.pos.CTB5_POS_RNN_FASTTEXT_ZH)

# 使用时，里面为list
recognizer(["President", "Obama", "is", "speaking", "at", "the", "White", "House"])
[('Obama', 'PER', 1, 2), ('White House', 'LOC', 6, 8)]
tagger(['我', '的', '希望', '是', '希望', '和平'])
~~~



~~~python
# one_hot编码
可以使用from sklearn.preprocessing import OneHotEncoder中的这个包来进行编码
也可以使用它给的示例来进行编码，我更倾向第一种，但是第一种的格式可能不一样

# word2vec
CBOW：根据前后的n个词来进行中间词的预测
skipgram：根据中间词对两边的n个词进行预测
注：有点像窗口滑动

# 词嵌入
将离散的词转化为连续的词
~~~



~~~python
# 文本数据可视化分析
# 1. 标签分布	sns.countplot("x",data=数据)
# 2. 长度分布	sns.displot(长度list) 
# 3. 长度散点分布		sns.stripplot(y="", x="", data=数据)
# 4. 不同词汇汇总		train_vocab = set(chain(*map(lambda x: jieba.lcut(x), train_data["sentence"])))
chain包的作用，将里面的数据进行拼接
# 5. 词云图	使用WordCloud包进行统计
~~~



~~~python
# n-gram特征，将词语连接起来，使它们具有相应的联系
    Bigram（Bi-gram）：
    Bigram 是指连续的两个词语组成的序列。
    例如，对于句子 "I love natural language processing"，其 bigram 特征包括："I love"，"love 		natural"，"natural language"，"language processing"。
    Trigram（Tri-gram）：
    Trigram 是指连续的三个词语组成的序列。
    例如，对于同样的句子 "I love natural language processing"，其 trigram 特征包括："I love 		natural"，"love natural language"，"natural language processing"。
# 文本长度规范
sequence.pad_sequences(x_train, cutlen)
# 将文本进行填充和删除，都是在前面进行增删
~~~



~~~python
# 回译数据增强
使用google的翻译器，将现在的文字转化为其它语言，再翻译回来
translations = translator.translate(ko_res, dest='zh-cn')
~~~

