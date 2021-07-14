class Solution(object):
    def compress(self, word):
        count = 0
        comp = ""
        for i in range(len(word)):
            count += 1

            if len(word) == 1 or i+1 == len(word) or word[i] != word[i + 1]:

                comp = comp + word[i]
                comp += str(count) if count > 1 else ""
                count = 0

        for i, char in enumerate(comp):
            word[i] = char
        return len(comp)
