'''
cse.montecarlo contains functions for generating simulated data.

Version 6/2/14. 
(c) 2014 Project Lead The Way, Inc
'''
import random
import cse # do not reload and there be no circular import
import numpy as np

def two_categories(number, proportion):
    ''' Simulate a data set of 0's and 1's.
    
    number = (int) number of elements in simulated data
    proportion = (float) probability that any given element is 1
    
    Returns:
    number_p (int), number_q (int), elements (list of 0s and 1s)    
    '''
    
    elements = []
    number_p, number_q = 0, 0
    for counter in range(number):
        if random.uniform(0, 1)<proportion:
            elements.append(1)
            number_p += 1
        else:
            elements.append(0)
            number_q += 1 
    return number_p, number_q, elements
    
def retail_data(number_of_data_points):
    '''Creates a data set from a model
    '''
    #Create five Variable objects
    height = cse.Variable('Height', 'numeric')
    weight = cse.Variable('Weight', 'numeric')
    gender = cse.Variable('Gender', 'categorical', [], ['Male','Female'])
    n_items = cse.Variable('# Items\nBought', 'numeric')
    money_spent = cse.Variable('$ spent', 'numeric')
    
    # Put them in a list
    variables = [height, weight, gender, n_items, money_spent]
                
    ###
    # Genders
    ###
    
    #model parameter sets percentage that are males
    p_male = 0.47 
    # Constant bool values coding for gender 
    MALE = 0 
    FEMALE = 1
    
    # Generate data from model
    for person in range(number_of_data_points):
        if random.uniform(0,1)<p_male:
            gender.data.append(MALE)
        else:
            gender.data.append(FEMALE)
    ###    
    # Heights
    ###
    # CDC. (2010). Body Measurements. Retrieved from 
    # http://www.cdc.gov/nchs/fastats/bodymeas.htm
    
    # model's parameters: 
    female_height_mean = 63.8
    female_height_sd = 2
    male_height_mean = 69.3
    male_height_sd = 2
    
    #generate data from model
    for person in range(number_of_data_points):
        my_gender = gender.data[person]
        if my_gender==FEMALE:
            my_height = female_height_sd * np.random.randn() + female_height_mean # female height
        else: #male
            my_height = male_height_sd * np.random.randn() + male_height_mean # male height
        
        # Round down to previous inch
        my_height = int(my_height)
        # Store the data in column 1
        height.data.append(my_height)
            
    ####
    # Weight
    ###
    # Engineering Toolbox (n.d.). HBody weight vs. height. Retrieved from
    # http://www.engineeringtoolbox.com/body-weight-versus-height-d_1551.html
    
    #model's parameters
    male_weight_69in_mean = 154
    male_weight_69in_sd = 17 #from (176-142)/2
    male_weight_per_in = 46/14. #from (187-141)/(6'4"-5'2")
    
    female_weight_64in_mean = 131 # (124+138)/2
    female_weight_64in_sd = 18 # (151-114)/2
    female_weight_per_in = 39/14. # ((148-109)/6'0"-4'10")
    
    # Generate data from model
    for person in range(number_of_data_points):
        my_height = height.data[person]
        my_gender = gender.data[person]
        if my_gender==FEMALE:
            my_weight = female_weight_64in_mean + female_weight_per_in*(my_height-64) + female_weight_64in_sd*np.random.randn()
        else: # male
            my_weight = male_weight_69in_mean + male_weight_per_in*(my_height-69) + male_weight_69in_sd*np.random.randn()
        
        # Round down to pounds
        my_weight = int(my_weight)
        # Store the data in column 1
        weight.data.append(my_weight)

    ###
    # Number of items purchased
    ###
    # https://econsultancy.com/blog/2982-top-10-tips-for-retailers-to-combat-the-economic-downturn
    
    # parameters
    
    p_0 = 0.10 # portion that buy nothing
    p_single = 0.25 # portion that come in looking for one item
    
    # remaining will buy many items
    buy_many_mean = 12
    buy_many_sd = 5
    
    # probability of adding one item
    p_suggestive_sale = 0.20
    
    # Generate data from model
    for person in range(number_of_data_points):
        #gender, height, and weight are not used in the algorithm here
        my_gender = gender.data[person]
        my_height = height.data[person]
        my_weight = weight.data[person]
        
        # Randomly decide if customer is buy-none, buy-one, buy-many
        type_of_customer = random.uniform(0,1)
        if type_of_customer < p_0:
            items_bought = 0
        elif type_of_customer < p_0+p_single:
            items_bought = 1
        else:
            # Use normal distribution
            items_bought = buy_many_mean + buy_many_sd*np.random.randn()
            # Don't let it be negative
            if items_bought < 0:
                items_bought = 0
        
        # Add the effect of suggestive sales, even for non-buyers
        if random.uniform(0,1) < p_suggestive_sale:
            items_bought += 1
    
        # Assign the data point
        n_items.data.append(int(items_bought))
        
    ###
    # Total $ spent
    ###
    
    # model's parameters
    mean_per_item = 12.05
    sd_per_item = 3.10
    
    # Generate simulated data
    for person in range(number_of_data_points):
        items_bought = n_items.data[person]
        #apply model's normal distribution
        cost_per_item = mean_per_item + sd_per_item*np.random.randn()
    
        # Force total sale to be non-negative
        if cost_per_item <0.05:
            cost_per_item = 0.05
        money_spent.data.append(items_bought * cost_per_item)
        
    return variables
