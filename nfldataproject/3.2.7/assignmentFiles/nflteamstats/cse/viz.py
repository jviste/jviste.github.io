'''
viz.py creates data visualizations for use in CSE Lesson 3.2


Version 6/2/14. 
(c) 2014 Project Lead The Way, Inc
'''

import matplotlib.pyplot as plt
import numpy as np 
from . import stats as csestats
from scipy.stats import linregress, ttest_ind

def two_proportions(data, treatments=['Group 1','Group 2'],
                    p_and_q=['Yes','No']):
    '''
    Creates two pie charts and a graph comparing the proportions
    
    treatments = list of two strings labelling the two groups
    p_and_q = list of two strings describing the two segments of each group
    data is a list of four integers [number_p1, number_q1, number_p2, number_q2]
    
    returns plt.Figure, list of three plt.AxesSubplot
    '''
    number_p1, number_q1, number_p2, number_q2 = data
    
    #####
    # Create the pie graphs
    #####
    fig, ax = plt.subplots(1, 3, figsize=(15,5))
    
    # First pie chart
    ax[0].pie([number_p1, number_q1], labels=p_and_q, colors=['#ffff77', 'tan'], autopct='%.1f%%', startangle=180)
    ax[0].set_aspect(1)
    #Annotate with total number
    ax[0].set_title('\n'+treatments[0]+' (n='+str(number_p1+number_q1)+')')
    
    # Second pie chart
    ax[1].pie([number_p2, number_q2], labels=p_and_q, colors=['#ffff77', 'tan'], autopct='%.1f%%', startangle=180)
    ax[1].set_aspect(1)
    ax[1].set_title('\n'+treatments[1]+' (n='+str(number_p2+number_q2)+')')
    
    ########
    # Get Inferential Statistics on Proportions
    #######
    
    # Get the point estimates and errors bars for p
    p1, p1_errorbar = csestats.CI95_proportion(number_p1, number_q1)
    p2, p2_errorbar = csestats.CI95_proportion(number_p2, number_q2)
    pcombined, pcombined_errorbar = \
        csestats.CI95_proportion(number_p1 + number_p2,
                                  number_q1 + number_q2)

    ########
    # Visualize Inferential Statistics on Proportions
    #######

    # Draw the 95% confidence intervals for the proportion in each sampled subpopulation
    ax[2].errorbar([1, 2], [p1, p2], yerr=[p1_errorbar, p2_errorbar], fmt='o')
    # Draw the 95% confidence interval for the proportion in the whole population
    ax[2].errorbar(1.5, pcombined, yerr=pcombined_errorbar, fmt='rx')
    # Prevent the plot from being crammed up on the left
    ax[2].margins(.5) 
    
    # Label the two groups of people surveyed or whatever
    ax[2].set_xticks([1,1.5,2])
    ax[2].set_xticklabels([treatments[0], "\ncombined", treatments[1]])
    # Title it. 
    ax[2].set_title('Proportion that '+p_and_q[0]+'\n95% Confidence Intervals')
    ax[2].set_ylabel('Proportion')
    
   
    # Infer whether these are from the same population
    # Get the p-value
    z, p_value = csestats.p_different_proportions(number_p1, number_q1, 
                                                  number_p2, number_q2)    
    # Annotate the inferential stats with p_value
    stat_string = 'z = ' + '%.1f'%z
    annotate(ax[2], stat_string, p_value) # defined herein
                
    #####
    # Label figure
    #####
    title=fig.suptitle('Are The Results in These Two Pie Graphs Different by Coincidence?'+
        '\nDo '+treatments[0]+' '+p_and_q[0]+ ' more than '+treatments[1]+'?',
        size=14, x=.4, verticalalignment='top', horizontalalignment='center')
    
    return fig, ax
    
def annotate(ax, line_one, p_value):
    '''Annotate an Axes with inferential stats
    
    line_one is a string to be printed first in the annotation
    '''
    # Print lines_one and p 
    note = ax.text(0.5, 0.1, line_one + '\np=' + '%.2f'%p_value,
	            transform=ax.transAxes) # changes lowerleft coordinates of
	        # text to be Figure coordinates instead of Axes coordinates
	            
	        # The '%.2f'%p is formattingstring%variables.
	        # The formattingstring is '%.2f' which takes a float and creates
	        # a string of digits followed by a decimal and two more digits.
	    
    # Two dictionaries of matplotlib.patch.Patch properties
    # for p<0.5
    properties_yes = dict(boxstyle='round', facecolor='lime', alpha=0.6) 
    # for p>=0.5
    properties_no = dict(boxstyle='round', facecolor='white', alpha=0.6)
    # Set significant coorelations with these properties
    if p_value<0.05:
        note.set_bbox(properties_yes)
    else:
        note.set_bbox(properties_no)

