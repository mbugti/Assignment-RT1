# Assignment-RT1

## Authors
* Malook : Malookbugti93@gmail.com

## Introduction
This repository contains a python script that asks user for coordinates and turtlebot will start moving to the described inputs


## Contents of the repository
In this section we will explain the repository's content.

### Src
Source folder that contains the scripts
* Goal.py (Python script that ask the user for Goal's Coordinates)

### Project_documentation
This folder contains doxygen documntation of the project

## Installation
The first thing to do, after having cloned the repository in the Ros workspace, is to build the package and install in order to make the files executable, using the following commands in the workspace:
   
   
    catkin_make
    catkin_make install
    
Execute the following commands for Ros related Python libraries     
   
   
	sudo apt-update
	sudo apt install python3-pip
    sudo apt-get install python3-yaml	
    sudo pip3 install rospkg catkin-pkg 

To install Turtlebot in your system
   ```
   cd ~/catkin_ws/src/
   git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
   git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
   cd ~/catkin_ws && catkin_make
   gedit ~/.bashrc
   ```
Add this line to your .bashrc file
   ```
   export TURTLEBOT3_MODEL=burger
   ```   
  * This will install Ros related python libraries and Turtlebot
    
 Before running the python scripts, remember two things
 * Setup your bash file. It can be done by going to root directory of your catkin_ws and use the following command in the terminal
    ```
    
    source devel/setup.bash
    
 * Add file path to your Bashrc. Go to homw directory, enable the hidden files. You will see a file " .bashrc" . At the bottom of the file add your file path. For example if your workspace goes by the name of catkin_ws. Add the following line
    
    ```
    source /home/malook/catkin_ws/devel
    
To run the system:
    
    rosrun assignment Goal.py
    
