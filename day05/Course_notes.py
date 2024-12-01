#Notes
#one can use the f2 botton to replace or rename a variable once for all the file
#call the file
#filename = "day05/digits.txt"
#filename = input("Enter the name of the file: ")
import sys
print(sys.argv)

def file_call():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} filename")
    for file in sys.argv[1:]:
        print(file)
    print(sys.argv[1])
    filename = sys.argv[1]

    with open(filename, "r") as fh:
        text = fh.read()
    return text

text = file_call()

#count the number of digits and right click to refactor and extract methods
def count_digits(text):
    number_of_digits = [0] * 10
    print(number_of_digits)
    for char in text:
        if char.isdigit():
            number_of_digits[int(char)] +=1
    return number_of_digits

number_of_digits = count_digits(text)

def enumerate_digits(number_of_digits):
    for i, count in enumerate (number_of_digits):
        print(f"{i}: {count}")

enumerate_digits(number_of_digits)
