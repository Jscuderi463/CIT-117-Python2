# Author: Joe Scuderi
# Due Date: 11/3/2024
# Assignment: Lists and Real Estate Analyzer Using Files

import csv

# 1.) Create a Function called getDataInput and read in the file.

def getDataInput():
    with open("RealEstateData.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        ListData = []
        for row in reader:
            ListData.append(row)
        return ListData

# 2.) Create a getMedian Function that receives a list and returns a float of the calculated median

def getMedian(lstList1:list)->float:

    lstList1.sort()
    iListLength = len(lstList1)

    if iListLength % 2 == 0:
        print(f"The list length is even: {iListLength}")
        fMedianA = lstList1[iListLength // 2]
        fMedianB = lstList1[(iListLength // 2) - 1]

        fMedian = (fMedianA + fMedianB) / 2

        print(f"The Medians are {fMedianA, fMedianB}")
        print(f"The Median is: {fMedian}")
    else:
        print(f"The list length is odd: {iListLength}")
        fMedian = lstList1[iListLength // 2]
        print(f"The Median is: {fMedian}")

    return fMedian

# 3.) Create the Main function to determine the other analytics for the sales

def main():

    lstData = getDataInput()

    lstCities = []
    lstProperyType = []
    lstPrices = []

    dictPropertyType = {}
    dictCities = {}
    dictZip = {}

    for row in lstData:

        sCity = row[1]
        sPropertyType = row[7]
        fPrice = float(row[8])
        sZip = row[2]

        if sCity not in lstCities: lstCities.append(sCity)
        if sPropertyType not in lstProperyType: lstProperyType.append(sPropertyType)

        if sPropertyType in dictPropertyType:
            dictPropertyType[sPropertyType] += fPrice
        else:
            dictPropertyType[sPropertyType] = fPrice

        if sCity in dictCities:
            dictCities[sCity] += fPrice
        else:
            dictCities[sCity] = fPrice

        if sZip in dictZip:
            dictZip[sZip] += fPrice
        else:
            dict[sZip] = fPrice


        lstPrices.append(fPrice)

    lstPrices.sort()
    fMedian = getMedian(lstPrices)

    for sPropertyType, fTotal in dictPropertyType.items():
        print(f"{sCity:20s}{fTotal:15,.2f}")

    for sCity, fTotal in dictCities.items():
        print(f"{sCity:20s}{fTotal:15,.2f}")

    for sZip, fTotal in dictZip.items():
        print(f"{sZip:20s}{fTotal:15,.2f}")

    print(lstCities)
    print(lstProperyType)

    print(f"The min is: {min(lstPrices)}")
    print(f"The max is: {max(lstPrices)}")
    print(f"The sum is: {sum(lstPrices)}")
    print(f"The average is: {sum(lstPrices)/len(lstPrices)}")
    print(f"The median is: {fMedian}")

main()
