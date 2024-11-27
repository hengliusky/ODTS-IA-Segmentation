# ODTS-IA-Segmentation


**This repository is for the paper, “Orthogonal Dual-Path Transformers for Accurate
Segmentation of Intracranial Aneurysm: A
Coarse-to-Fine Framework Without Patch
Division”**

###Network
![network](https://github.com/user-attachments/assets/574a9dfc-7ffa-4f74-b538-4d51515e1639)


### Result

Result1:
![WMC](https://github.com/user-attachments/assets/510d2aaf-1f25-43d3-8770-139946d25663)


Result2:
![MPH](https://github.com/user-attachments/assets/473dedf2-1882-4379-89aa-bd9420609ebc)

### Environment

Pytorch 1.9.0, Python 3.9

```
$ conda create --name odts python=3.9

```

### Testing

```
python3 predict.py -i /XXX/XXX/imagesTs -o /XXX/XXX/nnUNet_pred/ -d 606 -c 3d_fullres -f all



### Citing

If you use our work in your research, please cite us using the following entry ~ Thank you .

```
