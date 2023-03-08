def twoSum(arr, k):

    myMap = {}
    count = 0

    for num in arr:
        myMap[num] = 1 + myMap.get(num, 0)

    for num in arr:
        if k - num in myMap:
            if myMap[num] > 1 or k - num != num:
                count += myMap[k - num]

    return count // 2

print(twoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))