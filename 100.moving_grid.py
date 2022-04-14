'''
Moving on grid 

https://practice.geeksforgeeks.org/problems/moving-on-grid1135/1#
'''

#User function Template for python3

class Solution:
	def movOnGrid(self, r, c):
		# code here
        
        if((r-1)%7==(c-1)%4):
            return "ARYA"
        else:
            return "JON"

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		r,c =map(int,input().strip().split())
		ob = Solution();
		print(ob.movOnGrid(r,c))

# } Driver Code Ends