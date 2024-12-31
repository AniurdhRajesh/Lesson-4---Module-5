class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

obj = StringReverser("Hello World from Anirudh")
print(obj.reverse_words())
