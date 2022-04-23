# Search insert position of K in a sorted array 

# Given a sorted array Arr[](0-index based) consisting of N distinct integers and an integer k, 
# the task is to find the index of k, if its present in the array Arr[]. Otherwise, 
# find the index where k must be inserted to keep the array sorted.

# https://practice.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1#

#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        low = 0
        high = N-1
        while(low<=high):
            mid = (low+high)//2
            if(Arr[mid]==k):
                return mid
            elif(Arr[mid]<k):
                low = mid+1
            else:
                high = mid-1
        return low



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends
