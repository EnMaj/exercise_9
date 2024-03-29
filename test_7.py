class TrafficLight:
    '''
    Class of TrafficLight

    Attributes
    __current_signal: str
        current traffic light signal
    __permissible_values: list
        all possible traffic lights
    __chain: list
        how the traffic lights lit up one after another,
        a complete chain
    __index_signal: int
        current signal index
    __previous: str
        previous traffic light

    Methods
    next_signal_1()
        writes the next traffic light
    next_signal_2()
        writes the next traffic light
    '''
    def __init__(self):
        self.__current_signal = 'зеленый'
        self.__permissible_values = ['зеленый','желтый','красный']

        self.__chain = ['зеленый', 'желтый', 'красный','желтый']
        self.__index_signal = 0

        self.__previous = 'желтый'

    def next_signal_1(self):
        if self.__index_signal < 3:
            self.__index_signal += 1
            self.__current_signal = self.__chain[self.__index_signal]
        else:
            self.__index_signal = 0
            self.__current_signal = 'зеленый'

    def next_signal_2(self):
        if self.__current_signal == 'зеленый':
            self.__current_signal = 'желтый'
        elif self.__current_signal == 'красный':
            self.__current_signal = 'желтый'
        else:
            if self.__previous == 'зеленый':
                self.__current_signal = 'красный'
            elif self.__previous == 'красный':
                self.__current_signal = 'зеленый'