'''
Concatenate two numbers 

Given an array numbers[] of N positive integers and a positive integer X, 
The task is to find the number of ways that X can be obtained by writing pair of integers in the array numbers[] next to each other. 
In other words, find the number of ordered pairs (i,j) such that i != j and X is the concatenation of numbers[i] and numbers[j]

https://practice.geeksforgeeks.org/problems/1df2447c003940512562d766cf0583bbdc7a75ed/1#
'''

#User function Template for python3
from collections import defaultdict
class Solution:
    def countPairs(self, n, x, arr):
        ans = 0
        x = str(x)
        f = defaultdict(int)
        for i in range(n):
            arr[i] = str(arr[i])
            if x.startswith(arr[i]) or x.endswith(arr[i]):
                f[arr[i]] += 1
        for s in list(f):
            if x == 2*s:
                ans += f[s]*(f[s]-1)
            elif x.endswith(s):
                ans += f[s]*f[x[:-len(s)]]
        return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        numbers = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(N, X, numbers)
        print(ans)


# } Driver Code Ends