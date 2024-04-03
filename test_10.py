class Point:
    '''
    Class of point

    Attributes
    __cortege: tuple
        point coordinates

    Methods
    get_x()
        get x in __cortege
    get_y()
        get y in __cortege
    distance(self,other)
        distance between points self and other
    sum(self,other)
        returns a new point.
        the coordinates of this point are
        the sum of the coordinates self and other
    '''
    def __init__(self, cortege = (0,0)):
        self.__cortege = cortege

    def get_x(self):
        return self.__cortege[0]

    def get_y(self):
        return self.__cortege[1]

    def distance(self,other):
        return abs((other[0] - self.__cortege[0])**2 + (other[1] - self.__cortege[1])**2)**0.5

    def sum(self,other):
        new_point = Point((self.__cortege[0] + other[0], self.__cortege[1] + other[1]))
        return new_point

class Segment:
    '''

    '''

    def __init__(self, point1_x, point1_y, point2_x, point2_y):
        self.point1 = Point((point1_x, point1_y))
        self.point2 = Point((point2_x, point2_y))
        self.__one_intersection = False

    def get_point1(self):
        return self.point1

    def get_point2(self):
        return self.point2

    def set_one_intersection(self, is_intersect = True):
        self.__one_intersection = is_intersect

    def get_one_intersection(self):
        return self.__one_intersection

class CoordinateSystem:
    '''

    '''

    def __init__(self):
        self.__segments = []


    def add_segment(self,segment):
        self.__segments.append(segment)

    def get_segments(self):
        return self.__segments

    def axis_intersection(self):
        number_true = 0
        for i in range(len(self.__segments)):
            multiply = (self.__segments[i].get_point1().get_x()
                        * self.__segments[i].get_point1().get_y()
                        * self.__segments[i].get_point2().get_x()
                        * self.__segments[i].get_point2().get_y())

            if multiply < 0:
                self.__segments[i].set_one_intersection(True)
                number_true += 1
            elif multiply == 0:
                multiply_point1 = (self.__segments[i].get_point1().get_x()
                            * self.__segments[i].get_point1().get_y())
                multiply_point2 = (self.__segments[i].get_point2().get_x()
                            * self.__segments[i].get_point2().get_y())
                if multiply_point1 != multiply_point2:
                    self.__segments[i].set_one_intersection(True)
                    number_true += 1
        return number_true

a = Segment(0,2,0,-4)
print((a.point1).get_y())
b = CoordinateSystem()
b.add_segment(a)
print(b.get_segments()[0].get_point1().get_y())
print(b.axis_intersection())
