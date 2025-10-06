# Joey 1 Documentation

This project implements a **differential drive controller** using **ROS 1 Melodic** and **Nvidia Jetson Nano**. It includes features like:

- **Rviz simulation**  
- **robot_localization** ([Documentation](https://docs.ros.org/en/melodic/api/robot_localization/html/index.html))  
- **SLAM**  
- **Navigation** ([Navigation Stack](https://wiki.ros.org/navigation))  

---

## Getting Started

Before starting, ensure the following:

1. **Operating System:** Ubuntu 18.04  
2. **ROS Version:** ROS 1 Melodic installed on your machine (desktop or laptop).  
3. **Git:** Installed and configured.  

Install the Python dependencies:

```bash
pip install -r requirements.txt
Recommended Tools and Extensions
VS Code Extensions:

C/C++ Extension Pack

Python

ROS Melodic

YAML

Optional Tool: Terminator – Useful for managing multiple terminals with ROS.

Setting Up ROS Workspace
1. Create a Catkin Workspace
bash
Copy code
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
2. Install ROS 1 Packages
Follow the instructions for ROS 1 Melodic Installation:
ROS Melodic Installation Guide

3. Install Python Requirements for Workspace
bash
Copy code
cd ~/catkin_ws/src
pip install -r requirements.txt
4. Build the Workspace
bash
Copy code
cd ~/catkin_ws/
catkin_make
5. Source Workspace
bash
Copy code
source ~/catkin_ws/devel/setup.bash
Running ROS Nodes
Start ROS master:

bash
Copy code
roscore
Run your nodes in a new terminal:

bash
Copy code
rosrun <package_name> <node_name>
Launch Rviz for visualization:

bash
Copy code
rosrun rviz rviz
References
Differential Drive Controller

robot_localization

ROS Navigation Stack

pgsql
Copy code

This is fully in **Markdown format** ready for a GitHub README.  

If you want, I can also make a **version that is entirely command-oriented inside Markdown**, so users don’t have to read instructions separately—they just copy-paste the commands from the README.  

Do you want me to do that version?








