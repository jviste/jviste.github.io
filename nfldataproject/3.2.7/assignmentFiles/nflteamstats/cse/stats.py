'''
differenceBetweenProportions.py creates two proportions, MonteCarlo style,
from a known proportion in the population and from two sample sizes.
The two proportions are illustrated by two pie charts.
A third graphic shows the 95% confidence intervals for the proportions. 
A p-value is shown, highlighted green is p<0.05.
Alternate code allows the same visualization to be produced from real data.

Version 6/2/14. 
(c) 2014 Project Lead The Way, Inc
'''

from scipy.stats import norm as scipy_stats_norm

def CI95_proportion(number_p, number_q):
    '''Calculate 95% confidence interval for proportion p 
    
    number_p, number_q 
    are both positive integers
    
    returns:
    p, p_errorbar = floats
    Less than 5% chance of observing data (or stranger) if population proportion is 
    further than p_errorbar from p.
    '''
    
    # Caluclate percentages
    number_group = number_p + number_q
    p = 1.0* number_p/number_group # observed proportion of "yes" in sample 
    q = 1 - p
    # Calculate 95% confidence interval
    p_errorbar = 1.96 * (p*q/number_group)**.5 # two standard deviations include 95% of the area of the normal distribution, which approximate the binomial distribution for n>=30
    return p, p_errorbar

def p_different_proportions(number_p1, number_q1, number_p2, number_q2):
    '''Calculate probability of data if the two groups are inferential statistics
    
    number_p1 = number in group 1 who said "p"
    number_q1 = number in group 1 who said "q"
    number_p2 = number in group 2 who said "p"
    number_q2 = number in group 2 who said "q"
    are all positive integers; statistical test has further assumptions.
    
    returns:
    z, p_value
    
    p_value = probability that data from two random samples of a single population
    would be at least this different from each other   
    '''
    
    # Group sizes
    number_group1 = number_p1 + number_q1
    number_group2 = number_p2 + number_q2
    
    # Portions in combined group
    number_p = number_p1 + number_p2
    number_q = number_q1 + number_q2
    
    #Get on each treatment group
    p1, p1_errorbar =  CI95_proportion(number_p1, number_q1)
    p2, p2_errorbar = CI95_proportion(number_p2, number_q2)
    
    # observed  proportion of "yes" in both samples combined
    pcombined = 1.0*number_p/(number_group1 + number_group2)
    
    z = (p1-p2)/(pcombined*(1-pcombined)/number_group1 + pcombined*(1-pcombined)/number_group2)**.5    
    p_value = (scipy_stats_norm.sf(abs(z)))*2 # Two tailed test
    
    return z, p_value 