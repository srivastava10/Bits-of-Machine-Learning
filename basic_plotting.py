#In this tutorial we can see the basic usage of plotting using matplotlib.pyplot

import matplotlib.pyplot as plt 
import numpy as np
#Creating two vectors x and y for plotting them against each other

x = np.array([1,2,3,4,5,6,7,8,9,10])
#or u can also say 
# a = np.array(list(range(1,11)))

y = 2*x

plt.plot(x,y)
plt.plot(x,y,'ro')
plt.show()



# How to make a bar plot
fruits = ['apples','bananas','oranges']
number = [10,23,50]
plt.bar(fruits,number)