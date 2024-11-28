# ODTS-IA-Segmentation

**This repository is for the paper, “Orthogonal Dual-Path Transformers for Accurate
Segmentation of Intracranial Aneurysm: A
Coarse-to-Fine Framework Without Patch
Division”**



### Result

Result1:

![WMC](https://github.com/user-attachments/assets/ba4bb2e7-2e1e-4872-a6e2-dfea1b10e1d2)


Result2:

![MPH](https://github.com/user-attachments/assets/7989eea4-4319-4dbc-883a-ca05bbe4da11)




### Environment

Pytorch 1.9.0, Python 3.9

```
$ conda create --name odts python=3.9
$ conda activate odts
```



### Testing

```
python3 predict.py
-i imagesTs
-o nnUNet_pred
-d 606 -c 3d_fullres -f all
```



### Citing

If you use our work in your research, please cite us using the following entry ~ Thank you.








# 网络整体工作流程

## 网络训练
### 聚焦阶段
1. 全部将样本进行下采样——utils.focus_trainset_generator.py
   1. 下采样的尺寸为[256, 256, 160]
2. 对网络进行训练

### 精炼阶段
1. 训练数据由原始数据自动生成-utils.refinement_generator.py
   1. 生成的尺寸为[128, 128, 128]
2. 对网络进行训练

## 测试阶段
### 聚焦阶段
1. 对测试样本进行下采样-utils.focus_trainer_generator.py
2. 根据粗分割结果获得聚焦框，聚焦框的尺寸为[128, 128, 128]

### 精炼阶段
1. 将聚焦框送入精炼网络
2. 获得最终结果


