'''
Positive Negative Pair 

Given an array of distinct integers, find all the pairs having both negative and positive values of a number in the array.

https://practice.geeksforgeeks.org/problems/positive-negative-pair5209/1
'''
#User function Template for python3

class Solution:
    #Function to return list containing all the pairs having both
    #negative and positive values of a number in the array.
    def findPairs(self,arr, n):
        
        s = set()
        ret = []
        
        # For each element of array. 
        for i in arr:
            if abs(i) in s:
                ret.append(abs(i))
            else:
                s.add(abs(i))
        #print(ret)
        #ret.sort()
        res=[]
        for i in range(0, len(ret)):
            res.append(-ret[i])
            res.append(ret[i])
            #print(-ret[i], "", ret[i], end = " ")
        
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        res=Solution().findPairs(arr,n)
        if len(res) == 0:
            print(0)
        else:    
            for x in res:
                print(x,end=' ')
            print()
# } Driver Code Ends