#Sequence nucleotides counter
import os

question= "y"
while question == "y":
    import sys
    print(sys.argv)
    number_of_files= 1 + int(input("How many files do you want to open? "))
    files = 0
    Ad = 0
    Ci = 0
    Gu = 0
    Ti = 0
    Unk = 0
    nucleo= 0
    for file in sys.argv[1:number_of_files]:
        if len(sys.argv) < number_of_files:
            exit(f"Usage: {sys.argv[0]} filename")
        print(file)
        files += 1
        filename = sys.argv[files]
        with open(filename, "r") as fh:
            text= fh.read()
        #return text
        #text = file_call()

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

        #All acum
        Ad = Ad + A
        Ci = Ci + C
        Gu = Gu + G
        Ti = Ti + T
        Unk = Unk + UnKnown
        nucleo = nucleo + nucleotides

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
    
    #All
    porcetage_nucleotides(Ad, Ci, Gu, Ti, nucleo, Unk)
    A_percetage, C_percetage, G_percetage, T_percetage, unknown_percetage = porcetage_nucleotides(Ad, Ci, Gu, Ti, nucleo, Unk)
    print("All")
    number_of_nucleotides = [Ad, Ci, Gu, Ti, Unk]
    percentage_of_nucleotides = [A_percetage, C_percetage, G_percetage, T_percetage, unknown_percetage]
    nucleotides_names = ["A", "C", "G", "T", "Unknown"]
    for nucleot, count, percentages in zip(nucleotides_names, number_of_nucleotides, percentage_of_nucleotides):
            print(nucleot, ":", count, percentages)
        
    print("Total:", nucleo)

    question=input("Do you want to run again? (y/n): ")