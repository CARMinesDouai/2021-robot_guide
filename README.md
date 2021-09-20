# 2021-robot_guide

# Installation

## Prerequisites

[Installing ROS Environment](http://wiki.ros.org/fr/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

Dependencies :

* `ros-melodic-freenect-*`

* `ros-melodic-web-video-server-*`

* `ros-melodic-pid`

Install robot_guide project :

```bash
cd <catkin_repo>/src
git clone https://github.com/CARMinesDouai/2021-robot_guide
cd ..
catkin_make
```

## Run project

Run simulation :

`roslaunch robot_guide simulation.launch`

Run gmapping :

`roslaunch robot_guide gmapping.launch`

Run video :

`roslaunch robot_guide video.launch`

Run minimal bringup :

`roslaunch robot_guide bringup_minimal.launch`

Run web server :

```bash
roscd robot_guide/web
node app.js
```

# Participants
LECLERCQ Vinciane - VERGAERT Arthur - DELIEGE Victor
