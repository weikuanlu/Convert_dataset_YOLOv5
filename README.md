- 首先将自己的 `VOC` 格式的数据集，放在 `VOC2007` 路径下

    图片放在 `JPEGImages`

    标签放在 `Annotations`

- 运行 `01.划分数据集.py`代码，将数据集分割成 训练集、验证集和测试集（自行设置比例）

    生成的文件在 `VOC2007/ImageSets/Main` 中，

    分别是 `test.txt`、`train.txt`、`val.txt`

- 运行 `02.数据集分包.py` 代码，将 `VOC2007/JPEGImages` 路径下的图片，按照上面分好的数据集，分别保存到 `images/test`、`images/train`、`images/val`

- 运行 `03.voc_label.py` 代码（需要手动修改代码里面的目标类别），将 `VOC2007/Annotations` 路径下的标签，生成一个文件夹 `VOC2007/labels`，里面保存的是每张图片的标签坐标（以 `txt`格式保存）

- 运行 `04.标签分包.py` 代码，将 `VOC2007/labels` 路径下的标签，按照上面分好的数据集，分别保存到 `labels/test`、`labels/train`、`labels/val`

- 最后，`images` 和 `labels` 就是我们需要用的数据集

