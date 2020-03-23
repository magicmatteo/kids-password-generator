from random import randint

nounlist = ['ant', 'ape', 'bass', 'bat', 'bear', 'bee', 'bilby', 'bird', 'bison', 'bug', 'bull', 
'camel', 'cat', 'cobra', 'cod', 'cow', 'crab', 'crow', 'deer', 'dingo', 'dodo', 'dog', 
'dove', 'duck', 'eagle', 'eel', 'egg', 'emu', 'fish', 'flea', 'fly', 'fox', 'frog', 
'gecko', 'goat', 'goose', 'grub', 'hawk', 'hen', 'hippo', 'horse', 'hound', 'koala', 
'lion', 'mole', 'moose', 'moth', 'mouse', 'owl', 'panda', 'pig', 'pug', 'rat', 'ray', 
'roach', 'seal', 'shark', 'sheep', 'skink', 'skunk', 'sloth', 'slug', 'snail', 'snake', 
'swan', 'tiger', 'toad', 'wasp', 'whale', 'wolf', 'worm', 'yak', 'zebra']

adjlist = ['bad', 'baggy', 'bare', 'basic', 'big', 'black', 'bland', 'blind', 'blue', 
'bold', 'bony', 'bossy', 'brave', 'brisk', 'brown', 'bulky', 'bumpy', 'burly', 'busy', 
'calm', 'cheap', 'clean', 'cold', 'cool', 'crazy', 'crisp', 'cruel', 'curly', 'cute', 
'damp', 'dark', 'dim', 'dirty', 'dizzy', 'dopey', 'dual', 'dull', 'eager', 'easy', 
'empty', 'even', 'evil', 'faint', 'fair', 'fake', 'false', 'fancy', 'fast', 'fat', 
'fine', 'fixed', 'flaky', 'flat', 'fluid', 'fond', 'frail', 'free', 'fresh', 'full', 
'funny', 'fussy', 'fuzzy', 'giant', 'giddy', 'glum', 'good', 'grand', 'grave', 'grey', 
'great', 'green', 'grim', 'grimy', 'gross', 'grown', 'gummy', 'hairy', 'handy', 'happy', 
'harsh', 'hasty', 'heavy', 'hefty', 'hot', 'huge', 'husky', 'icy', 'ideal', 'idle', 
'ill', 'itchy', 'jaded', 'jolly', 'juicy', 'jumbo', 'jumpy', 'keen', 'kind', 'kooky', 
'lame', 'lanky', 'large', 'late', 'lazy', 'leafy', 'lean', 'light', 'live', 'livid', 
'lone', 'lost', 'loud', 'low', 'loyal', 'lucky', 'lumpy', 'mad', 'major', 'male', 
'mealy', 'mean', 'meek', 'merry', 'messy', 'mild', 'minor', 'minty', 'misty', 'moral', 
'muddy', 'murky', 'mushy', 'musty', 'muted', 'naive', 'nasty', 'neat', 'needy', 'new', 
'nice', 'nifty', 'nippy', 'noisy', 'novel', 'numb', 'nutty', 'odd', 'oily', 'old', 'open', 
'oval', 'pale', 'pesky', 'petty', 'pink', 'plain', 'plump', 'plush', 'poor', 'posh', 
'prime', 'prize', 'proud', 'puny', 'pure', 'pushy', 'quick', 'quiet', 'rapid', 'rare', 
'rash', 'real', 'red', 'regal', 'rich', 'right', 'rigid', 'ripe', 'rosy', 'rough', 
'round', 'rowdy', 'royal', 'rude', 'runny', 'rusty', 'sad', 'safe', 'sandy', 'sane', 
'scaly', 'scary', 'shady', 'sharp', 'shiny', 'short', 'showy', 'shy', 'sick', 'silky', 
'silly', 'slim', 'slimy', 'slow', 'small', 'smart', 'smug', 'soft', 'solid', 'sore', 
'sour', 'stale', 'stark', 'steel', 'sunny', 'super', 'sweet', 'swift', 'tall', 'tame', 
'tan', 'tasty', 'tense', 'thick', 'thin', 'tidy', 'tiny', 'tired', 'torn', 'tough', 
'true', 'tubby', 'twin', 'ugly', 'unfit', 'upset', 'urban', 'vague', 'vain', 'vast', 
'vital', 'vivid', 'warm', 'wary', 'wavy', 'weak', 'weary', 'wee', 'weepy', 'weird', 
'white', 'wide', 'wild', 'windy', 'wiry', 'wise', 'witty', 'woozy', 'wordy', 'worn', 
'young', 'yummy', 'zany', 'zesty']

class PasswordGenerator:

    def __init__(self, adjlist=adjlist, nounlist=nounlist, difficulty=7):
        self.difficulty = difficulty
        try:
            assert isinstance(nounlist, list)
            assert isinstance(adjlist, list)
        except AssertionError:
            raise AttributeError("Nounlist and Adjlist must be of type 'list'")
            
        self.nounlist = [x for x in nounlist if len(x) <= difficulty]
        self.adjlist = [x for x in adjlist if len(x) <= difficulty]
        
        if self.difficulty < 3:
            raise AttributeError("Difficulty must >= 3 ", f"Difficulty = {self.difficulty}")

    def __str__(self):
        return ("Password generator object - %i nouns and %i adjectives with a max difficulty of %i" % (len(self.nounlist), len(self.adjlist), self.difficulty))

    def __len__(self):
        return (self.difficulty * 2) + 2

    def randListItem(self, l):
        return l[randint(0, len(l)-1)]

    def generateBasicPassword(self):
        return self.randListItem(self.adjlist) + self.randListItem(self.nounlist) + str(randint(10, 99))