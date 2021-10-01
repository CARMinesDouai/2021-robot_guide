# 2021-robot_guide

Ce projet a pour but de créer un robot capable de suivre un QR code.

Ce projet contient :

* Un serveur web utilisateur, permettant d'obtenir le QR code;

* Un serveur web administrateur, affichant un flux vidéo et la carte générée.

## Organization

deps		-	Dépendances du projet

robot_guide :

config      -   Rviz configuration files

launch		- 	Launch files

models		- 	Map and robot files for simulation

params		- 	Parameter files

urdf		- 	Robot descriptions

web-admin		- 	Web administrator files

web-user		- 	Web user files

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

Python :

* `pandas`

* `pyzbar`

* `zbar-tools`

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

Pour lancer une simulation du projet :

```
roslaunch robot_guide simulation.launch
roslaunch robot_guide gmapping.launch
roslaunch turtlebot_teleop keyboard_teleop.launch

rviz -d `rospack find robot_guide`/config/gmapping.rviz
```

Run video server :

`roslaunch robot_guide video.launch`

Run minimal bringup :

`roslaunch robot_guide bringup_minimal.launch`

Run QR code tracking :

`rosrun robot_guide qr_code_tracking.py`

Run web-user server :

```bash
roscd robot_guide/web-user
node app.js
```

Run web-admin server :

```bash
roscd robot_guide/web-admin
node app.js
```

# Améliorations

* Créer un script mettant en place le serveur ad-hoc automatiquement

# Participants
LECLERCQ Vinciane - VERGAERT Arthur - DELIEGE Victor
