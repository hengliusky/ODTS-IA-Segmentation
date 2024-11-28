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

Pytorch 2.0.1, Python 3.9

```
$ conda create --name odts python=3.9
$ conda activate odts
```

### Dataset
This study utilizes two IA medical image datasets from Wannan Medical College (WMC-AHUT) and Ma'anshan People's Hospital (MPH-AHUT).

The datasets are not yet publicly available but are planned to be released soon. For access requests, please contact hengliusky@aliyun.com.


### Testing

```
python3 predict.py
-i imagesTs
-o nnUNet_pred
-d 606 -c 3d_fullres -f all
```



### Citing

If you use our work in your research, please cite us using the following entry ~ Thank you.


# Overall network workflow

## Training
### Focus stage
1. Downsample all samples -utils.focus_trainset_generator.py
   1. The downsampled size is [256, 256, 160]
2. Train the network.

### Refinement stage
1. Generate training data from the original data automatically - utils.refinement_generator.py
   1. The generated size is [128, 128, 128]
2. Train the network.

## Testing
### Focus stage
1. Downsample the test samples -utils.focus_trainer_generator.py
2. Obtain the focus cube based on the coarse segmentation result, with a size of [128, 128, 128]

### Refinement stage
1. Input the focus cube into the refinement network.
2. Obtain the final results.


