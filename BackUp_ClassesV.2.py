from math import sqrt, floor as down, ceil as up
import numpy as np
import matplotlib.pyplot as plt


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


class Line:


    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        x_distance = (self.p2.x - self.p1.x) ** 2
        y_distance = (self.p2.y - self.p1.y) ** 2

        return sqrt(x_distance + y_distance)

    def points(self):
        print("the line connects the following points: ", "(", self.p1.x, ",", self.p1.y, ")", "," "(", self.p2.x, ",",
              self.p2.y, ")")


t1 = Point(2, 1)
t2 = Point(1, 5)
t3 = Point(-3, 9)
t4 = Point(-2, 3)

# print(t1.position, "---", t2.position, "---", t3.position, "---", t4.position)

#l1 = Line(t1, t2)
#l2 = Line(t1, t3)
#l3 = Line(t1, t4)
#l4 = Line(t2, t3)


# print(l1.length(),l1.points() , l2.length(), l2.points(), l3.length(), l3.points(), l4.length(), l4.points())


class Shapes:

    def __init__(self, square, triangle, rectangle):
        self.square = square
        self.triangle = triangle
        self.rectangle = rectangle

def square(p1: Point, p2: Point, p3: Point, p4: Point):

    middle_point12 = ((p1.x + p2.x)/2, (p1.y +p2.y)/2)
    middle_point13 = ((p1.x + p3.x)/2, (p1.y +p3.y)/2)
    #middle_point14 = ((p1.x + p4.x)/2, (p1.y +p4.y)/)
    #middle_point23 = ((p2.x + p3.x)/2, (p2.y +p3.y)/)
    middle_point24 = ((p2.x + p4.x)/2, (p2.y +p4.y)/2)
    middle_point34 = ((p3.x + p4.x)/2, (p3.y +p4.y)/2)

    if distance_point(p1,p2, middle_point12) < 1 and distance_point(p1,p3, middle_point13) < 1 and \
            distance_point(p2,p4, middle_point24) < 1 and distance_point(p3,p4, middle_point34):
        first_line = line_in_matrix(p1, p2, (200,200))
        second_line = line_in_matrix(p1, p3, (200,200))
        third_line = line_in_matrix(p2, p4, (200,200))
        fourth_line = line_in_matrix(p3, p4, (200,200))

        square = np.add(first_line, second_line, third_line, fourth_line)
        return square




#############################
def is_point_on_line(p0, p1):
    if p0[0] == p1[0]:
        return None
    m = (p0[1] - p1[1]) / (p0[0] - p1[0])
    b = p0[1] - p0[0] * m
    return lambda x: m * x + b
#############################

#def distance_of_point_from_line(p1, p2, p3):
    #pass


def distance_point(p1, p2, p3):
    top = abs(((p1[1] - p2[1]) * p3[0]) - ((p1[0] - p2[0]) * p3[1]) + (p1[0] * p2[1]) - (p1[1] * p2[0]))
    return top / sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


##################
def choosing_pixels(x, y):
    x_diff_up = up(x) - x
    x_diff_down = x - down(x)
    y_diff_up = up(y) - y
    y_diff_down = y - down(y)
    if x_diff_up > x_diff_down:
        x = down(x)
    elif x_diff_up < x_diff_down:
        x = x_diff_up
    if y_diff_up > y_diff_down:
        y = down(y)
    elif y_diff_up < y_diff_down:
        y = y_diff_up


##################
# https://stackoverflow.com/questions/46081491/how-to-generate-squares-randomly-located-equally-sized-randomly-rotated-that


h1 = Point(0, 5)
h2 = Point(5, 5)
h3 = Point(1, 1)
h4 = Point(0, 0)

point1 = Point(0, 0)
point2 = Point(0, 1800)
point3 = Point(5000, 0)
point4 = Point(2500, 5000)
point5 = Point(900, 9)
point6 = Point(3975, 775)
point7 = Point(3651, 1712)
point8 = Point(1025, 3831)
point9 = Point(4611, 1328)


class LineObject:

    '''

    defines a line as a two Point object with calculated attribute called length

    :param start_point: The point at which the line starts
    :type start_point: Point object
    :param end_point: The point at which the line ends
    :type end_point: Point object

    '''

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        diff_x_squared = (self.end_point.x - self.start_point.x) ** 2
        diff_y_squared = (self.end_point.y - self.start_point.y) ** 2

        return sqrt(diff_x_squared + diff_y_squared)

    def points(self):
        print("the line connects the following points: ", "(", self.start_point.x, ",", self.start_point.y,
              ")", "," "(", self.end_point.x, ",",
              self.end_point.y, ")")



def line_in_matrix(start_point, end_point, matrix_size: tuple, anti_aliasing=(0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)):
    matrix = np.full(matrix_size, 10)

    for pointX in range(min(end_point.x, start_point.x), max(end_point.x, start_point.x) + 1):
        for pointY in range(min(end_point.y, start_point.y), max(end_point.y, start_point.y) + 1):
            middle = Point(pointX, pointY)
            if distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[0]:
                matrix[(pointX, pointY)] = 0
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[1]:
                matrix[(pointX, pointY)] = 1
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[2]:
                matrix[(pointX, pointY)] = 2
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[3]:
                matrix[(pointX, pointY)] = 3
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[4]:
                matrix[(pointX, pointY)] = 4
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[5]:
                matrix[(pointX, pointY)] = 5
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[6]:
                matrix[(pointX, pointY)] = 6
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[7]:
                matrix[(pointX, pointY)] = 7
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[8]:
                matrix[(pointX, pointY)] = 8
            elif distance_point(start_point.position, end_point.position, middle.position) <= anti_aliasing[9]:
                matrix[(pointX, pointY)] = 9

    return matrix


matrix2 = np.full((20, 20), 4)
l1 = line_in_matrix(Point(100, 100), Point(750,250), (1000, 1000))
l2 = line_in_matrix(Point(100, 100), Point(200,750), (1000, 1000))
l3 = line_in_matrix(Point(100, 750), Point(700,700), (1000, 1000))
l4 = line_in_matrix(Point(750, 100), Point(720,700), (1000, 1000))

matrix_square_angle1 = np.add(l1, l2)
matrix_square_angle2 = np.add(l3, l4)
matrix_square = np.add(matrix_square_angle1, matrix_square_angle2)


fig = plt.figure(figsize=(10, 7))

plt.imshow(l1, cmap="gray", vmin=0, vmax=10)
# plt.imshow(matrix2, cmap="gray", vmin=0, vmax= 10)
plt.axis(xmin=0, xmax=1000, ymin=0, ymax=1000)
plt.show()
print(l1)