'''
Exactly one swap 

Given a string S containing lowercase english alphabet characters. The task is to calculate the number of distinct strings that can be obtained after performing exactly one swap.
In one swap,Geek can pick two distinct index i and j (i.e 1 < i < j < |S| ) of the string, then swap the characters at the position i and j.

URL.https://practice.geeksforgeeks.org/problems/2ac2f925b836b0625d848a0539ffd3d2d2995f92/1url.
'''

#User function Template for python3Solution:
    def countStrings(self, S): 
        n = len(S)
        charSet = {}
        count = 0
     in S:
         i in charSet:
                count = count + charSet[i] + 1
                charSet[i] += 1
        
                charSet[i] = 0
        ans = ((-1)) // 2
    (count >0):
            ans = ans - count + 1
    
