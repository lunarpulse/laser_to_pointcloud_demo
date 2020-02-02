# laser assembler node

## Brief

This pakckage shows how to use the assembler to make multiple scans into a point cloud

using gazebo demos and laser_assembler

clone this Repository
```
mkdir catkin_ws/src
git clone https://github.com/lunarpulse/laser_to_pointcloud_demo.git
```

change the chmod of the files
```
cd catkin_ws/src/<clone directory>
sudo chmod +x ./src/*.py
```

install dependencies
```
sudo apt-get install ros-kinetic-laser-assembler ros-kinetic-laser-geometry ros-kinetic-rqt-controller-manager ros-kinetic-ros-controllers ros-kinetic-gazebo-ros ros-kinetic-gazebo-ros-control ros-kinetic-robot-state-publisher ros-kinetic-ros-comm ros-kinetic-gazebo-plugins
```

launch with a launch file

```
catkin_make laser_to_pc
source ~/catkin_ws/devel/setup.bash
roslaunch laser_to_pcl start.launch
```
