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

a = Point((-1,7))
print(a.get_x())
print(a.get_y())
print(a.distance((7,1)))
print(a.sum((7,1)))