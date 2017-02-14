# -*- coding: utf-8 -*-
'''
Group Members: Jumhelle Viduya, Janelle Viste
Assignment: Activity 3.2.7 | Investigating with Data
'''
import re
import time
import math
import random
import numpy as np
import os.path
import matplotlib.pyplot as plt

# Modifiying graph to Beautify :3
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Arial')
        item.set_fontsize(16)

# Get the NFL player weight/height data from CSV
NFLTeams = ['49ers','Bears' ,'Bengals' ,'Bills' ,'Browns' ,'Buccaneers' 
,'Cardinals' ,'Chargers','Chiefs' ,'Colts' ,'Cowboys' ,'Dolphins' ,'Eagles' ,'Falcons' 
,'Giants' ,'Jaguars' ,'Jets' ,'Lions' ,'Packers' ,'Panthers' ,'Patriots' ,'Raiders' 
,'Rams','Ravens' ,'Redskins' ,'Saints' ,'Seahawks' ,'Steelers' ,'Texans' 
,'Titans' ,'Vikings']

# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))

#==============================================\
# Initializing the aggregators (Based on Type) \
#==============================================\

# Subjective (categorical, etc.)          
playerNames = []
statusData = []
teamcount = 0 

injured_lowBMI = 0
notInjured_lowBMI = 0

injured_highBMI = 0
notInjured_highBMI = 0

injured_total = 0
notInjured_total = 0

# Quantitative (Numbers, etc.)
heightData = []
weightData = []
bmiData = []


#_________________Actual Activty Code___________________________________________________________
'''
***********************************************
Finding Height, Weight, Injury Status, and BMI
***********************************************
'''
# Scan each NFL Team's file at a time
for team in NFLTeams:
    teamcount = teamcount + 1 # To count how many teams there are
    # Open the file
    filename = os.path.join(directory, str(team)+'.csv')
    datafile = open(filename,'r')
    data = datafile.readlines()
    # Go through all the heights and weights in that file
    for line in data[1:]:
        #linechecker = line.strip()
        #print(linechecker)
        lastname, firstname, pos, status, height, weight = line.split(",")
        
        #===================================\
        # Convert String Height into Inches \
        #===================================\ 
        #____________________________________________Feet to Inches____________
        height_in_feet = height.split("'") 
        feet = int(height_in_feet[0])
        inches = int(height_in_feet[1])
        height_in_inches = (feet*12) + (inches)
        #___________________________________________Inches to Meters___________
        height_in_meters = height_in_inches*0.025
        
        #===============================\ 
        # Calculate BMI of EACH Player  \ 
        #===============================\ 
        if weight.isdigit() == True:
            player_Weight = int(weight)
        else:
            player_Weight = int(weight.replace("\n", ""))
        player_Weight_in_kilograms = player_Weight*0.45
        player_Height_Squared = height_in_meters**2
        bmi = float(player_Weight_in_kilograms)/float(player_Height_Squared) 
        
        playerNames.append(firstname+lastname)
        statusData.append(status)
        heightData.append(height_in_meters)
        weightData.append(player_Weight_in_kilograms)
        bmiData.append(round(bmi,1))
        
        print("NFL Team: "+ str(team))
        print('Player (Name): '+ str(lastname + "," + firstname))
        print('Status (Injured, etc.): '+ status)
        print('Height (meters): '+ str(height_in_meters))
        print('Weight (kilograms): '+ str(player_Weight))
        print('BMI: '+ str(round(bmi,1)) + '\n' + '-'*35 + '\n')
       
        #time.sleep(.3)
        
        #If player is above average BMI (not healthy)
        if bmi > 32.1596276355:    
            if ((status == 'RES') or (status == 'NO')):
                injured_highBMI = injured_highBMI + 1
            else:
                notInjured_highBMI = notInjured_highBMI + 1
        #If player is below average BMI (healthy)
        else: 
            if ((status == 'RES') or (status == 'NO')):
                injured_lowBMI = injured_lowBMI + 1
            else:
                notInjured_lowBMI = notInjured_lowBMI + 1
    #Close that year's file
    datafile.close()
time.sleep(1)


'''
*******************************************************************
Finding Concussion Rates & # of Concussions (from years 2012-2015)
*******************************************************************
'''
'''
o_Pos = ['Wide Receiver', 'Offensive Tackle', 'Running Back', 'Tight End',
'Guard', 'Center', 'Quarterback']
d_Pos = ['Cornerback', 'Safety', 'Linebacker', 'Defensive End', 'Defensive Tackle']
'''
offenseData = []
WR = []
OT = []
RB = []
TE = []
G = []
C = []
QB = []
defenseData = []
CB = []
S = []
LB = []
DE = []
DT = []

