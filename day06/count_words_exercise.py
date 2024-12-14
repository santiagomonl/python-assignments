##Count_words

import sys
print(sys.argv)

def file_call():
    for file in sys.argv[1:]:
        print(file)
    print(sys.argv[1])
    filename = sys.argv[1]

    with open(filename, "r") as fh:
        textfile = fh.read()
    return textfile

textfile=file_call()

def count_number_of_each_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

res = count_number_of_each_words(textfile)

for key in res.keys():
    print (key, res[key])