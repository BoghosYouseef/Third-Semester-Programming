from math import sqrt
import numpy as np
import matplotlib.pyplot as plt



class Point:

    '''
    Class that defines 2d points with x and y as coordinates
    '''

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.position = tuple((x, y))



class Line():
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

    def points(self):
        print("the line connects the following points: ", "(" ,self.p1.x ,",", self.p1.y ,")","," "(",self.p2.x ,",", self.p2.y ,")")


t1 = Point(2,1)
t2 = Point(1, 5)
t3 = Point(-3, 9)
t4 = Point(-2, 3)

#print(t1.position, "---", t2.position, "---", t3.position, "---", t4.position)

l1 = Line(t1, t2)
l2 = Line(t1, t3)
l3 = Line(t1, t4)
l4 = Line(t2, t3)


#print(l1.length(),l1.points() , l2.length(), l2.points(), l3.length(), l3.points(), l4.length(), l4.points())






class Shapes:

    def __init__(self, square, triangle, rectangle):

        self.square = square
        self.triangle = triangle
        self.rectangle = rectangle


def get_func_deg1(p0, p1):
    p0 = Point(p0.x, p0.y)
    p1 = Point(p1.x, p1.y)
    if p0.x == p1.x:
        return None
    a = (p0.y - p1.y)/(p0.x - p1.x)
    b = p0.y - p0.x * a
    return lambda x: a * x + b
# https://stackoverflow.com/questions/46081491/how-to-generate-squares-randomly-located-equally-sized-randomly-rotated-that


h1 = Point(0, 5)
h2 = Point(0, 0)
h3 = Point(5, 5)
h4 = Point(0,0)

if get_func_deg1(h1, h2):
    print("not on the same line")
else:
    print("are on the same line")

if get_func_deg1(h1, h3):
    print("not on the same line")
else:
    print("are on the same line")

if get_func_deg1(h1, h4):
    print("not on the same line")
else:
    print("are on the same line")

if get_func_deg1(h2, h3):
    print("not on the same line")
else:
    print("are on the same line")

if get_func_deg1(h2, h4):
    print("not on the same line")
else:
    print("are on the same line")

if get_func_deg1(h3, h4):
    print("not on the same line")
else:
    print("are on the same line")

if get_func_deg1(h4, h4):
    print("not on the same line")
else:
    print("are on the same line")