'''
Height Using Parent Array 

Given a parent array arr[] of a binary tree of N nodes. Element at index i in the array arr[] represents the parent of ith node, i.e, arr[i] = parent(i). Find the height of this binary tree.
Note: There will be a node in the array arr[], where arr[i] = -1, which means this node is the root of binary tree.

https://practice.geeksforgeeks.org/problems/height-using-parent-array4103/1#
'''
#User function Template for python3

class Solution:
    def findHeight(self, N, arr):
        # code here
        h=1
        k=arr[N-1]
        while(arr[k]!=-1):
            k=arr[k]
            h+=1
        return h+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.findHeight(N, arr))
# } Driver Code Ends