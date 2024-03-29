class Game:
    '''
    Class of game

    Attributes
    dictionary: dict
        A dictionary with a key - the name of the team
        and a value - the number of points the team has

    Methods
    ball_thrown(self, command, points)
        Writes the team's points in the dictionary
    get_score()
        Gives back a tuple with a score
    get_winner():
        Writes the winner
    '''
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def ball_thrown(self, command, points):
        self.dictionary['command' + str(command)] += points

    def get_score(self):
        return tuple(self.dictionary.items())

    def get_winner(self):
        if self.dictionary['command1'] > self.dictionary['command2']:
            return 'command1'
        elif self.dictionary['command1'] < self.dictionary['command2']:
            return 'command2'
        return 'Ничья'


dictionary = {'command1': 0 , 'command2': 0}
a = Game(dictionary)
a.ball_thrown(1,2)
print(a.get_score())
print(a.get_winner())