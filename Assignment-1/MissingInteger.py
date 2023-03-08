def missingInteger(arr, n):

    expected = n * (n+1) // 2 #Gauss I think? Just learned about this formula in discrete math.

    actual = sum(arr)
    return expected - actual
        

print(missingInteger([1, 2, 3, 4, 6, 7], 7))
print(missingInteger([1], 2))
print(missingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))