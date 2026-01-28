# yolov12的复现工作
**说明：**
本项目的复现工作主要针对轻量化的nano模型，开源的权重也是nano规模的，可用于简单的日常任务。
yolov12n是在COCO数据集上训练，yolov12n-obb是在DOTAv1.0数据集上训练的。

**环境配置**
install the ultralytics package, including all requirements, in a Python>=3.8 environment with PyTorch>=1.8.
```
cd yolov12-Reproduce
pip install e . 
```


## 在COCO数据集上训练yolov12-HBB模型
将COCO数据集解压后按照如下格式放入`datasets/coco`文件夹中
```
-datasets
    -coco
        -annotations
        -images
        -labels
        -train2017.txt
        -val2017.txt
        -test-dev2017.txt
```
配置好数据及后直接使用`train12.py`脚本进行训练，训练时设置参数`'val': True`，训练时会自动在终端输出mAP50(val)结果。可与官方结果进行对齐。
```
cd yolov12-Reproduce
python train/train12.py
```
训练后的结果会保存在`yolov12-Reproduce/YOLO12-HBB/nano`文件夹中

## 在DOTA数据集上训练yolov12-OBB模型
### 1. 数据集处理
#### DOTA原始标签格式
在官网上(https://captain-whu.github.io/DOTA/dataset.html)下载数据集后解压，可以看到官方的数据集标注格式为
```
409 1171 410 1191 343 1201 342 1182 small-vehicle 0
434 1483 505 1479 507 1502 436 1504 large-vehicle 0
697 1281 718 1278 743 1405 721 1410 large-vehicle 0
556 1314 580 1310 603 1437 578 1442 large-vehicle 0
521 1296 544 1291 549 1361 528 1364 small-vehicle 0
```
是`x1 , y1 , x2 , y2, x3 , y3 , x4 , y4 , classes ,   difficulty`的四点绝对像素坐标格式

#### preprocess
首先将数据集整理成以下目录形式并放入`datasets`文件夹中，方便后续处理
```
-datasets
    -DOTAv1.0
        -images
            -train
            -val
            -test
        -labels
            -train
            -val
            -test

// 其中labels/test为空文件夹
```
由于DOTA数据集中图片尺寸很大，因此要对数据集中的图片进行切割，同时切割时使用不同`size`来对切割尺寸进行缩放，以便训练时同时能兼顾到大尺寸目标和小尺寸目标。

在进行切割之前需要将原DOTA标签数据格式进行转化，转化成可以直接输入进行`split`的形式，具体操作为将原DOTA标签中的`class_name`转换成`class_id`并放在`labels`的第一列。
```
python data-pre/labels_split_pre.py
```
执行上述命令后，会在`datasets`文件夹下生成标签转换后的数据集`DOTAv1.0-pre`
```
-datasets
    -DOTAv1.0
    -DOTAv1.0-pre
```

之后使用脚本`DOTA_split.py`对数据集进行分割：
```
python data-pre/DOTA_split.py
```
执行上述命令后会在`datasets`文件夹下生成分割后的数据集`DOTAv1.0-split`

#### 处理结果
切割完之后的label格式为：
```
10 0.623047 0.482422 0.638672 0.488281 0.621094 0.519531 0.605469 0.513672
10 0.671875 0.498047 0.685547 0.505859 0.673828 0.535156 0.660156 0.529297
10 0.207031 0.986328 0.210938 0.970703 0.251953 0.976562 0.25 0.990234
10 0.548828 0.726562 0.533203 0.716797 0.548828 0.693359 0.560547 0.699219
```
`class_id`+归一化四点坐标，可以直接进行训练

### 2. 训练和推理
#### 训练
使用ultralytics中封装好函数`model.train`进行训练，具体参数配置在训练脚本`train12n-obb.py`中。
```
# 训练命令
python train/train12n-obb.py
```
训练后的结果会保存在`yolov12-Reproduce/YOLO12-OBB/nano`文件夹中

#### 推理
使用`model.val`进行推理，设置`save_json = True`。如此在进行`model.val`推理调用函数`OBBValidator`时，如果检测到数据集为DOTA会自动执行标签合并操作，直接输出名为`predictions_merged_txt`的文件夹。该文件夹以及val的结果保存在`runs/obb/val/`目录中。
```
# 推理命令，用于在test集上预测并将最终结果提交官网
python train/val-obb.py
```













