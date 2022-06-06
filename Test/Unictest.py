#Ctrl + Shift + E in Visual Studio to open the folder direction so it can detect where's the location
#in case the terminal is not detecting it.

import time
import re

tic = time.perf_counter()

dictionary = open('words.txt', 'r')
words_cleaned = [re.sub(r"[^a-zA-Z]","",i) for i in dictionary]
clean = set(words_cleaned)
clean = list(clean)
clean.sort()

newuniques =  open(r'uniques.txt', 'w', encoding='UTF-8')
for x in clean:
    _x = x[:4]
    if len(x) >= 4:
        newuniques.write(_x+'\n')                  
    
newfullwords = open(r'fullwords.txt', 'w', encoding='UTF-8')
for x in clean:
    if len(x) >= 4:
        newfullwords.write(x+'\n')
    
toc = time.perf_counter()
print(f'{toc - tic:0.4f}')


#I did it on python because for me, its easier, less tedious and less complicated. 
#i hate PHP and i feel it was better on python than in C# in my case. 

#Bonus Question Answer: can be solved in under than 10 miliseconds 
#by paralellism, a better computer or a better programmed solution. 
#Deppends of the situation but its possible.