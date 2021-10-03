import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#            start,stop,step
x = np.arange(0.0,10.0,0.01)   # similar to range function in python. nparange deals with decimals unlike range function in python
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0,len(x))  # random numbers. Centre, std dev, size


plt.plot(x, y + noise, 'r.', label = "Actual")
plt.plot(x,y, 'b-', label = "Model")   # this runs two plots on same axes

plt.title("Simple Plot")
plt.xlabel("Weight")
plt.ylabel("Mass")
plt.legend() # add this if you've a few plots. Essential to add labels above too

plt.show()

