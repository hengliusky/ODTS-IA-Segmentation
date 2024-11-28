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
This study collects two IA medical image datasets - WMC-AHUT from Wannan Medical College and MPH-AHUT from Ma'anshan People's Hospital.

These datasets are not yet publicly available but are planned to be released soon. If you need access, please email hengliu@ahut.edu.cn to apply.

### Testing

```
python3 predict.py
-i imagesTs
-o nnUNet_pred
-d 606 -c 3d_fullres -f all
```



### Citing

If you use our work in your research, please cite us using the following entry ~ Thank you.


# Overall workflow

## Training
### Focus stage
1. Use `utils.focus_trainset_generator.py` to downsample the training samples with a target size of `[256, 256, 160]` after downsampling.
2. Train the focuing network.

### Refinement stage
1.Use `utils.refinement_generator.py` to generate training data from raw input data.
2.Train the refinement network.

## Testing
### Focus stage
1. Use `utils.focus_trainset_generator.py` to downsample the test samples with a target size of `[256, 256, 160]` after downsampling.
2. Obtain the focus cube based on the coarse segmentation resultof the focus stage, with a size of [128, 128, 128]

### Refinement stage
1. Input the focus cube into the refinement network.
2. Obtain the final results.


