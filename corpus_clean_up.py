import re

def load_words(file_name):
    '''Loads words from a file and cleans text of most special characters'''
    file = open(file_name,'r')
    read_words = file.readlines()
    file.close()
    pattern = '\d:\d'
    no_num = list()
    for line in read_words:
        no_num.append((re.sub(pattern, "" , line)))
    words = list()
    for line in no_num:
        split_line = line.strip().split(" ")
        for word in split_line:
            if(word.lower() != ""):
                words.append(word.strip(":;(),!."))

    return words

file_name = "raw_corpus_part.txt"
words = load_words(file_name)
print(words)
