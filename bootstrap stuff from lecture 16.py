# bootstrap stuff

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
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

#%%
class BootCI:
    
    def __init__(self):
        self.stat = "mean"
        self.dat = None
        self.n_boot = 0
        self.boot_stat = None
        self.ci_level = .95
        self.sim_list = []
    
    def simulation(self):
        # for loop
        # adds sims to overall list 
        n = len(self.dat)
        for _ in range(self.n_boot):
    
            boot_sample = self.dat.sample(n, replace = True)

            if stat == "median":
                self.sim_list.append(float(boot_sample.median()))
                
            elif stat == "mean":
                self.sim_list.append(float(boot_sample.mean()))
                
            elif stat == "std dev": 
                self.sim_list.append(float(boot_sample.std()))
                
            else:
                raise TypeError("Wrong statistic name")
                
        
    def clear(self):
        #clear the sim list
        self.sim_list = []
    
    def set_data(self, dat):
        #set the data
        self.data = dat


test = BootCI()
test.dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
test.dat = test.dat["Combined Mileage (mpg)"]
test.n_boot = 10000
test.simulation()
print(test.sim_list)