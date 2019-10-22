from Prisoner import Prisoner
import random

class BahHumbug(Prisoner):

    def __init__(self):
        self.N = self.C = self.D = self.ci = self.di = 0
        self.other_strategy = True
    
    """

    """
    def pick_strategy(self):
        # N is the total number of rounds we have done so far
        # C is the total number of times I have cooperated
        # D is the total number of times I have defected
        # ci is the number of times in a row I have cooperated
        # di is the number of times in a row I have defected
        
        #if self.ci > 5: # magic c number = 5
         #   return False # defect
        if self.di > 5:
            return True
        else:
            r = random.randint(0,3) # generate random number
            if r == 0:
                return self.other_strategy
            else:
                return False
        # else
            # do what the other person did 50% of the time:
            # return self.last_strategy
            # cooperate the other 50% of the time:
            # cooperate
    
    """
    This Prisoner also has to remember their opponent's last strategy
    """
    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:
            self.C += 1
            self.ci += 1
            self.di = 0
        elif my_strategy == False:
            self.D += 1
            self.di += 1
            self.ci = 0
        self.other_strategy = other_strategy



