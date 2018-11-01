import random, sys
params = sys.argv[1:]
words = ""

for word in params:
    words += word
    words += " "

new_word = ""
length = len(words)

i = 1
while(i <= length):
    index = random.randint(0,length - i)
    new_word += words[index]
    #print(words[0:index])
    #print(words[index+1:])
    words = words[0:index] + words[index+1:]
    i += 1

print(new_word)
