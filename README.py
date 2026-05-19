# Autonomous-Robot-Using-the-ROS2-Jazzy-and-Gazebo-Harmonic
Obstacle Avoidance Robot → robot moves and avoids obstacles by itself. Autonomous Navigation Robot → robot creates a map, understands the environment, and goes to a target location automatically.
Step-by-Step Roadmap

We will make it in small steps so it becomes easy.

Step 1: Understand the Architecture

Your robot workflow will be:

Gazebo World → Robot Sensors → SLAM Mapping → Save Map → Navigation (Nav2) → Autonomous Goal Movement

You will learn:

Robot simulation in Gazebo
SLAM (mapping)
Map saving
Localization
Navigation using Nav2
Autonomous goal reaching
Step 2: Install Required Packages

Open terminal and run:

sudo apt update
sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup
sudo apt install ros-jazzy-slam-toolbox
sudo apt install ros-jazzy-turtlebot3*

After installation:

source /opt/ros/jazzy/setup.bash

Check package:

ros2 pkg list | grep nav2

If packages are installed properly, you will see nav2 packages.

Step 3: Launch TurtleBot3 in Gazebo

We will first practice using TurtleBot3 before making your own custom robot.

Terminal 1
source /opt/ros/jazzy/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

Expected:
✅ Gazebo opens
✅ Robot appears

Step 4: Start SLAM Mapping

Open new terminal

Terminal 2
source /opt/ros/jazzy/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch slam_toolbox online_async_launch.py

Expected:
✅ SLAM starts

Step 5: Open RViz

Open new terminal

Terminal 3
source /opt/ros/jazzy/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True

RViz will open.

You should see:

Laser scan
Map
Robot model
Step 6: Move Robot and Create Map

Open new terminal

Terminal 4

Control robot manually:

source /opt/ros/jazzy/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 run turtlebot3_teleop teleop_keyboard

Now drive robot using keyboard:

i = forward
, = backward
j = left
l = right
k = stop

Move robot slowly around the world.

Goal:

Cover complete area
SLAM should build map
Step 7: Save the Map

After mapping is complete:

Terminal 5
mkdir -p ~/maps
cd ~/maps

Save map:

ros2 run nav2_map_server map_saver_cli -f ~/maps/my_map

Expected files:

my_map.pgm
my_map.yaml
Step 8: Stop Everything

Close all terminals.

Step 9: Launch Robot Again
Terminal 1
source /opt/ros/jazzy/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
Step 10: Start Navigation with Saved Map
Terminal 2
source /opt/ros/jazzy/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch nav2_bringup navigation_launch.py \
use_sim_time:=True \
map:=~/maps/my_map.yaml
Step 11: Set Initial Pose in RViz

In RViz:

Click “2D Pose Estimate”
Click on robot position
Drag arrow in robot direction

This tells robot:

"You are here"

Step 12: Give Navigation Goal

In RViz:

Click “Nav2 Goal”
Select destination
Robot will move automatically

Expected:
✅ Robot plans path
✅ Avoids obstacles
✅ Reaches target automatically

Final Project Architecture
Gazebo
   ↓
Robot Sensors (LiDAR/Odom)
   ↓
SLAM Toolbox
   ↓
Map Creation
   ↓
Nav2 Stack
   ↓
Path Planning
   ↓
Autonomous Navigation
Important Concepts You Will Learn
SLAM → Simultaneous Localization and Mapping
Localization → Robot finding its position
Costmap → Obstacle understanding
Path Planning → Shortest safe path
Nav2 → ROS2 navigation stack

Since you already completed obstacle avoidance, I recommend doing this in 3 phases:

Phase 1: Mapping robot
Phase 2: Save map and localization
Phase 3: Autonomous navigation goal reaching

Start with Step 2 (installation) and tell me if it works. Then I’ll guide you to the next step based on your output/errors.

