class Assignment():
    def word_count(self,str):
        f = open(str, "r")
        str= f.read()
        counts = dict()
        words = str.split()
        count =1
        longest_word =''
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

        while(count <= len(longest_word)):
            #print(count + " letter word")
            words = [word for word in str.split() if len(word) == count]
            count += 1
            print(words)


a =  Assignment()
print(a.word_count("sonnet.txt"))
