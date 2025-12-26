class Alphabet:
    def __init__(self, char):
        self.char = char
    def display_char(self):
        print("Alphabet:", self.char)
class Vowel(Alphabet):   
    def __init__(self, char):
        super().__init__(char)
    def display_vowel(self):
        self.display_char()
        print("This is a vowel")
v1 = Vowel('A')
v1.display_vowel()
