Bert Orientation analysis
==============
使用Bert模型训练的情感分析模型

配置
--------
下载[预训练模型](https://pan.baidu.com/s/1okGx_qRvlimNuv_-TSRz0w)（提取码n6mb），解压后将`chinese_wwm_ext_L-12_H-768_A-12`目录放置于项目根目录

训练参数说明
------------
内存（显存）的使用取决于三个因素：句子长度、batch size、模型复杂度。如果内存不够大，将句子的maxlen和batch size都调小一点试试。
