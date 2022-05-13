# Maximize The Array 

# Given two integer arrays Arr1 and Arr2 of size N. Use the greatest elements from the given arrays to create a new array of size N such that it consists of only unique elements and the sum of all its elements is maximum.

# https://practice.geeksforgeeks.org/problems/maximize-the-array3340/1

#User function Template for python3

from heapq import heappush as hp, heappop as hpo 
class Solution:
    def maximizeArray(self, arr1, arr2, n):
        heap =[]
        vis = set()
        for idx,ele in enumerate(arr2+arr1):
            if ele not in vis:
                hp(heap,(ele,idx))
                vis.add(ele)
                if len(heap)>n:
                    hpo(heap)
        return map(lambda x:x[0],sorted(heap,key = lambda x:x[1]))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maximizeArray(arr1, arr2, n)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1

# } Driver Code Ends