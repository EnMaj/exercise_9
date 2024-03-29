class User:
    '''
    Class of user

    Attributes
    id: int
        unique user number
    nick_name: str
        user alias
    first_name: str
        user first name
    last_name: str
        user last name
    middle_name: str
        user middle name
    gender: str
        user gender

    Methods
    update()
        updates some parameters
    print_user()
        print user parameters
    '''
    def __init__(self, id, nick_name, first_name, last_name = None,
                 middle_name = None, gender = None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, nick_name = None, first_name = None, last_name = None,
               middle_name = None, gender = None):
        if nick_name!=None:
            self.nick_name = nick_name
        if first_name != None:
            self.first_name = first_name
        if last_name != None:
            self.last_name = last_name
        if middle_name != None:
            self.middle_name = middle_name
        if self.gender != None:
            self.gender = gender

    def print_user(self):
        print(f'{self.id}, {self.nick_name}, {self.first_name}, {self.last_name}'
                f', {self.middle_name}, {self.gender}')

a = User(11112, 'aaaaa', 'qqqqqq', 'rrrrr')
a.update(nick_name='iiiiiii')
a.print_user()

