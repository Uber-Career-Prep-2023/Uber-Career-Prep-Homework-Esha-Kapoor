#NOT SURE HOW TO DO WITH POINTERS
def backSpace(s1, s2):
        
        s1Stack = []
        s2Stack = []
        
        for i in range(len(s1)):

            if s1[i] == '#':
                if s1Stack:
                    s1Stack.pop()

            else:
                s1Stack.append(s1[i])
            
        for i in range(len(s2)):

            if s2[i] == '#':
                if s2Stack:
                    s2Stack.pop()

            else:
                s2Stack.append(s2[i])
        
        return s1Stack == s2Stack

print(backSpace("Uber Career Prep", "u#Uber Careee#r Prep"))