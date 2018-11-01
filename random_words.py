import random, sys
params = sys.argv[1:]

file = open('/usr/share/dict/words','r')
read_words = file.readlines()
file.close()

for i in range (int(params[0])):
    index = random.randrange(len(read_words)-i)
    print(read_words[index].rstrip())
    read_words[index], read_words[-i] = read_words[-i],read_words[index]
