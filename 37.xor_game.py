'''
XOR Game 

Given a positive number k, we need to find a minimum value of positive integer n, such that XOR of n and n+1 is equal to k. If no such n exist then print -1.

https://practice.geeksforgeeks.org/problems/xor-game2143/1
'''
#User function Template for python3

class Solution:
    def xorCal(self, k):
        # code here
        if(k==1):
            return 2
        
        if(k==3 or k==7 or k==15 or k==31 or k==63):
            return k//2

        return -1            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends