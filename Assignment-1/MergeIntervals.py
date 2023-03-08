#ALREADY DONE THIS PROBLEM BEFORE AND HAVE IT MEMORIZED. I HAVE ALL THE BLIND 75 PROBLEMS MEMORIZED (NEETCODE'S SOLNS)
#BECAUSE KNOWING THE PATTERNS FOR THOSE ALLOW ME TO SOLVE PROBLEMS I HAVE NOT SEEN BEFORE.

def mergeIntervals(intervals):
        
        intervals.sort(key = lambda pair: pair[0])

        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)

            else:
                res.append([start, end])

        return res

print(mergeIntervals([[2, 3], [4, 8], [1, 2], [5, 7], [9, 12]]))