x_axis_increments = [2012, 2013, 2014, 2015]

#=====================================\ 
# ALL Player injuries (ALL Postions)  \ 
#=====================================\ 

# Open the file "ConcussionsByPosition.csv" to grab data for concussion numbers
filename2 = os.path.join(directory, 'ConcussionsByPosition.csv')
datafile2 = open(filename2,'r')
data2 = datafile2.readlines()
# Go through all the concussion data in that file
for line2 in data2[2:]:
    #linechecker2 = line2.strip()
    #print(linechecker2)
    position, postype, yr2012, yr2013, yr2014, yr2015 = line2.split(',')
    
    #==========================\
    # Acquiring Offense Data   \
    #==========================\
    if position == 'Offense':
        if postype == 'Wide Receiver':
            WR.append(yr2012)
            WR.append(yr2013)
            WR.append(yr2014)
            WR.append(yr2015)
        elif postype == 'Offensive Tackle':
            OT.append(yr2012)
            OT.append(yr2013)
            OT.append(yr2014)
            OT.append(yr2015)
        elif postype == 'Running Back':
            RB.append(yr2012)
            RB.append(yr2013)
            RB.append(yr2014)
            RB.append(yr2015) 
        elif postype == 'Tight End':
            TE.append(yr2012)
            TE.append(yr2013)
            TE.append(yr2014)
            TE.append(yr2015)
        elif postype == 'Guard':
            G.append(yr2012)
            G.append(yr2013)
            G.append(yr2014)
            G.append(yr2015)
        elif postype == 'Center':
            C.append(yr2012)
            C.append(yr2013)
            C.append(yr2014)
            C.append(yr2015)
        elif postype == 'Quarterback':
            QB.append(yr2012)
            QB.append(yr2013)
            QB.append(yr2014)
            QB.append(yr2015)
        else: # Last two lines of csv file w/ **OFFENSE totals** per year
            offenseData.append(yr2012)
            offenseData.append(yr2013)
            offenseData.append(yr2014)
            offenseData.append(yr2015)
    
    #==========================\
    # Acquiring Defense Data   \
    #==========================\    
    elif position == 'Defense':
        if postype == 'Cornerback':
            CB.append(yr2012)
            CB.append(yr2013)
            CB.append(yr2014)
            CB.append(yr2015)
        elif postype == 'Safety':
            S.append(yr2012)
            S.append(yr2013)
            S.append(yr2014)
            S.append(yr2015)
        elif postype == 'Linebacker':
            LB.append(yr2012)
            LB.append(yr2013)
            LB.append(yr2014)
            LB.append(yr2015)
        elif postype == 'Defensive End':
            DE.append(yr2012)
            DE.append(yr2013)
            DE.append(yr2014)
            DE.append(yr2015)
        elif postype == 'Defensive Tackle':
            DT.append(yr2012)
            DT.append(yr2013)
            DT.append(yr2014)
            DT.append(yr2015)
        else: # Last two lines of csv file w/ **DEFENSE totals** per year
            defenseData.append(yr2012)
            defenseData.append(yr2013)
            defenseData.append(yr2014)
            defenseData.append(yr2015)
    
    print("Position (O/D): " + str(position))
    print("Position Type: " + str(postype))
    print("Concussions Each Year: ")
    print("    2012   =>   " + str(yr2012))
    print("    2013   =>   " + str(yr2013))
    print("    2014   =>   " + str(yr2014))
    print("    2015   =>   " + str(yr2015))
    concussTotal = int(yr2012)+int(yr2013)+int(yr2014)+int(yr2015)
    print("Total = "+ str(concussTotal) + '\n' + '-'*35 + '\n')



###################################
# Calculating the Mean and Median  
###################################

#___________________________Mean___________________________________
number_of_elements = len(bmiData) # The number of list elements
sum_of_elements = sum(bmiData) # The sum of list elements
mean = sum_of_elements/number_of_elements

#__________________________Median__________________________________
bmiData.sort()
median = bmiData[int(number_of_elements/2)]

for i in range(3):
    print()
print("================================")
print(" List of Mean and Median Values ")
print("================================")
print("<> Mean: " + str(mean))
print("<> Median: " + str(median))



#_________________________BMI of Entire NFL Roster_________________________

#######################
# Create the Histogram  
#######################

# Bin size determined using sources
increment_val = int(math.sqrt(float(len(bmiData))))     
start = int(min(bmiData))
end = int(max(bmiData))

fig_bmi, ax = plt.subplots(1, 3)
ax[0].hist(bmiData, color="red", bins=range(start, end, 1))
ax[0].set_title('BMI Distribution (Histogram)')
ax[0].set_xlabel('NFL Player BMI (BMI Scale)')
ax[0].set_ylabel('Frequency (# of players w/ BMI)')
make_PLTW_style(ax[0])

