class NotSleeping:
    '''
    Falling asleep class

    Attributes
    __sheep: int
        number of sheep

    Methods
    add_sheep()
        increases the number of sheep by 1
    lost()
        resets the number of sheep
    get_count_sheeps()
        get the number of sheep
    '''
    def __init__(self):
        self.__sheep = 0

    def add_sheep(self):
        self.__sheep += 1

    def lost(self):
        self.__sheep = 0

    def get_count_sheeps(self):
        return self.__sheep

a = NotSleeping()
a.add_sheep()
a.add_sheep()
a.lost()
print(a.get_count_sheeps())