def two_means(sample1, sample2, measurement_variable='Measurement', 
                measurement_unit='Unit', treatments=['Group 1','Group 2']):
    '''
    Creates two histograms a graph comparing the means' confidence intervals
    
    treatments = list of two strings labelling the two groups
    p_and_q = list of two strings describing the two segments of each group
    data is a list of four integers [number_p1, number_q1, number_p2, number_q2]
    
    returns plt.Figure, list of three plt.AxesSubplot
    '''
    
    ######
    #Calculate descriptive statistics of samples
    ######
    # sample 1
    xbar1 = np.mean(sample1) # sample mean
    s1 = np.std(sample1) # sample standard deviation
    n1 = len(sample1)
    
    # sample 2
    xbar2 = np.mean(sample2) # sample mean
    s2 = np.std(sample2) # sample standard deviation
    n2 = len(sample2)
    
    # Make a new array of the combined sample for operating on it with numpy
    combined_sample = np.append(sample1, sample2) # numpy.append is a function on two arrays, unlike Python List.append()
    xbar = np.mean(combined_sample) # sample mean
    s = np.std(combined_sample) # sample standard deviation
    
    #########
    # Calculate inferential statistics
    #########
    # Calculate the test statistic for two sample means 
    t, p_value = ttest_ind(sample1, sample2)
    
    ########
    # Visualize the histograms
    ########
    
    fig, ax = plt.subplots(1, 3, figsize=(15,5))
    color1 = 'red'
    color2 = 'blue'
    colorc = 'tan' # for combined sample
    # First histogram
    frequencies1, intervals, patches = ax[0].hist(sample1, color=color1) 
    ax[0].set_title('\n'+treatments[0]+' (n='+str(n1)+')')
    ax[0].set_xlabel(measurement_variable + ' (' + measurement_unit + ')' )
    ax[0].set_ylabel('Frequency')
    
    # Second histogram
    frequencies2, intervals, patches = ax[1].hist(sample2, color=color2) 
    ax[1].set_title('\n'+treatments[1]+' (n='+str(n2)+')')
    ax[1].set_xlabel(measurement_variable + ' (' + measurement_unit + ')' )
    ax[1].set_ylabel('Frequency')
    
    # Set x-a and y-axes to be the same for the two histograms
    xmin, xmax = [min(combined_sample), max(combined_sample)]
    ymin, ymax = [0, max(np.append(frequencies1,frequencies2))]
    # Make some padding
    xpad = (xmax-xmin)/20
    xmax += xpad
    xmin -= xpad
    ymax *= 1.10
    
    ax[0].set_xlim(xmin, xmax)
    ax[0].set_ylim(ymin, ymax)
    ax[1].set_xlim(xmin, xmax)
    ax[1].set_ylim(ymin, ymax)
    
    #Annotate both histograms with mean and +- standard deviation
    ax[0].vlines([xbar1-2*s1, xbar1, xbar1+2*s1], ymin, ymax, colors=color1, zorder=-1)
    ax[1].vlines([xbar2-2*s2, xbar2, xbar2+2*s2], ymin, ymax, colors=color2, zorder=-1)
    
    ax[0].text(xbar1+xpad/4, ymin+0.95*(ymax-ymin), '$x_1$', color=color1)
    ax[1].text(xbar2+xpad/4, ymin+0.95*(ymax-ymin), '$x_2$', color=color2)

    # Annotate each histogram with the other one's mean    
    ax[1].vlines(xbar1, ymin, ymax, colors=color1, zorder=-1)
    ax[0].vlines(xbar2, ymin, ymax, colors=color2, zorder=-1)
    
    ########
    # Visualize Inferential Statistics on Population Means
    #######
    # Title it. 
    ax[2].set_title('Inferred Mean ' + measurement_variable + '\n95% Confidence Intervals')
    ax[2].set_ylabel(measurement_variable + ' (' + measurement_unit + ')')
    
    # Draw the 95% confidence intervals for the mean of each sampled subpopulation
    ax[2].errorbar(1, xbar1, yerr=1.96*s1/n1**.5, color=color1, fmt='o')
    ax[2].errorbar(2, xbar2, yerr=1.96*s2/n2**.5, color=color2, fmt='o')
    # Label the two groups of people measured or whatever
    ax[2].set_xticks([1, 1.5, 2])
    ax[2].set_xticklabels([treatments[0],'\ncombined', treatments[1]])
    
    # Draw the 95% confidence interval for the mean of the combined population with H0
    ax[2].errorbar(1.5, xbar, yerr=1.96*s/(n1+n2)**.5, color=colorc, fmt='x')
    ax[2].margins(.5) # otherwise one of the error bars is crammed up on the left
    
    # Annotate the Inferential stats with p_value
    stat_string = 't = ' + '%.1f'%t
    annotate(ax[2], stat_string, p_value) # defined herein
            
    #####
    # Label figure
    #####
    title=fig.suptitle('Are These Two Distributions Different by Coincidence?',
        size=14, x=.4, verticalalignment='top', horizontalalignment='center')
    #title.set_y(.95)
    
    return fig, ax        
        
