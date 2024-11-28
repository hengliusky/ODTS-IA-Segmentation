import re
import shutil
import nibabel as nib
import os
import numpy as np

# ============================ 获取ID ========================================
# dir = r'/opt/data/private/Datasets/nnunet_base/nnUNet_raw/Dataset605_MAS2_refine_finetune/imagesTr'
# patient_list = os.listdir(dir)
# print(patient_list)
#
# name_list = []
#
# for name in patient_list:
#     ret = re.split('_0000', name)
#     name_list.append(ret[0])
#
# print(name_list)
# print(len(name_list))

# ============================ 在列表中去除低质量的 ===============================
# dataset_list = ['0000683270', '0000962629', '0000862853', '0000151253', '0000111371', '0000469491', '0000009426', '0000894607', '0000981387', '0000000692', '0000038985', '0000230028', '0000384595', '0000097259', '0000963377', '0000868666', '0000965795', '0000154597', '0000825658', '0000864918', '0000899179', '0000862266', '0000109572', '0000118857', '0001014213', '0000706877', '0000858081', '0000626470', '0000570636', '0000591801', '0000874742', '0000425994', '0000792474', '0000925566', '0000157009', '0000776724', '0001016478', '0000352025', '0000933988', '0000876881', '0000007212', '0001017295', '0001019586', '0001017612', '0000178011', '0000974965', '0000420105', '0000931699', '0000046981', '0000900932', '0000348024', '0000233748', '0000916594', '0000971138', '0000258124', '0000072306', '0000786529', '0000391043', '0000638451', '0000612982', '0000025745', '0000042693', '0000466994', '0000264877', '0000667324', '0000686835', '0000095216', '0000420571', '0000966323', '0000861405', '0000972912', '0000163718', '0000924122', '0000979454', '0000987587', '0000977646', '0000925737', '0000990926', '0000306571', '0000959870', '0000927108', '0000454967', '0000963538', '0000231737', '0000098621', '0000447651', '0000410329', '0000231397', '0000859304', '0000724089', '0000954259', '0000996543', '0000951772', '0001015136', '0000986040', '0000065253', '0000510480', '0000956102', '0000872440', '0000996658']
# print(len(dataset_list))
#
# dice_0 = ['0000009426', '0000025745', '0000038985', '0000046981', '0000095216', '0000097259', '0000109572', '0000151253', '0000157009', '0000230028', '0000352025', '0000384595', '0000454967', '0000469491', '0000570636', '0000786529', '0000792474', '0000862266', '0000868666', '0000894607', '0000927108', '0000933988', '0000959870', '0000962629', '0000963538', '0000965795', '0000972912', '0000974965', '0000977646', '0000981387']
# print(len(dice_0))
#
# dice_low = ['0000007212', '0000154597', '0000420105', '0000683270', '0000859304', '0000864918']
# print(len(dice_low))
#
# dataset_list_new = []
# for name in dataset_list:
#     if name in dice_0:
#         # print(1)
#         pass
#     elif name in dice_low:
#         print(name)
#         pass
#     else:
#         dataset_list_new.append(name)
#
# print(dataset_list_new)
# print(len(dataset_list_new))


# ============================= 筛选数据集 =================
# dir = r'/opt/data/private/Datasets/MAS/NII-100/label_with_chest'
# # dir = r'/opt/data/private/Datasets/WMC_mydiv/train/label'
# name_list = os.listdir(dir)
#
# n_small = 0
#
# small_name = []
#
# for name in name_list:
#     print(name)
#     path = os.path.join(dir, name)
#
#     label_data = nib.load(path).get_fdata()
#
#     print(np.sum(label_data))
#
#     if np.sum(label_data) < 150:
#         n_small += 1
#         small_name.append(name)
# print(n_small)
# print(small_name)


# ==============================读取训练集样本名称创建列表===================================
# dir = r'/opt/data/private/Datasets/nnunet_base/nnUNet_raw/Dataset701_WMC_lowres_coarse_finetune/imagesTr'
# patient_list = os.listdir(dir)
#
# train_list = []
#
# # val_keys = ['image_048', 'image_073', 'image_081', 'image_093', 'image_105', 'image_104', 'image_055', 'image_035', 'image_060', 'image_063', 'image_033', 'image_103', 'image_100', 'image_062', 'image_079', 'image_096', 'image_040', 'image_086', 'image_076', 'image_089', 'image_044', 'image_087', 'image_070', 'image_074', 'image_052', 'image_064', 'image_043', 'image_098', 'image_049', 'image_061', 'image_084', 'image_047', 'image_069', 'image_057', 'image_094', 'image_099', 'image_037', 'image_034', 'image_075', 'image_032', 'image_078', 'image_088', 'image_102', 'image_106', 'image_030', 'image_056', 'image_101', 'image_090', 'image_067', 'image_041', 'image_029', 'image_080', 'image_036', 'image_054', 'image_085', 'image_046', 'image_065', 'image_068', 'image_092', 'image_045', 'image_097', 'image_039', 'image_038', 'image_072', 'image_083', 'image_051', 'image_042', 'image_053', 'image_071', 'image_095', 'image_059', 'image_091', 'image_031', 'image_077', 'image_107', 'image_082', 'image_050', 'image_058', 'image_066', 'image_108']
# tr_keys = ['image_001', 'image_002', 'image_009', 'image_010', 'image_018', 'image_022', 'image_024', 'image_027', 'image_029', 'image_031', 'image_034', 'image_037', 'image_039', 'image_040', 'image_043', 'image_045', 'image_052', 'image_053', 'image_057', 'image_061', 'image_062', 'image_063', 'image_064', 'image_065', 'image_066', 'image_068', 'image_071', 'image_072', 'image_074', 'image_075', 'image_076', 'image_078']
#
# test_list = tr_keys
#
#
# for name in patient_list:
#     ret = re.split('_0000.nii.gz', name)
#     print(ret)
#
#     if ret[0] in test_list:
#         continue
#     else:
#     # print(ret[0])
#         train_list.append(ret[0])
#
# print(train_list)
# print(len(train_list))
#     # break


# ===============================MAS数据集中将100体素以下的分到训练集当中==============================
# # dir = r'/opt/data/private/Datasets/WMC_mydiv/test/label'
# dir = r'/opt/data/private/Datasets/nnunet_base/nnUNet_raw/Dataset602_MAS_lowres_coarse_finetune/labelsTr'
#
# train_list = []
# val_list = []
# patient_list = os.listdir(dir)
#
# print(len(patient_list))
#
# min_n_voxel = 10000
#
# for name in patient_list:
#     ret = re.split('\.', name)
#     print(ret)
#
#     # break
#     path = os.path.join(dir, name)
#     label_data = nib.load(path).get_fdata()
#
#     n_voxel = np.sum(label_data)
#
#     if n_voxel < 100:
#         print(name)
#         print(n_voxel)
#         train_list.append(ret[0])
#     else:
#         val_list.append(ret[0])
#
#     if n_voxel < min_n_voxel:
#         # print(name)
#         min_n_voxel = n_voxel
#     # print(np.sum(label_data))
#
# print(min_n_voxel)
#
# print(train_list)
# print(val_list)
# # print(name_list)

