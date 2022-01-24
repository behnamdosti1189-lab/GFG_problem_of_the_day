'''
Next Permutation 

Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

https://practice.geeksforgeeks.org/problems/next-permutation5226/1#
'''

#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        i=N-2
        while(i>=0 and arr[i]>=arr[i+1]):
            i-=1
        if(i>=0):
            j=N-1
            while(j>=0 and arr[i]>=arr[j]):
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
            arr2 = arr[:i+1]+arr[:i:-1]
        else:
            arr2 = arr[::-1]
        #print(arr,arr2,arr[:i+1],arr[:i:-1])
        
        return arr2
        
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
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends