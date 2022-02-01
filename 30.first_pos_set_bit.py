'''
Find position of set bit 

Given a number N having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.

https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1#
'''

#User function Template for python3
'''
A number will only have one signed bit if its a power of 2.
Thus, log base 2 of the number must be an integer, not a float point. 
Once, you determine, it's a power of 2, know that log gives you the 
0-based index of the number's signed bit, and you've to return 1-based index, 
thus add 1 to your answer and that's it.
'''
import math;
class Solution:
    def findPosition(self, N):
        if(N==0):
            return -1
        pos = math.log(N)/math.log(2)
        if(math.ceil(pos)==pos):
            return int(pos)+1
        else:
            return -1
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends