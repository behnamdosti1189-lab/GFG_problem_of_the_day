'''
Special Matrix 

You are given a matrix having n rows and m columns. 
The special property of this matrix is that some of the cells of this matrix are blocked i.e. 
they cannot be reached. Now you have to start from the cell (1,1) and reach the end (n,m) provided during the journey you can move horizontally right from the current cell or vertically down from the current cell. Can you answer the number of ways you can traverse the matrix obeying the above constraints starting from (1,1) and ending at (n,m).

https://practice.geeksforgeeks.org/problems/special-matrix4201/1#
'''

#User function Template for python3
import sys
sys.setrecursionlimit(10**9)
class Solution:
    
    def solve(self,i,j,arr,dp):
        
        if(i<0 or j<0 or arr[i][j]==-1):
            return 0
        
        if(i==0 and j==0):
            return 1
        
        if(dp[i][j]!=-1):
            return dp[i][j]%1000000007
        
        right = self.solve(i,j-1,arr,dp)%1000000007
        down  = self.solve(i-1,j,arr,dp)%1000000007
        
        dp[i][j]=(right+down)%1000000007
        
        return dp[i][j]
            
    
	def FindWays(self, n, m, blocked_cells):
		# Code here
		
		mod=1000000007
		arr=[[0]*(m+1)]*(n+1)
	    arr = [[0 for j in range(m)] for i in range(n)]
		dp = [[-1 for j in range(m)] for i in range(n)]
		#print(arr)

		for point in blocked_cells:
		    arr[point[0]-1][point[1]-1] = -1
		   
		#print(arr)
		
		if (arr[0][0] == -1) or (arr[n-1][m-1] == -1):
           return 0
		
		return self.solve(n-1,m-1,arr,dp)
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, k= input().split()
		n = int(n); m = int(m); k = int(k);
		blocked_cells = []
		for i in range(k):
			a = list(map(int, input().split()))
			blocked_cells.append(a)
		obj = Solution()
		ans = obj.FindWays(n, m, blocked_cells)
		print(ans)

# } Driver Code Ends