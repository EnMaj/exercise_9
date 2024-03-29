class NotSleeping:
    '''
    Falling asleep class

    Attributes
    __sheep: int
        number of sheep

    Methods
    add_sheep()
        increases the number of sheep by 1
    sheep()
        get the number of sheep
    '''
    def __init__(self):
        self.__sheep = 0

    def add_sheep(self):
        self.__sheep += 1

    @property
    def sheep(self):
        return self.__sheep

a = NotSleeping()
a.add_sheep()
a.add_sheep()
print(a.sheep)
