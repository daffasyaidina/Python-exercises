import re

def avgwords(path):
    txt = open(path,"r",encoding="utf-8")
    words = re.findall("\w+", txt.read().lower())
    length = sum([len(word) for word in words]) / len(words)
    print(f"{length:.2f}")

avgwords("E:\werk\Algorithm and programming\Exercise(LEC)\Python exercise\poem.txt")

