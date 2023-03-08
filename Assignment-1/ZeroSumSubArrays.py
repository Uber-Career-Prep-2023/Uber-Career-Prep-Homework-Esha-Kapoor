def countSubArrays(arr):

    res = 0
    mySum = 0
    myMap = {}

    for num in arr:
        mySum += num
            
        if mySum in myMap:
            res += myMap[mySum]
            myMap[mySum] += 1

        elif mySum == 0:
            res += 1

        else:
            myMap[mySum] = 1

    return res

print(countSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7]))