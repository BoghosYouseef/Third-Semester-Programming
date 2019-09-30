from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.image as mpimg


"""
x1 = np.arange(0,10, 1) # creates [ 1  2  3  4  5  6  7  8 4]
print(x1)

x2 = np.arange(2000, 2020, 2) #creates [2000 2002 2004 2006 2008 2010 2012 2014 2016 2018]

print(x2)

A = np.vstack((x1,x2))

x3 = x2 - x1**2
print(x3)
A = np.vstack((x1))


print(A)
plt.plot(A)
plt.matshow(A, fignum=None)
plt.matshow(B, fignum=None)
"""
matplotlib.colors.Colormap("gray", N = 256)
plot =  plt.figure(figsize=(12, 6))
B = np.full((28,28), 0.46982734)

#plt.matshow(B, fignum=None)
plt.imshow(B)
plt.show()