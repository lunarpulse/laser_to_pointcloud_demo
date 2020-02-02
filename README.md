# laser assembler node

## Brief

This pakckage shows how to use the assembler to make multiple scans into a point cloud

using gazebo demos and laser_assembler

install dependencies
```
sudo apt-get install ros-kinetic-laser-assembler ros-kinetic-laser-geometry ros-kinetic-rqt-controller-manager ros-kinetic-ros-controllers ros-kinetic-gazebo-ros ros-kinetic-gazebo-ros-control ros-kinetic-robot-state-publisher ros-kinetic-ros-comm ros-kinetic-gazebo-plugins
```

launch with a launch file

```
source ~/catkin_ws/devel/setup.bash
roslaunch laser_to_pcl start.launch
```
