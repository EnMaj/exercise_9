class StrandsDNA:
    '''
    class of strands DNA

    Attributes
    __all_strands: list
        dna strand list

    Methods
    add_strands(self, strands)
        you can add chains that are written in a line strands
    get_max_strands(self)
        you can get a string containing chains of maximum length
    '''

    def __init__(self):
        self.__all_strands = []

    def add_strands(self, strands):
        strands_list = map(str, strands.split(' '))
        self.__all_strands += strands_list
        self.__all_strands = sorted(list(set(self.__all_strands)))

    def get_max_strands(self):
        len_max = len(max(self.__all_strands))
        str_max_strands = []
        for i in self.__all_strands:
            if len(i) == len_max:
                str_max_strands.append(i)
        return ' '.join(str_max_strands)


a = StrandsDNA()
a.add_strands('qqq aaaa ee ee ttttt aaaaa')
print(a.get_max_strands())
