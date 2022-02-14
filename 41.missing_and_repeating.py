'''
Find Missing And Repeating 

Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
'''

# User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        arr.sort()
        #print(arr)
        rep=0
        mis=0
        if(len(arr)>=3):
            for i in range(len(arr)-1):
                if(arr[i+1]==arr[i]+1):
                    pass
                elif(arr[i+1]==arr[i]):
                    rep=arr[i+1]
                else:
                    mis=arr[i]+1
            if(mis==0):
                if(arr[0]!=1):
                    mis=1
                else:
                    mis=arr[-1]+1
        else:
            if(arr[0]==1 and arr[1]==1):
                rep=1
                mis=2
            else:
                rep=2
                mis=1
        ans=[]
        ans.append(rep)
        ans.append(mis)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends