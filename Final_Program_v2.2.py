from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
import random
from datetime import datetime as dt
import re


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
        self.anti_aliasing = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
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
        # print(self.points)
        return matrix

    def get_points(self):
        return self.points


class RandomShapeGenerator:

    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
        self.square_points = {*()}
        self.lines_length = []
        self.shape_angle_points = {*()}

    def draw_shape(self):
        square_matrix = np.full(self.matrix_size, 10) # creates a matrix with all values = 10

        # creates random points

        p1 = Point(random.randrange(2, 10), random.randrange(2, 10))
        p2 = Point(p1.x, random.randrange(2, 10))
        p3 = Point(random.randrange(2, 10), p1.y)
        p4 = Point(p3.x, p2.y)
        '''
        p1 = Point(random.randrange(2, 10), random.randrange(2, 10))
        p2 = Point(random.randrange(2, 10), random.randrange(2, 10))
        p3 = Point(random.randrange(2, 10), random.randrange(2, 10))
        p4 = Point(random.randrange(2, 10), random.randrange(2, 10))
        '''
        # adds the randomly generated points to a set for accessibility
        for i in [p1, p2, p3, p4]:
            self.shape_angle_points.add(i)

        # self.shape_angle_points |= {p1, p2, p3, p4}

        # generates line objects using  the generated random points
        l1 = LineInMatrix(p1, p2, self.matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
        l2 = LineInMatrix(p1, p3, self.matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
        l3 = LineInMatrix(p4, p2, self.matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
        l4 = LineInMatrix(p3, p4, self.matrix_size, anti_aliasing=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

        # adds lines attributes to lists for accessibility purposes

        self.lines_length.append(l1.length())
        self.lines_length.append(l2.length())
        self.lines_length.append(l3.length())
        self.lines_length.append(l4.length())

        # draws lines in matrix
        for i in [l1, l2, l3, l4]:
            try:
                if p1.position != p2.position:
                    i.draw_line()

            except ZeroDivisionError:
                pass

        # checks if points of lines are not overlapping

        for point_a in l1.get_points():
            self.square_points.add(point_a)
        for point_b in l2.get_points():
            if point_b not in self.square_points:
                self.square_points.add(point_b)
        for point_c in l3.get_points():
            if point_c not in self.square_points:
                self.square_points.add(point_c)
        for point_d in l4.get_points():
            if point_d not in self.square_points:
                self.square_points.add(point_d)

        for point in self.square_points:
            square_matrix[point] = 0

        print("the chosen random points are: ", p1.position, p2.position, p3.position, p4.position)
        return square_matrix

    def shape_label(self):

        if self.lines_length[0] == self.lines_length[1]:

            label = "SQUARE"
        else:
            label = "RECTANGLE"


        return label


class PDF16Shapes:
    counter = 0

    def __init__(self, num, plot, matrix_size, file_name=None):
        self.num = num
        self.plt = plot
        self.matrix_size = matrix_size
        self.fn = file_name

    def create_image(self):
        # plot with various axes scales
        self.plt.figure(figsize=(15, 10))

        self.num = 16  # number of subplots
        roww = int(sqrt(self.num))  # variable used to perfectly chop the plot into subplots

        for i in range(self.num):
            uf = RandomShapeGenerator(self.matrix_size)
            of = uf.draw_shape()
            self.plt.subplot(self.num // roww, roww, i+1)
            # 331
            # 332
            # plt.plot(of)
            self.plt.title(uf.shape_label())
            self.plt.imshow(of, cmap = "gray", vmin = 0, vmax = 10)  # working#
            self.plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35,
                                     wspace=0.45)
            self.plt.gray()
        self.counter += 1
        #self.plt.show()

        self.plt.savefig(fname=f"permutationNO{self.counter}_dateOfCreation_{str(dt.now()).replace('.','_').replace(':', '_').replace(' ', '@')}.PDF")


num_of_images = 1

for i in range(num_of_images):
    PDF16Shapes(5, plt, (15, 15)).create_image()



