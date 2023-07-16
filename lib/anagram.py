class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, list_of_words):
        matches = []
        for word in list_of_words:
            word.lower()
            if sorted(word) == sorted(self.word) and self.word != word:
                matches.append(word)
        return matches
