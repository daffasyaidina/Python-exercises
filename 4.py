#%%
import re

def splitter(path):
    txt = open(path, encoding="utf8")
    word = txt.read() 
    sentences = re.sub(r'\n','', word)  
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)  
    sentences = re.sub(r'!\s', '!\n', sentences) 
    sentences = re.sub(r'\?\s', '?\n', sentences) 
    print(sentences)

splitter("E:\werk\Algorithm and programming\Exercise(LEC)\Python exercise\mr.miyagi.txt")

# %%
