from random import randint

class PasswordGenerator:

    def __init__(self, nounlist=[], adjlist=[], difficulty=5):
        self.difficulty = difficulty

        self.nounlist = [x for x in nounlist if len(x) <= difficulty]
        self.adjlist = [x for x in adjlist if len(x) <= difficulty]

        if not self.nounlist:
            print("No noun list received or is empty")

        if not self.adjlist:
            print("No adjective list received or is empty")
    
    def __str__(self):
        return ("Password generator object - %i nouns and %i adjectives with a difficulty of %i" % (len(self.nounlist), len(self.adjlist), self.difficulty))

    def __len__(self):
        return (self.difficulty * 2) + 2

    def randListItem(self, l):
        return l[randint(0, len(l)-1)]

    def generateBasicPassword(self):
        return self.randListItem(self.adjlist) + self.randListItem(self.nounlist) + str(randint(10, 99))