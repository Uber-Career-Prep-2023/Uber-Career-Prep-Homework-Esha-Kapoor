def dedupArray(nums):

    if not nums:
        return []
        
    j = 0

    for i in range(1, len(nums)):

        if nums[i] != nums[j]:

            j += 1
            nums[j] = nums[i]
            
    return nums[:j+1]


print(dedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))