def bestline(ax, xdata, ydata, notate=False):
	    ''' Annotate an axes with the best fit line and stats on linear correlation
	    
	    ax is a single plt.SubplotAxes
	    xdata and ydata are each a list
	    notate is a boolean that determines whether to annotate with r^2 and p 
	    '''
	    # find best-fit line
	    m, b, r, p, E = linregress(xdata, ydata)
	    
	    # Draw the best fit line in blue
	    # Create values on best-fit line
	    xmin, xmax = ax.get_xlim()
	    x = np.linspace(xmin, xmax)
	    y = m*x + b
	    # Plot best fit line
	    ax.plot(x, y, 'b-')
	    
	    # Notate the linear correlation
	    stat_string = '$r^2$=' + str(int(r**2*100)) + '%'
	    annotate(ax, stat_string, p)
	        
def sort_by_category(data, category):
	    '''separates data into two lists
	    
	    data is a list
	    category is a list of 0s and 1s
	    category[i] and data[i] describe a single data point
	    returns data0, data1 which are both lists, subsets of data
	    '''
	    data0=[]
	    data1=[]
	    for datum, mycategory in zip(data, category):
	        if mycategory==0:
                    data0.append(datum)
	        else:
	            data1.append(datum)
	    return data0, data1

def ticks_for_arrayplot(ax):
    ''' Adjust tick mark displays: Place two ticks and pad them inwards
        
    ax is a square two-dimensional array of plt.SubplotAxes
    '''
    padding = 0.15 
    number_of_variables = len(ax)
    # For bottom row
    for column in range(number_of_variables):
        row = number_of_variables-1 # last row
        # Get the range of axes of this plot
        xmin, xmax = ax[row][column].get_xlim()
        
        #make just two ticks on x axis 
        ax[row][column].set_xticks([xmin, xmax])
        
        # Provide some padding
        dx = xmax - xmin
        ax[row][column].set_xlim(xmin-padding*dx, xmax+padding*dx)
        
    # For left column
    for row in range(number_of_variables):
        column = 0 # first column
        # Get the range of axes of this plot
        ymin, ymax = ax[row][column].get_ylim()
        
        #make just two ticks on y axis 
        ax[row][column].set_yticks([ymin, ymax])
        
        # Provide some padding
        dy = ymax - ymin
        ax[row][column].set_ylim(ymin-padding*dy, ymax+padding*dy)
        
def scatter_plot_array(variables):     
    ''' Creates a scatter plot array
    variables is a list of cse.Variables
    
    returns fig, ax
    fig = matplotlib.pyplot.Figure
    ax = list of lists of matplotlib.pyplot.SubplotAxes 
    '''
    
    #####
    # Create the scatter plot array
    #####
    number_of_variables = len(variables)
    fig, ax = plt.subplots(number_of_variables, number_of_variables, 
        sharex='col', sharey='row')        
    
    # Plot data
    # For all graphs
    for row in range(number_of_variables):
        for column in range(number_of_variables):
            ax[row][column].plot(variables[column].data, 
                                variables[row].data, 'ro')
    
    # Function defined earlier, should be method of a new class ScatterPlot
    ticks_for_arrayplot(ax)

    # Annotate with linear correlation if quantity vs. quantity
    for row in range(number_of_variables):
        for column in range(number_of_variables):
            if variables[row].type=='numeric' and \
                variables[column].type=='numeric' and row != column:
                bestline(ax[row][column], 
                    variables[column].data, variables[row].data, notate=True)
                      
    # Label columns
    for column in range(number_of_variables):
        ax[0][column].text(0.5, 1.1, variables[column].label,
            horizontalalignment='center', verticalalignment='bottom',
            transform=ax[0][column].transAxes)
        
    # Label rows
    for row in range(number_of_variables):
        ax[row][0].text(-0.3, 0.5, variables[row].label, rotation=90,
        horizontalalignment='right', verticalalignment='center',
            transform=ax[row][0].transAxes)    

    # Next two nested for loops do nothing; retained only in case for later use
    
    #For lower-left half of graphs, not including midline
    for row in range(number_of_variables):
        for column in range(row):
            pass

    # For upper right half and \ diagonal
    for row in range(number_of_variables):
        for column in range(row, number_of_variables):
            pass
            # Hide everything of the plot box altogether
            # ax[row][column].axis('off')
                        
    #####
    # Label figure
    #####
    fig.text(0.5, 0.98, 'How much is each variable correlated with another variable?', 
        horizontalalignment='center')
    
    return fig, ax