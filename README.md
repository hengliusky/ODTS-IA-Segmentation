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


