# PillarFocusNet
PillarFocusNet：a 3D point cloud object detection network based on perceptual diffusion and key feature understanding
# Introduction
PillarFocusNet marks a major advancement in the field of 3D point cloud object detection, extending the work of PointPillars. By incorporating sophisticated feature extraction techniques and a unique network architecture, PillarFocusNet establishes new standards for both accuracy and efficiency in 3D object detection tasks.

This approach introduces several key innovations designed to tackle the challenges posed by the sparsity and uneven distribution of point cloud data. Through optimized feature extraction and network design, PillarFocusNet achieves exceptional performance in detecting objects, surpassing previous methods in both precision and computational efficiency.

# Main Contributions
（1）Pillar Clustering Sampling Method: A new method that utilizes DBSCAN density clustering and central sampling techniques to efficiently address the challenges of sparsity and uneven distribution inherent in point cloud data.

（2）Mixed Pooling Dilated Convolution Layer: This novel layer integrates max pooling, average pooling, and dilated convolution to enrich feature extraction, while retaining spatial information. This combination improves the network’s capacity to capture a broader spectrum of contextual details.

（3）Space-Channel Synergistic Enhancement Module (SCS-EM): Located within the backbone network, the SCS-EM strengthens the synergy between spatial and channel information. It introduces an extra channel attention branch that employs horizontal and vertical global mean pooling, emphasizing important features across multiple dimensions. This enhancement significantly improves the network’s object detection performance.

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

