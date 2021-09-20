#!/bin/sh
xterm  -e  " roslaunch hepta_robot hepta_robot_world.launch " &
sleep 3
xterm  -e  " roslaunch hepta_robot gmapping_demo.launch " &
sleep 3
xterm  -e  " roslaunch hepta_robot view_navigation.launch " &
sleep 3
xterm  -e  " rosrun teleop_twist_keyboard teleop_twist_keyboard.py " &
sleep 3