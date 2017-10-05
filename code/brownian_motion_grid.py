import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

def brownian_model_plot(length):
    # Length of array (or how long motion is modeled)
    X = np.zeros((length,2))
    
    for i in range(0,len(X) - 1):
        for ii in range(0,len(X[i])):
            direction = random.choice([1,0,-1,-2,2])
            X[i + 1][ii] = X[i][ii] + direction
            
    x = X[:,0]
    y = X[:,1]
    
    return x,y
    
    
#pylab.rcParams['figure.figsize'] = (60, 60)
#plt.figure(figsize=(10,10))
#plt.plot(x[:,0],x[:,1])
#plt.axis('equal')
#plt.savefig('Brownian_Model.png', dpi=300)
#plt.show()


fig, ax = plt.subplots(nrows=5, ncols=5, figsize=(10,10))
for row in ax:
    for col in row:
        x,y = brownian_model_plot(1000)
        col.plot(x,y)
        col.axis('equal')

plt.suptitle('5x5 Grid of Multiple Brownian Walks', fontsize=20)
plt.savefig('Brownian_Model_grid.png', dpi=100)
plt.show()