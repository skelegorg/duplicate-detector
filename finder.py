import string

def getFormatString():
    unformatted = input("Input the numbers desired, seperated with commas")
    format1 = unformatted.replace(" ", "")
    formatted = format1.split(",")
    try:
        for num in formatted:
            chek = int(num)
    except ValueError:
        print("please input the right hekking format")
        getFormatString()
    return formatted


def sorter(array):
    array.sort()
    return array


def findDuplicate(arrForSearch):
    print("finding duplicates")
    repeatedInts = []
    size = len(arrForSearch)
    for rangeCount in range(size):
        next = rangeCount + 1
        for rangeCount2 in range(next, size):
            if(arrForSearch[rangeCount] == arrForSearch[rangeCount2] not in repeatedInts):
                repeatedInts.append(arrForSearch[rangeCount])
    print(repeatedInts)

def checkDuplicate(arrForCheck):
    print("checking for duplicates")
    if(len(arrForCheck) != len(set(arrForCheck))):
        print("duplicates detected")
        findDuplicate(arrForCheck)
    else:
        print("no duplicates found")


checkDuplicate(getFormatString())
