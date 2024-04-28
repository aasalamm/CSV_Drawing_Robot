# CSV_Drawing_Robot

## Overview
This project aims to draw shapes based on a CSV file input with coordinates of points in the drawing. Once a file is chosen, the drawing is plotted and the coordinates are passed into an Inverse Kinematics solver to find the angles the motors need to be. This happens for each coordinate until the drawing is complete

Video URL: https://www.youtube.com/watch?v=5Uk5X_NYQGM

## User Interface
Ask user to pick between available shapes. If shape is not available, it will keep asking until the user gives it a valid shape

## Drawing 
Reads all coordinates from CSV file, plots the drawing, and passes coordinantes one by one to Inverse Kinematics Function

## Inverse Kinematics
Consists of a two DOF RR robot arm.

r = Distance between joint 1 to end effector (pen) <br />
H = Height of triangle formed (base = r, edges = motor arms) <br />
Theta 1 = Angle between D and Motor 1 Arm <br />
Theta 2 = Angle between Motor 1 Arm and Motor 2 Arm 

## Arduino Control
Inverse Kinematics outputs angles to write to Arduino Servo Motors
