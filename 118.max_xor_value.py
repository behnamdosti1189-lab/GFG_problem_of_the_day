# Subsets with XOR value 

# Given an array arr of N integers and an integer K, find the number of subsets of arr having XOR of elements as K.

# https://practice.geeksforgeeks.org/problems/subsets-with-xor-value2023/1#

#User function Template for python3

import math
class Solution:
    def subsetXOR(self, arr, N, k): 
        # code here
        dp = [[0 for i in range(128)] for j in range(N+1)]
        dp[0][0] = 1
        for i in range(1,N+1):
            for j in range(128):
                dp[i][j] = dp[i-1][j] + dp[i-1][j^arr[i-1]]
        return dp[N][k]

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(' ')
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr,N,K))
# } Driver Code Ends