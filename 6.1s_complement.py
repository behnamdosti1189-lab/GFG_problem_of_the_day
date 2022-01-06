'''
1's Complement 

Given an N bit binary number, find the 1's complement of the number. The ones' complement of a binary number is defined as the value obtained by inverting all the bits in the binary representation of the number (swapping 0s for 1s and vice versa).

Example 1:

Input:
N = 3
S = 101
Output:
010
Explanation:
We get the output by converting 1's in S
to 0 and 0s to 1
Example 2:

https://practice.geeksforgeeks.org/problems/1s-complement2819/1#
'''
#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        # code here
        res=''
        for i in str(S):
            if(i=='1'):
                res+='0'
            else:
                res+='1'
        
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.onesComplement(S,N))
# } Driver Code Ends