# =================================== 根据给定名称移动测试集 =================================
val_keys = ['0000178011', '0000666275', '0000931699', '0000562386', '0000648594', '0000348024', '0000540498', '0000233748', '0000258124', '0000072306', '0000092333', '0000638451', '0000612982', '0000042693', '0000040000', '0000466994', '0000825658', '0000264877', '0000686835', '0000100099', '0000420571', '0000602569', '0000966323', '0000736360', '0000861405', '0000719066', '0000163718', '0000979454', '0000987587', '0000609232', '0000744155', '0000421192', '0000336128', '0000626322', '0000925737', '0000990926', '0000715767', '0000509676', '0000306571', '0000108941', '0000354402', '0000724089', '0001015136', '0000065253', '0000150573', '0000996658', '0000245347','0000876881', '0000776724', '0001014213', '0000706877', '0000626470', '0000745235', '0000874742', '0000217989', '0000425994']
source_dir = r'/opt/data/private/Comparative_work/nnFormer-main/DATASET/nnFormer_raw/nnFormer_raw_data/Task502_MAS2/labelsTr'
# target_dir = r'/opt/data/private/Datasets/nnunet_base/nnUNet_raw/Dataset605_MAS2_refine_finetune/imagesTs'

patient_list = os.listdir(source_dir)

for name in patient_list:
    source_path = os.path.join(source_dir, name)
    # target_path = os.path.join(target_dir, name)

    ret = re.split('[_\.]', name) # 这是针对MAS数据集的
    # ret = re.split('_0000.nii.gz', name)   # 这是针对WMC数据集的
    print(ret)
    # if ret[0] in val_keys:
    #     print(ret)
    #     print(source_path)
    #     print(target_path)
    #
    #     # break
    #     shutil.copyfile(source_path, target_path)
    # else:
    #     continue

    # 去除训练文件夹中的测试集
    if ret[0] in val_keys:
        print(source_path)
        os.remove(source_path)


    # break


# ==========================================进行350体素的切割==============================
# dir = r'/opt/data/private/Datasets/MAS/NII-42'
# out_dir = r'/opt/data/private/Datasets/MAS/NII-42'
# # out_dir = r'/opt/data/private/DataSets/nnunet_base/nnUNet_raw/Dataset601_MAS'
#
# ct_dir = os.path.join(dir, 'ct_with_chest')
# label_dir = os.path.join(dir, 'label_with_chest')
#
# ct_out_dir = os.path.join(out_dir, 'ct')
# label_out_dir = os.path.join(out_dir, 'label')
#
# patient_list = os.listdir(ct_dir)
#
# print(patient_list)
#
# for patine_name in patient_list:
#     ct_path = os.path.join(ct_dir, patine_name)
#     label_path = os.path.join(label_dir, patine_name) + '.gz'
#
#     ct_data = nib.load(ct_path)
#     ct_data = ct_data.get_fdata()
#     label_data = nib.load(label_path).get_fdata()
#
#     print(patine_name)
#     print(ct_data.shape)
#     s_index = np.unique(np.where(label_data == 1)[2])
#     print(s_index)
#     print(ct_data.shape[2] - s_index[0])
#     print(np.sum(label_data))
#
#     print('--------------裁剪后-----------------')
#
#     crop_ct_data = ct_data[:, :, -350:]
#     crop_laebl_data = label_data[:, :, -350:]
#
#     print(crop_ct_data.shape)
#     print(crop_laebl_data.shape)
#     print(np.sum(crop_laebl_data))
#     if np.sum(crop_laebl_data) != np.sum(label_data):
#         print('WARNING!')
#         break
#
#     # continue
#
#     ret = re.split('\.', patine_name)
#
#     print(ret)
#
#     ct_out_path = os.path.join(ct_out_dir, ret[0]+'_0000.nii.gz')
#     # ct_out_path = os.path.join(ct_out_dir, ret[0] + '.nii.gz')
#     label_out_path = os.path.join(label_out_dir, ret[0] + '.nii.gz')
#
#     print(ct_out_path)
#
#     cta_nii = nib.Nifti1Image(crop_ct_data, affine=np.eye(4))
#     label_nii = nib.Nifti1Image(crop_laebl_data, affine=np.eye(4))
#
#     nib.save(cta_nii, ct_out_path)
#     nib.save(label_nii, label_out_path)
#
#     print('-------------------------')

    # break