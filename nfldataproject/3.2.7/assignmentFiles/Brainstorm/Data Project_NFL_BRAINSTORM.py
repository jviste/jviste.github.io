'''
Group Members: Jumhelle Viduya, Janelle Viste
Assignment: Activity 3.2.7 | Investigating with Data
'''
import random
import numpy as np
import os.path
import matplotlib.pyplot as plt
import time

height = [72, 74, 77, 79, 70, 68, 52]           #height in inches(in)
weight = [220, 252, 260, 242, 220, 190]         #weight in pounds(lbs)
bmi = []

for h, w in height, weight:
    player_bmi = float(height[h]) / float(weight[w])
    bmi.append(player_bmi)
    print("Player Height: ", str(height[h]))
    print("Player Weight: ", str(weight[w]))
    print("BMI (Body Mass Index): ", str(player_bmi))
    time.sleep(1)


         