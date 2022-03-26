'''
Maximum average subarray 

Given an array Arr of size N and a positive integer K, find the sub-array of length K with the maximum average.

https://practice.geeksforgeeks.org/problems/maximum-average-subarray5859/1#
'''
#User function Template for python3

class Solution:
    def findMaxAverage(self, arr, n, k):
        # code here
        sumi=0
        idx=0
        for i in range(k):
            sumi+=arr[i]
        maxsum = sumi
        
        for i in range(k,n):
            sumi+=arr[i]-arr[i-k]
            if(sumi>maxsum):
                maxsum = sumi
                idx = i-k+1
                
        return idx
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans+k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends
