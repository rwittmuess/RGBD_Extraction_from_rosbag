# RGBD_Extraction_from_rosbag
Convenient way of extracting images and sensor data from ROS bag files to python.

## Setup
To create the envrionment used for this code, navigate to the directory of the repository and run the following commands.

    conda env create -f environment.yaml
    conda activate RGBD-extraction-py310

You can see and delete the created environment by using

    conda env list
    conda env remove --name RGBD-extraction-py310

## Use
The jupyter notebook "how to use" in an interactive way how to use the functions provided by the repository. 


## Still Work In Progress:
* OPtimize Runtime
* Simplify use
* Comment
* ...


## Further information
If data is *NOT* captured from the ROS terminal I can be worth it to have a look into "read_bag_example.py". This seems to be a convenient way of working with data from the Intel RealSense.

In this case valuable insights and approaches could potentially be found here: [https://github.com/IntelRealSense/librealsense/blob/jupyter/notebooks/distance_to_object.ipynb]  

