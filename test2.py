from math import sqrt, floor as down, ceil as up
import numpy as np
import matplotlib.pyplot as plt
import random

class Point:
    '''
    Class that defines 2d points with x and y as coordinates with a tuple property (x,y)

    :param x: value of point on x-axis
    :type x: float
    :param y: value of point on y-axis
    :type x: float

    '''

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.position = (x, y)


class LineObject(Point):

    '''

    defines a line as a two Point object with calculated attribute called length

    :param start_point: The point at which the line starts
    :type start_point: Point object
    :param end_point: The point at which the line ends
    :type end_point: Point object

    '''

    def __init__(self, start_point: Point, end_point: Point):
        Point.__init__(self, self.x, self.y)
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        diff_x_squared = (self.end_point.x - self.start_point.x) ** 2
        diff_y_squared = (self.end_point.y - self.start_point.y) ** 2

        return sqrt(diff_x_squared + diff_y_squared)

    def line_end_points(self):
        print("the line connects the following points: ", "(", self.start_point.x, ",", self.start_point.y,
              ")", "," "(", self.end_point.x, ",",
              self.end_point.y, ")")



def distance_point(p1, p2, p3):
    top = abs(((p1[1] - p2[1]) * p3[0]) - ((p1[0] - p2[0]) * p3[1]) + (p1[0] * p2[1]) - (p1[1] * p2[0]))
    return top / sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


class LineInMatrix(LineObject):

    def __init__(self, start_point, end_point, matrix_size, anti_aliasing):
        self.start_point = start_point
        self.end_point = end_point
        self.matrix_size = matrix_size
        self.anti_aliasing = anti_aliasing= [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
        self.points = {*()}


    def draw_line(self):
        matrix = np.full(self.matrix_size, 10)
        for pointX in range(min(self.end_point.x, self.start_point.x), max(self.end_point.x, self.start_point.x) + 1):
            for pointY in range(min(self.end_point.y, self.start_point.y), max(self.end_point.y, self.start_point.y) + 1):
                middle = Point(pointX, pointY)
                for i in range(10):
                    if distance_point(self.start_point.position, self.end_point.position, middle.position) <= self.anti_aliasing[i]:
                        if middle.position not in self.points:
                            self.points.add(middle.position)
                            matrix[middle.position] = i
                continue
        #print(self.points)
        return matrix

    def get_points(self):
        return self.points

matrix_size = (50, 50)


# error_margin = 2

p1 = Point(random.randrange(5,30),random.randrange(5, 30))
p2 = Point(p1.x, random.randrange(5, 30))
p3 = Point(random.randrange(5,30), p1.y)

#if distance_point(p1.position, p2.position, p3.position):
 #   p4 = Point(p2.x, p3.y)
 #   l1 = LineInMatrix(p1, p2, matrix_size, anti_aliasing= [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
 #   l2 = LineInMatrix(p1, p3, matrix_size, anti_aliasing= [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
 #   l3 = LineInMatrix(p3, p2, matrix_size, anti_aliasing= [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
 #   l4 = LineInMatrix(p3, p4, matrix_size, anti_aliasing= [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
 #   while (max(l1.length(),l3.length()) - min(l1.length(), l3.length())) <= error_margin:
#
#        if (max(l2.length(), l4.length()) - min(l2.length(), l4.length())) <= error_margin:
#            l1.draw_line()
#            l2.draw_line()
 #           l3.draw_line()
 #           l4.draw_line()

p5 = Point(10, 10)
p6 = Point(40, 10)
p7 = Point(10, 40)
p8 = Point(40, 40)

l5 = LineInMatrix(p5, p6, matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
l6 = LineInMatrix(p5, p7, matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
l7 = LineInMatrix(p6, p8, matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
l8 = LineInMatrix(p7, p8, matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

l5.draw_line()
l6.draw_line()
l7.draw_line()
l8.draw_line()

print(l5.get_points())
print(l6.get_points())
print(l7.get_points())
print(l8.get_points())

"""
try:
    print("length of line1 = {}".format(l1.length()))
    print("length of line2 = {}".format(l2.length()))
    print("length of line3 = {}".format(l3.length()))
    print("length of line4 = {}".format(l4.length()))
except:
    print("division by zero")
"""


square_points = {*()}

square_matrix = np.full(matrix_size, 10)

for point in l5.get_points():

    square_points.add(point)

for point_b in l6.get_points():
    if point_b not in square_points:
        square_points.add(point_b)
for point_c in l7.get_points():
    if point_c not in square_points:
        square_points.add(point_c)
for point_d in l8.get_points():
    if point_d not in square_points:
        square_points.add(point_d)

for point in square_points:
    square_matrix[point] = 0


fig = plt.figure(figsize=(10, 7))

plt.imshow(square_matrix, cmap="gray", vmin=0, vmax=10) # working#
plt.axis(xmin=0, xmax=matrix_size[0], ymin=0, ymax=matrix_size[1])
plt.show()
