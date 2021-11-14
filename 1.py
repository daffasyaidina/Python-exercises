import re

def hapax(path):
    txt = open(path,"r",encoding="utf-8")
    words = re.findall("\w+", txt.read().lower())
    freq = {key: 0 for key in words}
    for word in words:
        freq[word] += 1
    for word in freq:
        if freq[word] == 1:
            print (word)


hapax("e:/werk/Algorithm and programming/Exercise(LEC)/poem.txt")