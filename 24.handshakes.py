'''
Handshakes

We have N persons sitting on a round table. Any person can do a handshake with any other person.

     1
2         3
     4

Handshake with 2-3 and 1-4 will cause cross.

In how many ways these N people can make handshakes so that no two handshakes cross each other. N would be even. 

https://practice.geeksforgeeks.org/problems/handshakes1303/1#
'''

#User function Template for python3

class Solution:
    
    def count(self,n):
        if n % 2 == 1: return 0
        elif n == 0: return 1
        res = 0
        for i in range(0, n, 2):
            res += self.count(i) * self.count(n-2-i)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.count(N))
# } Driver Code Ends