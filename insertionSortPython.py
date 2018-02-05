def insertionSort1(n, arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1

        while j >=0 and key =< arr[j]: #for each element in array, do this
            arr[j+1] = arr[j]
            j -= 1 #keeps comparing to in the case where we have a element further right that needs to move all the way left.
            printArr(arr)

        arr[j+1] = key  #once above sort order is established, insert key where it is supposed to go
    printArr(arr)

def printArr(arr):
    printableArr = ''
    for i in arr:
        printableArr = printableArr + str(i) + " "
    print(printableArr)
