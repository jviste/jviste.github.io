'''
The __init__.py file makes this folder into a package, so that other files 
in this folder can be referred to as cse.module
'''
import viz
import stats
import montecarlo

# Make all these imports fresh in case you changed code in any of them
reload(viz)
reload(stats)
reload(montecarlo)

class Variable(object):
    ''' Defines objects that store data and metadata
    '''
    def __init__(self, mylabel, mytype='numeric', mydata=[], mytreatments=None):
        '''Create a new Variable
        mylabel is a string for labelling axes
        data is a list of data values
        mytype'''
        self.label = mylabel
        self.data = mydata[:] # Copies what was provided
        self.type = mytype # must be 'numeric' or 'categorical'; if latter, use values 0 and 1
        self.treatments = mytreatments # [Fstring, Tstring] for type bool