# bootstrap stuff

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import numpy as np
import os

# os.chdir("C:\\Users\\Owner\\OneDrive - Baylor University\\School\\Senior Fall Semester\\Statistics\\Spyder things")
# dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

# for me Brennan Chan (Carson comment me out)
os.chdir("C:/Users/Hi_I_/Downloads")
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")



dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot  = 10000

stat = "mean"

boot_stat = []

# method that does that within the class
for i in range(n_boot):
    
    boot_sample = dat.sample(n, replace = True)

    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
        
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
        
    elif stat == "std dev": 
        boot_stat.append(float(boot_sample.std()))
        
    else:
        raise TypeError("Wrong statistic name")
        
        

boot_df = pd.DataFrame({'x': boot_stat})


(
    ggplot(boot_df, aes( x = "x"))+
    geom_histogram()+
    theme_classic()
)

class BootCI:
    
    def __init__(self):
        """
        The above code defines a class with methods for performing bootstrapping simulations and setting
        parameters for the simulations.
        """
        
        self.stat = "mean"
        self.dat = "2017_Fuel_Economy_Data.csv"
        self.n_boot = 0
        self.boot_stat = None
        self.ci_level = .95
        self.sim_list = []
    
    def simulation(self):
        """for loop adds sims to overall list """
        n = len(self.dat)
        for _ in range(self.n_boot):
    
            boot_sample = self.dat.sample(n, replace = True)

            if self.stat == "median":
                self.sim_list.append(float(boot_sample.median()))
                
            elif self.stat == "mean":
                self.sim_list.append(float(boot_sample.mean()))
                
            elif self.stat == "std dev": 
                self.sim_list.append(float(boot_sample.std()))
                
            else:
                raise TypeError("Wrong statistic name")
                
        
    def clear(self):
        """clear the sim list"""
        self.sim_list = []
    
    def set_data(self, dat):
        """clear the sim list"""
        #set the data
        self.data = dat
    
    def set_n_boot(self, n_boot):
        """
        The function sets the value of the variable "n_boot" in the class.
        
        Prams: 
            n_boot: The parameter "n_boot" represents the number of bootstrap iterations to perform
        """
        self.n_boot = n_boot
    
    def set_stat(self, stat):
        """
        The function sets the value of the "stat" attribute and clears the "sim_list" attribute.
        
        Params:
            stat: The `stat` parameter is the value that you want to set for the `stat` attribute of
            the object
        """
        self.stat = stat
        self.sim_list = []
    
    def set_conf(self, ci):
        """
        The function sets the confidence interval level.
        
        Prams:
            ci: The parameter "ci" represents the confidence interval level. It is used to set the
            confidence interval for a particular calculation or analysis
        """
        #sets the conf interval
        self.ci_level = ci
    
    def give_conf(self):
        """
        The function "give_conf" returns the confidence interval of a given list of values.
        
        Return: 
            a tuple containing the lower and upper bounds of the confidence interval.
        """
        # give conf interval 
        lb = (1 - self.ci_level) / 2
        ub = 1 - lb
        
        return (np.percentile(self.sim_list, [lb, ub]))
    
    def plot_dis(self):
        """
        The function `plot_dis` creates a histogram plot using the values in the `sim_list` attribute of
        the object.
        
        Returns:
            a histogram plot of the data stored in the "sim_list" attribute of the object.
        """
        # plots 
        boot_plot = pd.DataFrame({'x': self.sim_list})
        
        return(
            ggplot(boot_plot, aes( x = "x"))+
            geom_histogram()+
            theme_classic()
        )


test = BootCI()
test.dat = test.dat["Combined Mileage (mpg)"]
test.n_boot = 10000
test.simulation()
print(test.sim_list)
test.plot_dis()
test.give_conf()