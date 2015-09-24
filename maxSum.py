'''
Jethro Chan
Wednesday September 23, 2015
Max value of Subarray Demonstration in Python 3.5.0
'''

def maximumSubAr(inputarray):
        
    if not inputarray:
        raise Exception("Error, Array Can't be Empty")
      
    currentTotal = inputarray[0]
    biggestTotal = inputarray[0]

    for i in range(1, len(inputarray)):
        if inputarray[i] <= (currentTotal + inputarray[i]):
            '''current element in the array will increase currentTotal'''
            currentTotal = inputarray[i] + currentTotal  
                      
        else:
            '''stop counting currently processed subarray's sum of array into total sum'''
            currentTotal = inputarray[i] 

        if currentTotal > biggestTotal:
            '''check if the value of the subarray we are working on has
            a bigger sum than the biggest Subarray Sum we have seen'''
            biggestTotal = currentTotal 

    return biggestTotal   
    

'''Calling our function to test it'''
maximumSum = maximumSubAr([11, -1, -6, 16, -5, -100, 12])
print ("Max Sum Value of any Subarray:", maximumSum)

