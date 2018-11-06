import time

def load_words(file_name):
    file = open(file_name,'r')
    read_words = file.readlines()
    file.close()
    words = list()
    for line in read_words:
        split_line = line.strip().split(" ")
        for word in split_line:
            if(word.lower() != ""):
                words.append(word.strip("(),!."))

    return words

def histogram_list_of_lists(text):
    words = text

    #print(words)

    to_return = list()

    for word in words:
        wasFound=False
        for value in to_return:
            if word.lower() == value[0].lower():
                wasFound=True
                value[1] += 1
                break

        if not wasFound:
            to_add = list()
            to_add.append(word.lower())
            to_add.append(1)
            to_return.append(to_add)

    return to_return


def histogram_count_lists_try_catch(text):
    words = text

    to_return = list()
    ones_list = list()
    ones_list.append(1)
    empty_list = list()
    ones_list.append(empty_list)
    to_return.append(ones_list)

    for word in words:
        wasFound=False
        for array in to_return:
            try:
                index = array[1].index(word.lower())
                wasFound=True
                if(array[0] == len(to_return)):
                    word_to_add = array[1].pop(index)
                    to_add = list()
                    to_add.append(array[0]+1)
                    list_list = list()
                    list_list.append(word_to_add)
                    to_add.append(list_list)
                    to_return.append(to_add)
                else:
                    word_to_add = array[1].pop(index)
                    count = array[0]
                    to_return[count][1].append(word_to_add)

                break

            except ValueError:
                pass

        if not wasFound:
            to_return[0][1].append(word.lower())

    max = len(to_return)
    for index in range(max):
        if(not to_return[max-index-1][1]):
            to_return.pop(max-index-1)
    return to_return

def histogram_count_lists(file_name):
    words = load_words(file_name)

    to_return = list()
    ones_list = list()
    ones_list.append(1)
    empty_list = list()
    ones_list.append(empty_list)
    to_return.append(ones_list)

    for word in words:
        wasFound=False
        for array in to_return:
            index = 0
            while(index < len(array[1])):
                if(word.lower() == array[1][index]):
                    wasFound=True
                    break
                else:
                    index += 1

            if(wasFound):
                if(array[0] == len(to_return)):
                    word_to_add = array[1].pop(index)
                    to_add = list()
                    to_add.append(array[0]+1)
                    list_list = list()
                    list_list.append(word_to_add)
                    to_add.append(list_list)
                    to_return.append(to_add)
                else:
                    word_to_add = array[1].pop(index)
                    count = array[0]
                    to_return[count][1].append(word_to_add)

                break

        if(not wasFound):
            to_return[0][1].append(word.lower())

    return to_return



#text = "how How now Brown brown cow cow cow"
#current = time.perf_counter()
#text = load_words("notes.txt")
#print(histogram_count_lists("notes.txt"))
#print(histogram_list_of_lists(text))
#print(histogram_count_lists_try_catch(text))
#print(time.perf_counter()-current)
