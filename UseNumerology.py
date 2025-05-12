# Author: Joe Scuderi
# Due Date: 04/20/2024
# Numerology Assignment part 2 Use

from Numerology import Numerology

def main():

    while True:
        sName = input("Enter Name: ")

        if not sName:
            continue

        sDOB = input("Enter Birthday: ")



        if sDOB[2] == "-" and sDOB[5] == "-" or sDOB[2] == "/" and sDOB[5] == "/" and len(sDOB) == 10:
            break

    NumerologyObject = Numerology(sName,sDOB)

    print(NumerologyObject)

main()