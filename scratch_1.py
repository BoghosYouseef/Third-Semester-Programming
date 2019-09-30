import numpy as np
import pandas as pd

A = np.full((4,3), 1)
B = np.eye(3, 4)
print(A)
print(B)

C = np.arange(10, 0, -1)
print(C)

D = pd.Series(C)
print(D)
print("________________")
G = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(G[0,0])
print(G[0,1])
print(G[0,2])
print(G[0,3])
print(G[1,0])
print(G[1,1])
print(G[1,2])
print(G[1,3])
print(G[2,0])
print(G[2,1])
print(G[2,2])
print(G[2,3])
G[2,3] = 0
G[1,2] = 0
G[0,0] = 0
G[1,1] = 0
print(G)

print(G.shape)
print(np.arange(3, 10, 1))

E = np.array([[3, 5, 3, 3],
              [0, 1, 2, 7],
              [9, 1, 4, 2],
              [0, 1, 2, 7]])

print("___________")
F = np.dot(G, E, out=None)
print(F)
print("_________________________________")

v = np.array([1,0])
u = np.array([0,1])

UV = np.vstack((v, u))
print(UV)

