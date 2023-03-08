def kAnagrams(str1, str2, k):

    if len(str1) != len(str2):
        return False
    
    freq = [0] * 26

    for i in range(len(str1)):

        freq[ord(str1[i]) - ord('a')] += 1
        
    for i in range(len(str2)):

        freq[ord(str2[i]) - ord('a')] -= 1
        
    diff = 0

    for i in range(26):

        if freq[i] > 0:

            diff += freq[i]

        if diff > k:
            
            return False
        
    return True

print(kAnagrams("apple", "peach", 1))
print(kAnagrams("apple", "peach", 2))