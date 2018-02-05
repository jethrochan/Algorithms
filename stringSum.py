# /**
#  * Given three strings, each composed of alphabetical letters A to Z, and a mapping from letters to 
#  * numbers 0 to 9, write a function to check if the mapping is valid so that the numbers represented 
#  * by the first two strings add up to the number represented by the third string.
#  * e.g. mapping = {A:2, B:3, C:1, D:4, E:6}
#  *   ABC                          231
#  * + ABC                        + 231
#  * ------------    ====>  ------------
#  *   DEA                          462
#  */


import math

def strToInt(arr):
    
    strLen = len(arr) - 1
    resultInt = 0
    
    for i in arr:
        temp = int(i)
        resultInt += (temp * math.pow(10, strLen))
        strLen -= 1
        
    return(int(resultInt)) 

def mapsum(str1, str2, resultStr, mapDict):
    
    arrStr1 = [None] * len(str1)
    arrStr2 = [None] * len(str2)
    arrResultStr = [None] * len(resultStr)
    
    for i in range(0, len(str1)):
        arrStr1[i] = str(mapDict[str1[i]])
                    
    for j in range(0, len(str2)):
        arrStr2[j] = str(mapDict[str2[j]])
    
    for k in range(0, len(resultStr)):
        arrResultStr[k] = str(mapDict[resultStr[k]])

    sum1 = strToInt(arrStr1)
    sum2 = strToInt(arrStr2)
    sum3 = strToInt(arrResultStr)
    
    inputSums = sum1 + sum2
    
    if inputSums == sum3:
        return True
    else:
        return False


mapDict = {"A":2, "B":3, "C":1, "D":4, "E":6}
print(mapsum("ABC", "ABC", "DEA", mapDict))
print(mapsum("AAA", "ABC", "DEA", mapDict))
print(mapsum("CCBC", "ABC", "DEA", mapDict)) 
