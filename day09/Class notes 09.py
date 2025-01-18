##Class notes 09

##regular expressions
#Need library re

import re


## Funtions without parentesis are not called, you need to use parethesis to call and "activate" the funtion

##Regular expression (Regexes) are part of a tool/language separate from python 
#but integrated through the re library and can also be used inside the editor
#can also integrate pattern and can be used for searching
#but parenthesis and dots are special symbol, therefore need to be preceded by \
#and \b limits the search to the term search instead of complete words before the term used in the search
#this can be used to search for specific and complex things
#Is commonly used for input validation

##Example: r stand for row to keep the backslash as it is
text= "the lightBlack cat climed the tree"
match= re.search(r'cat', text)
if match:
    print("Matching")
    print (match.group(0))
else:
    print("Did Not Match")

match2= re.search(r'[a-zA-z]+lac[a-z]*', text)
if match2:
    print("Matching")
    print (match2.group(0))
else:
    print("Did Not Match")


#Example matching numbers: \d matches digit

line= "there is a phone number 12345000 in this row and an age: 23"

match= re.search(r'\d+', line)
if match:
    print(match.group(0))

match2= re.search(r"age: (\d+)", line) #create a second group using ()
if match2:
    print(match2.group(0)) # age: 23
    print(match2.group(1)) # 23

#Can do multiple groups and assign names to each group
regex= r"((?P<word>\w+) (?P<key>\w+)): (?P<value>\d+)"
match3=re.search(regex, line)
if match3:
    print(match3.group("word"))
    print(match3.group("key"))
    print(match3.group("value"))

##findall
#returns a list of all the matched substrings

line= "there is a phone number 12345000 in this row and an age: 23"
matchall= re.findall(r'\d+', line)
if matchall:
    print(matchall)


## Class 1:30:00

##Looking for subsequence that repeats itself:
#What's is the longest subsequence that repeats itself


