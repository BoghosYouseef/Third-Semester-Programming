import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import image as img



A = np.full((28,28), 10)
B = np.eye(28,28)
print(A)
print("_________________________")
print(B)
#print(A)

def line_in_matrix(Y, x):
    for i in np.nditer(Y[...][14], op_flags=['readwrite']):
        i[...] = x
        print(A)

line_in_matrix(A, 5)
#rotational_matrix_90_right = np.full((15,15), math.cos(90))
# print(rotational_matrix_90_right)




plot =  plt.figure(figsize=(9, 9))

ax = plt.axes()

plt.matshow(A, fignum=0)
#plt.imshow(A)

#plt.subplot(A[4])
plot.add_axes([1,1,28,28])
plt.gray()
ax.xaxis.set_label_position('top')
ax.xaxis.tick_bottom()
ax.invert_yaxis()


plt.show()
#print(D.shape)
plt.imsave("horizontal_line.pdf", A)