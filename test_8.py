class MorseMsg:
    '''
    Class of Morze

    Attributes
    __morse_list: list
         array of all letters in Morse language

    Methods
    eng_decode()
        returns the decrypted message in Latin letters
    ru_decode()
        returns the decrypted message in Cyrillic letters
    get_vowels(self, lang)
        returns a list of vowels in lang, in the order they appear
        in the message (lang is line 'ru' or 'eng')
    get_consonants(self, lang)
        returns the consonants in lang, in the order
        they appear in the message.
    '''

    def __init__(self, morse_str):
        self.__morse_list = list(map(str, morse_str.split(' ')))

    def eng_decode(self):
        morze = {'•—': 'A', '—•••': 'B', '—•—•': 'C', '—••': 'D',
                 '.': 'E', '••—•': 'F', '——•': 'G', '••••': 'H',
                 '••': 'I', '•———': 'J', '—•—': 'K', '•—••': 'L',
                 '——': 'M', '—•': 'N', '———': 'O', '•——•': 'P',
                 '——•—': 'Q', '•—•': 'R', '•••': 'S', '-': 'T',
                 '••—': 'U', '•••—': 'V', '•——': 'W', '—••—': 'X',
                 '—•——': 'Y', '——••': 'Z', 7 * '.': ' '}
        decode_str = ''
        for i in self.__morse_list:
            decode_str += morze[i]
        return decode_str

    def ru_decode(self):
        morze = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
                 '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
                 '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
                 '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
                 '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
                 '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э',
                 '..--': 'Ю', '.-.-': 'Я', 7 * '.': ' '}
        decode_str = ''
        for i in self.__morse_list:
            decode_str += morze[i]
        return decode_str

    def get_vowels(self, lang):
        if lang == 'ru':
            return list(filter(lambda x: x in 'УЕЫАОЭЯИЮ', self.ru_decode()))
        elif lang == 'eng':
            return list(filter(lambda x: x in 'EYUIOA', self.eng_decode()))

    def get_consonants(self, lang):
        if lang == 'ru':
            return list(filter(lambda x: x in 'ЦКНГШЩЗХЪФВПРЛДЖЧСМТБЬ', self.ru_decode()))
        elif lang == 'eng':
            return list(filter(lambda x: x in 'QWRTPSDFGHJKLZXCVBNM', self.eng_decode()))

a = MorseMsg('.- .-.-')
print(a.ru_decode())
print(a.get_vowels('ru'))
