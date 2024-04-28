# Awab A Salam Mohamed

import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from pyfirmata import Arduino, SERVO

########################
# Board initialization #
########################
port = 'COM7'
board=Arduino(port)

pin1 = board.digital[9]
pin1.mode=SERVO

pin2 = board.digital[11]
pin2.mode=SERVO

pin1.write(90)
pin2.write(90)

###################################################################################################
# Inverse Kinematics: Function takes coordinates and calculates motor angles then writes to motor #
###################################################################################################
def calculate_angles(x, y):

    link = 8 #cm

    phi = np.arctan2(y, x) #radiams
    phi = np.rad2deg(phi) #degrees

    d = np.sqrt((x**2) + (y**2)) #cm
    h = np.sqrt((link**2) - ((d / 2)**2)) #cm

    theta1 = np.arctan2(h, (d / 2)) #radians
    theta1 = np.rad2deg(theta1) #degrees

    theta2 = (90 - theta1) * 2 #degrees
    theta1 += phi

    if (theta1 > 0 and theta2 > 0):
        if (theta1 < 180 and theta2 < 180):
            pin1.write(theta1)
            pin2.write(theta2)
            time.sleep(2) #give enough time for worst case. 0 to 180 is the longest path, 2 seconds is enough time for motors to execute

#############################################################
# Reads CSV file, figures out coordinates and plots drawing #
#############################################################
def draw(filename):
    rectangle_list = []
    df = pd.read_csv(filename)

    rectangle_list = df.values.T.tolist() #makes data frame a list
    x = rectangle_list[0][:] #x coordinates
    y = rectangle_list[1][:] #y coordinates

    plt.plot(df['x'], df['y']) #plot all x and y
    plt.title("Shape")
    plt.show()

    for i in range(len(x)):
        calculate_angles(x[i], y[i]) #pass coordinates one by one to calculate angle
    return x, y

#############################
# Function Calls and Prompt #
#############################

def shape_select():
    while True:
        print("Shapes available are: ")
        print("   _ Rectangle")
        print("   - Star")
        print("   - Heart")

        input_shape = input("Choose A Shape:").lower()

        if input_shape == "star":
            star_csv = draw('star.csv')
        elif input_shape == "heart":
            heart_csv = draw('heart.csv')
        elif input_shape == "rectangle":
            rect_csv = draw('rectangle.csv')

shape_select()