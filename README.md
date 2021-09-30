# 2021-robot_guide

## Organization

.
├── deps		-	Dépendances du projet
└── robot_guide
    ├── launch		- 	Launch files
    ├── models		- 	Map and robot files for simulation
    ├── params		- 	Parameter files
    ├── urdf		- 	Robot descriptions
    └── web		- 	Web files


# Installation

## Prerequisites

[Installing ROS Environment](http://wiki.ros.org/fr/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

Dependencies :

* `ros-melodic-web-video-server-*`

* `ros-melodic-pid`

* `ros-melodic-ecl-*`

* `ros-melodic-yocs-controllers`

* `ros-melodic-laser-*`

* `ros-melodic-joy-*`

* `ros-melodic-urg-node`

* `ros-melodic-rosbridge-*`

* `ros-melodic-dwa-local-planner-*`

* `ros-melodic-move-base`

* `ros-melodic-gmapping`

* `ros-melodic-dynamic-reconfigure`

* `ros-melodic-gazebo-ros`

Pour lancer les simulations :

* `ros-melodic-desktop-full`

* `ros-desktop`

* `ros-melodic-freenect-*`

Install robot_guide project :

```bash
cd <catkin_repo>/src
git clone https://github.com/CARMinesDouai/2021-robot_guide
cd ..
catkin_make
```

## Run project

```
roslaunch robot_guide simulation.launch
roslaunch robot_guide gmapping.launch
roslaunch turtlebot_teleop keyboard_teleop.launch

rviz -d `rospack find robot_guide`/config/gmapping.rviz
```

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
