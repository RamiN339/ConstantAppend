import turtle as trtl
import random
import nltk
import csv
with open('nouns.csv', "r") as f:
    reader = csv.reader(f)
    data = list(reader)

nouns2 = str(data[0])
nouns2 = nouns2.replace('[', '')
nouns2 = nouns2.replace(']', '')
nouns2 = nouns2.split(',')
lengthofnounslist= len(nouns2)
wordstochange = (nouns2[0])
wordstochange = wordstochange.replace("'",'')

wordstochange1 =nouns2[int((lengthofnounslist)-1)]
wordstochange1 = wordstochange1.replace("'",'')

newnouns = []


for words in nouns2:
    if nouns2.index(words) != 0 and nouns2.index(words) != (int(lengthofnounslist)-1):
        newnouns.append(words)
newnouns.append(wordstochange)
newnouns.append(wordstochange1)





with open('verbs.csv', "r") as f:
    reader = csv.reader(f)
    data = list(reader)

verbs2 = str(data[0])
verbs2 = verbs2.replace('[', '')
verbs2 = verbs2.replace(']', '')
verbs2 = verbs2.split(',')
lengthofverbslist= len(verbs2)
vwordstochange = (verbs2[0])
vwordstochange = vwordstochange.replace("'",'')

vwordstochange1 =verbs2[int((lengthofverbslist)-1)]
vwordstochange1 = vwordstochange1.replace("'",'')

newverbs = []


for words in verbs2:
    if verbs2.index(words) != 0 and verbs2.index(words) != (int(lengthofverbslist)-1):
        newverbs.append(words)
newverbs.append(vwordstochange)
newverbs.append(vwordstochange1)



nouns = []
verbs = []
pronouns = []


  
import nltk
lines = input('Say Something: ')
is_noun = lambda pos: pos[:2] == 'NN'
is_verb = lambda pos: pos[:2] == 'VB'
tokenized = nltk.word_tokenize(lines)
noun = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
verb = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)] 
for noun1 in noun:
    nouns.append(noun1)

for words in newnouns:
    for wordss in nouns:
        if str(wordss) == str(words):
            nouns.pop(nouns.index(words))



for verb1 in verb:
    verbs.append(verb1)

for words in newverbs:
    for wordss in verbs:
        if str(wordss) == str(words):
            verbs.pop(verbs.index(words))
















            
with open('nouns.csv', 'w') as f:
    totalnouns = nouns + newnouns
    fields = ['nouns'] 
    rows = [",".join(totalnouns)]
    write = csv.writer(f)
    write.writerow(rows)


with open('verbs.csv', 'w') as f:
    totalverbs = verbs + newverbs
    fields = ['verbs'] 
    rows = [",".join(totalverbs)]
    write = csv.writer(f)
    write.writerow(rows)

lengthoftotalnouns = len(totalnouns)
lengthoftotalverbs = len(totalverbs)
nountosay = totalnouns[random.randint(0,int(lengthoftotalnouns)-1)]
objecttosay = totalnouns[random.randint(0,int(lengthoftotalnouns)-1)]
verbtosay = totalverbs[random.randint(0,int(lengthoftotalverbs)-1)]
print(nountosay + ' ' + verbtosay + ' ' + objecttosay + '.')



'''
class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

python = Snake("python")
anaconda = Snake("anaconda")
print (python.name)
print (anaconda.name)
'''