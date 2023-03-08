def reverse(myStr):

    l = 0 
    r = len(myStr) - 1

    vowels = {'a' , 'e' ,'o' , 'i' , 'u'}

    while l < r:

        if myStr[l] in vowels and myStr[r] in vowels:
            myStr[l] = myStr[r]
            myStr[r] = myStr[l]
            l += 1
            r -= 1

        elif myStr[l] in vowels:
            r -= 1

        else:
            l += 1

    return "".join(myStr)

# ""
# "aaa"
# "bbb"
# "####" redundant test case with line 22
# "bbabb"
# "aebb" -> "eabb"
# "t#era$"

#what happens when they meet? setting up a test case that proves that the code works when there is a vowel in the middle or two
#vowels in the middle
#with regards to pointers to the end, is that handled properly>
