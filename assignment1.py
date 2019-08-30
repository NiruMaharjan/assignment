class Assignment():
    def word_count(self,str):
        f = open(str, "r")
        str= f.read()
        counts = dict()
        words = str.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
a =  Assignment()
print(a.word_count("sonnet.txt"))


#print( word_count('the quick brown fox jumps over the lazy dog.'))
