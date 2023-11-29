class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word)
