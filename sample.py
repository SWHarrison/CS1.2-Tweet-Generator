import histogram, random

def sample_lists_of_lists(file_name):

    text = histogram.load_words(file_name)
    histogram_list = histogram.histogram_list_of_lists(text)
    max = len(text)
    print("number of words is: " + str(max))
    value = random.randrange(max)

    count = 0
    index = 0
    while(count < value):
        index += 1
        count += histogram_list[index][1]


    return histogram_list[index][0]

file_name = "notes.txt"

print(sample(file_name))
