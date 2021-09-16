# 2021-robot_guide
deps => dossier contenant les dépendances du projet
robot_guide => dossier du projet

# Installation

## Prerequisites

* [Installing ROS Environment](http://wiki.ros.org/fr/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

Install robot_guide project :

```bash
cd <catkin_repo>/src
git clone https://github.com/CARMinesDouai/2021-robot_guide
cd ..
catkin_make
```

Run simulation :

`roslaunch robot_guide simulation.launch`

Run gmapping :

`roslaunch robot_guide gmapping.launch`

Run web server :

```bash
roscd robot_guide/web
node app.js
```

# Participants
LECLERCQ Vinciane - VERGAERT Arthur - DELIEGE Victor
