from math import sqrt
import numpy as np
import matplotlib.pyplot as plt



class Point:

    '''
    Class that defines 2d points with x and y as coordinates
    '''

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.position = tuple((x, y))



class Line:
    '''
defines a line as a two Point object with calculated attribute called length
    '''

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def length(self):

        x_distance = (self.p2.x - self.p1.x)**2
        y_distance = (self.p2.y - self.p1.y)**2

        return sqrt(x_distance + y_distance)


t1 = Point(2,1)
t2 = Point(1, 5)
t3 = Point(-3, 9)
t4 = Point(-2, 3)

# print(t1.position, "//", t2.position, "//", t3.position, "//", t4.position)

l1 = Line(t1, t2)
l2 = Line(t1, t3)
l3 = Line(t1, t4)
l4 = Line(t2, t3)

# print(l1.length(), l2.length(), l3.length(), l4.length())


class Grid():
    def __init__(self, x_axis, y_axis):
        self.x_axis = Line(Point(-10,0), Point(10, 0))
        self.y_axis = Line(Point(0, -10), Point(0, 10))


def matrix_points(A):
    for i in A[0][range(0,-1)]:
        i = Point(A[0], A[i])
        return print(i)


A = np.eye(28,28)
B = np.full((28,28), 0)
C = np.arange(0, 28, 1)
C1 = np.vstack(np.arange(0,1,0.1))
plot = plt.plot(figsize=(30,30))
plt.gray()
plt.imshow(A)
plt.matshow(C1, fignum= 2)
#plt.subplot(C1, [0, 1, 0.1, 10])


plt.show()