#########################
# Create the Scatterplot  
#########################

ax[1].scatter(weightData, heightData, color="blue", s=10)
ax[1].set_title('Height vs. Weight (Scatterplot)')
ax[1].set_xlabel('Weight (kg)')
ax[1].set_ylabel('Height (m)')
make_PLTW_style(ax[1])

########################
# Create the Boxplot
########################

ax[2].boxplot(bmiData)
ax[2].set_title('BMI Distribution (Boxplot)')
ax[2].set_ylabel('Distance from center (increments of 2)')
fig_bmi.show()

######################################################
# Create Difference between Proportions Visualization
######################################################

import cse
reload(cse) # make import fresh in case code was modified

# Get the data from NFL player stats

# The two categories of each pie chart.
p_and_q = ['Injured', 'Not Injured'] # [p-label, q-label]
# The two groups of people (or whatever) being compared
treatments = ['Below Average BMI','Above Average BMI'] 

# Data of Injured/Non-Injured NFL Players (based on BMI)
number_p1 = injured_lowBMI       # INJURED players w/ bmi |||BELOW AVERAGE|||
number_q1 = notInjured_lowBMI    # NON-INJURED players w/ bmi |||BELOW AVERAGE|||
number_p2 = injured_highBMI      # INJURED players w/ bmi |||ABOVE AVERAGE|||
number_q2 = notInjured_highBMI   # NON-INJURED players w/ bmi |||ABOVE AVERAGE|||

injuryData = [number_p1, number_q1, number_p2, number_q2] # use values from above
fig_proportions, ax = cse.viz.two_proportions(injuryData, treatments, p_and_q)
fig_proportions.show()

#####################
# Create Line Graph  (Concussions over Time by Position)
#####################

years = [2012, 2013, 2014, 2015]
labels = ['2012', '2013', '2014', '2015']

fig_concussions, ax = plt.subplots(1,3)
fig_concussions.suptitle('NFL Concussions Over Time (By PlayerPosition)')

ax[0].set_title('Offense Totals')
ax[0].set_xlabel('Time (Years)')
ax[0].set_ylabel('Concussion Frequency (# of Concussions)')
ax[0].plot(years, WR, linestyle='-', color='red', label='Wide Receiver')
ax[0].plot(years, OT, linestyle='-', color='orange', label='Offensive Tackle')
ax[0].plot(years, RB, linestyle='-', color='yellow', label='Running Back')
ax[0].plot(years, TE, linestyle='-', color='lime', label='Tight End')
ax[0].plot(years, G, linestyle='-', color='aqua', label='Guard')
ax[0].plot(years, C, linestyle='-', color='green', label='Center')
ax[0].plot(years, QB, linestyle='-', color='blue', label='Quarterback')
ax[0].legend(loc=1)
ax[0].xaxis.set_ticks(np.arange(min(years), max(years)+1, 1.0))
ax[0].set_xticklabels(labels)

ax[0].set_title('Defense Totals')
ax[1].set_xlabel('Time (Years)')
ax[1].set_ylabel('Concussion Frequency (# of Concussions)')
ax[1].plot(years, CB, linestyle='-', color='black', label='Cornerback')
ax[1].plot(years, S, linestyle='-', color='brown', label='Safety')
ax[1].plot(years, LB, linestyle='-', color='red', label='Linebacker')
ax[1].plot(years, DE, linestyle='-', color='green', label='Defensive End')
ax[1].plot(years, DT, linestyle='-', color='blue', label='Defensive Tackle')
ax[1].legend(loc=1)
ax[1].xaxis.set_ticks(np.arange(min(years), max(years)+1, 1.0))
ax[1].set_xticklabels(labels)

ax[0].set_title('Offense vs Defense Totals')
ax[2].set_xlabel('Time (Years)')
ax[2].set_ylabel('Concussion Frequency (# of Concussions)')
ax[2].plot(years, offenseData, linestyle='-', color='red', label='Offense Total')
ax[2].plot(years, defenseData, linestyle='-', color='blue', label='Defense Total')
ax[2].legend(loc=1)
ax[2].xaxis.set_ticks(np.arange(min(years), max(years)+1, 1.0))
ax[2].set_xticklabels(labels)
fig_concussions.show()

'''
Sources Used:
    BMI Data:
        https://www.sportingcharts.com/articles/nfl/what-is-the-average-bmi-of-an-nfl-player.aspx
    Concussion Data:
        http://apps.frontline.org/concussion-watch/#positions_2015
        http://www.cbssports.com/nfl/injuries
        https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3438866/
    Arranging Bins Help:
        http://stats.stackexchange.com/questions/798/calculating-optimal-number-of-bins-in-a-histogram
'''