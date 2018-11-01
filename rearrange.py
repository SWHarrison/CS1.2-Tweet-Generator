import random, sys
params = sys.argv[1:]

for i in range(0,len(params)):
    index = random.randrange(len(params))
    params[index], params[-i] = params[-i], params[index]

for word in params:
    print(word)
