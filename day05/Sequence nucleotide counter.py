#Sequence nucleotides counter
import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Change to a new directory  (replace with your desired path)
new_directory = "c:/Users/santi/Documents/python_class_2024/python-assignments/day05" # Example
os.chdir(new_directory)

# Verify the change
current_directory = os.getcwd()
print(f"New Current Directory: {current_directory}")

question= "y"
while question == "y":
    def file_call():
        filename = input("Enter the name of the file (filename.txt): ")
        print(filename)
        with open(filename, "r") as fh:
            text= fh.read()
        return text

    text = file_call()

    def count_nucleotides(text):
        A = 0
        C = 0
        G = 0
        T = 0
        nucleotides = 0
        UnKnown = 0
        for nucleotide in text:
            nucleotides += 1
            if nucleotide == "A":
                A += 1
            elif nucleotide == "C":
                C += 1
            elif nucleotide == "G":
                G += 1
            elif nucleotide == "T":
                T += 1
            else:
                UnKnown += 1
        return A, C, G, T, nucleotides, UnKnown

    A, C, G, T, nucleotides, UnKnown = count_nucleotides(text)

    def porcetage_nucleotides(A, C, G, T, nucleotides, UnKnown):
        A_percetage = round((A / nucleotides) * 100, 1)
        C_percetage = round((C / nucleotides) * 100, 1)
        G_percetage = round((G / nucleotides) * 100, 1)
        T_percetage = round((T / nucleotides) * 100, 1)
        unknown_percetage = round((UnKnown / nucleotides) * 100, 1)
        return A_percetage, C_percetage, G_percetage, T_percetage, unknown_percetage


    A_percetage, C_percetage, G_percetage, T_percetage, unknown_percetage = porcetage_nucleotides(A, C, G, T, nucleotides, UnKnown)

    number_of_nucleotides = [A, C, G, T, UnKnown]
    percentage_of_nucleotides = [A_percetage, C_percetage, G_percetage, T_percetage, unknown_percetage]

    nucleotides_names = ["A", "C", "G", "T", "Unknown"]

    for nucleot, count, percentages in zip(nucleotides_names, number_of_nucleotides, percentage_of_nucleotides):
        print(nucleot, ":", count, percentages)
    
    print("Total:", nucleotides)
    question=input("Do you want to open a new file? (y/n): ")