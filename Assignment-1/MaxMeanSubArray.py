
def meanMaxSubArray(arr, k):
    currSum = 0
    maxSum = 0

    for l in range(len(arr) - (k - 1)):  

        r = l + (k - 1)
        currSum = 0


        for i in range(l, r + 1):
            currSum = currSum + arr[i]
        
        maxSum = max(maxSum, currSum)

    return maxSum/k


print(meanMaxSubArray([4, 5, -3, 2, 6, 1], 2))
print(meanMaxSubArray([4, 5, -3, 2, 6, 1], 3))
print(meanMaxSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))
print(meanMaxSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))

#Big-Oh is size n*k, worst case O(n^2)
#Define what your variables are and state what the big-oh is based on those
