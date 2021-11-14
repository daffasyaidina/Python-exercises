import os

os.chdir("E:\werk\Algorithm and programming\Exercise(LEC)\Python exercise\super secret folder")

input = open("can you imagine.txt","r")
output = open("menagerie.txt","w")

count = 0

for line in input:
    count += 1
    output.write(f"{count:2d} {line}")

output.close()

