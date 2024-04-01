# PillarFocusNet
PillarFocusNet：a 3D point cloud object detection network based on perceptual diffusion and key feature understanding
# Introduction
PillarFocusNet represents a significant leap forward in the domain of 3D point cloud object detection, building upon the foundations laid by PointPillars. By introducing advanced feature extraction methods and a novel network architecture, PillarFocusNet sets new benchmarks for accuracy and efficiency in detecting objects within 3D point clouds.

This project introduces several key innovations to overcome the challenges of sparsity and non-uniform distribution of point cloud data, achieving superior object detection performance through enhanced feature extraction and network optimization techniques.

# Main Contributions
（1）Pillar Clustering Sampling Method: A novel approach that leverages DBSCAN density clustering and central sampling techniques to effectively manage the inherent sparsity and non-uniform distribution of point cloud data.

（2）Mixed Pooling Dilated Convolution Layer: This innovative layer combines max pooling, average pooling, and dilated convolution to diversify feature extraction while preserving spatial information, enhancing the network's ability to comprehend a wider range of contextual information.

（3）Space-Channel Synergistic Enhancement Module (SCS-EM): Positioned within the backbone network, the SCS-EM enhances spatial and channel information synergy. By incorporating an additional channel attention branch that utilizes horizontal and vertical global mean pooling, it highlights key features across multiple dimensions, significantly boosting the network's object detection capabilities.

# Installation
## Prerequisites
Python 3.8
PyTorch 1.11.0
CUDA 11.3

# Steps
Clone the repository and install the dependencies:
```
git clone https://github.com/yourgithubusername/PillarFocusNet.git
cd PillarFocusNet
pip install -r requirements.txt
```

# Usage
To run PillarFocusNet on your dataset, follow these steps:
```
python tools/train.py --config.py
```

# Dataset
1.Download
Download point cloud(29GB), images(12 GB), calibration files(16 MB)和labels(5 MB)。Format the datasets as follows:
```
kitti
    |- training
        |- calib (#7481 .txt)
        |- image_2 (#7481 .png)
        |- label_2 (#7481 .txt)
        |- velodyne (#7481 .bin)
    |- testing
        |- calib (#7518 .txt)
        |- image_2 (#7518 .png)
        |- velodyne (#7518 .bin)
```

2.Pre-process KITTI datasets First
```
cd PointPillars/
python pre_process_kitti.py --data_root your_path_to_kitti
```
Now, we have datasets as follows:
```
kitti
    |- training
        |- calib (#7481 .txt)
        |- image_2 (#7481 .png)
        |- label_2 (#7481 .txt)
        |- velodyne (#7481 .bin)
        |- velodyne_reduced (#7481 .bin)
    |- testing
        |- calib (#7518 .txt)
        |- image_2 (#7518 .png)
        |- velodyne (#7518 .bin)
        |- velodyne_reduced (#7518 .bin)
    |- kitti_gt_database (# 19700 .bin)
    |- kitti_infos_train.pkl
    |- kitti_infos_val.pkl
    |- kitti_infos_trainval.pkl
    |- kitti_infos_test.pkl
    |- kitti_dbinfos_train.pkl
```

