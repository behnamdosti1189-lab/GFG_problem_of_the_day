'''
Swap Bits

Given a number X and two positions (from right side) in binary representation of x, write a program that swaps N bits at given two positions and returns the result.

https://practice.geeksforgeeks.org/problems/swap-bits5726/1
'''
#User function Template for python3
#Bit Manipulation refer video https://www.youtube.com/watch?v=5crWUE65q44
#Let's Practice Together
class Solution:
    def swapBits(self, X, P1, P2, N):
        m=(1<<(N-1)) | ((1<<(N-1))-1)
        bs1, bs2=m&(X>>P1), m&(X>>P2)
        X&=~((m<<P1)|(m<<P2))
        X= X | (bs1<<P2) | (bs2<<P1)
        return X



#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))
        

# } Driver Code Ends