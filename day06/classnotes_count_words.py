##Count_words
def count_words(text):
    words = text.split(",") #split the string where...
    return len(words)

print(count_words("name,23,value,42.1"))

def count_number_of_each_words(text):
    words = text.split(",")
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

res = count_number_of_each_words("name,23,value,42.1,name,25")
print(res)
print(res["name"])

for key in res.keys():
    print (key, res[key])

for key in ["23", "42.1", "25", "100"]:
    if key in res:
        print(key, res[key])
    else:
        print(key, "Not found")
    print(key, res.get(key, "Not found")) #This does the same of just taking the values that are in the dic otherwise fives "not found" message

def count_number_of_each_words_using_default_dict(text):
    from collections import defaultdict
    words = text.split(",")
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count

