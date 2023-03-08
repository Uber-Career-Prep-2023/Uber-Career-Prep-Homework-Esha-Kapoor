#ALREADY DONE THIS PROBLEM BEFORE AND HAVE IT MEMORIZED. I HAVE ALL THE BLIND 75 PROBLEMS MEMORIZED (NEETCODE'S SOLNS)
#BECAUSE KNOWING THE PATTERNS FOR THOSE ALLOW ME TO SOLVE PROBLEMS I HAVE NOT SEEN BEFORE.

def shortSubstring(parent, child):

        countChild = {}
        countParent = {}

        if child == "":
            return ""
        
        for c in child:
            countChild[c] = 1 + countChild.get(c, 0)

        have = 0
        need = len(countChild)
        l = 0
        res = float("infinity")


        for r in range(len(parent)):

            c = parent[r]
            countParent[c] = 1 + countParent.get(c, 0)

            if c in countChild and countParent[c] == countChild[c]:
                have += 1

            while have == need:

                if (r - l + 1) < res:
                    res = r - l + 1

                countParent[parent[l]] -= 1

                if parent[l] in countChild and countParent[parent[l]] < countChild[parent[l]]:
                    have -= 1

                l += 1
        
        return res

print(shortSubstring("abracadabra", "abc"))
