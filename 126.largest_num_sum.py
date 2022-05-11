# Largest number with given sum 

# https://practice.geeksforgeeks.org/problems/largest-number-with-given-sum-1587115620/1#
#User function Template for python3

class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        
        # code here
        if(n*9<s):
            return -1
        
        res=''
        while(s>0):
            if(s>9):
                res+='9'
                s-=9
            else:
                res+=str(s)
                s-=s
        
        if(len(res)<n):
            res += '0'*(n-len(res))
        
        return res
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends