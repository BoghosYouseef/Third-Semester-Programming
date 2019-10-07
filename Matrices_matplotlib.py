import pandas as pd  #imports Python module Pandas
import numpy as np   #imports Python module Pandas
import math
from matplotlib import colors
from matplotlib import pyplot as plt
from matplotlib import image as img

A = np.full((28,28), 255)  #Creates a matrix with dimensions 28x28 which only has the value 10
B = np.eye(28,28)
#print(A)
print("_________________________")
#print(B)


def line_in_matrix(matrix, polarisation:str, position:float, value, print_out=False ):
    if polarisation == "h":
        for i in np.nditer(matrix[position], op_flags=['readwrite']):
            i[...] = value

    elif polarisation == "v":
        for i in np.nditer(matrix[:, position], op_flags=['readwrite']):
            i[...] = value
    if print_out == True:
        print(matrix)

line_in_matrix(A,"h", 15, 0,True)
line_in_matrix(A,"h",14, 100)
line_in_matrix(A,"h",16, 100)
line_in_matrix(A,"h",13, 150)       #horizontal grey scale
line_in_matrix(A,"h",17, 150)
line_in_matrix(A,"h",18, 200)
line_in_matrix(A,"h",12, 200)


line_in_matrix(A,"v", 14, 0, True)
line_in_matrix(A,"v",15, 100)
line_in_matrix(A,"v",13, 100)
line_in_matrix(A,"v",16, 150)       #vertical grey scale
line_in_matrix(A,"v",12, 150)
line_in_matrix(A,"v",17, 200)
line_in_matrix(A,"v",11, 200)
plot =  plt.figure(figsize=(8, 6))

ax = plt.axes()
#plt.matshow(A, fignum=0)
plt.imshow(A, cmap='gray', vmin=0, vmax=255)

plot.add_axes([1,1,28,28])
ax.xaxis.set_label_position('top')
ax.xaxis.tick_bottom()
ax.invert_yaxis()

plt.show()

#plt.imsave("horizontal_line.pdf", A) #saves the figure in PDF format