# testing demo stuff can go here!
import re

file = open('words_huge.txt')
for line in file:
    fox = re.search("fox", line)
    if fox:
        print(line)

