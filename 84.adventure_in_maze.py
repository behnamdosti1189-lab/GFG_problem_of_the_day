'''
Adventure in a Maze 

https://practice.geeksforgeeks.org/problems/adventure-in-a-maze2051/1#

First hard dp problem solved completely so happy
'''

#User function Template for python3
import sys
sys.setrecursionlimit(10**9)

class Solution:
    def ctPath(self,i,j,n,m,matrix,dp):
        if(i>=n or j>=m):
            return 0
        
        if(i==n-1 and j==m-1):
            return 1
    
        if(dp[i][j]!=-1):
            return dp[i][j]
        
        right,down,right_fin,down_fin = 0, 0, 0, 0
        
        if(matrix[i][j]==1):
            #go right
            right = self.ctPath(i,j+1,n,m,matrix,dp)
        elif(matrix[i][j]==2):
            #go down
            down = self.ctPath(i+1,j,n,m,matrix,dp)
        elif(matrix[i][j]==3):
            #go right and down
            right_fin = self.ctPath(i,j+1,n,m,matrix,dp)
            down_fin = self.ctPath(i+1,j,n,m,matrix,dp)
        
        #print(sum(right,down,right_fin,down_fin))
        
        dp[i][j]= right+down+right_fin+down_fin
        return dp[i][j]


    def maxPath(self,i,j,n,m,matrix,dp):
        if(i>=n or j>=m):
            return -999999999
        
        if(i==n-1 and j==m-1):
            return matrix[n-1][m-1]
        
        if(dp[i][j]!=-1):
            return dp[i][j]
        
        right,down,right_fin,down_fin = -999999999,-999999999,-999999999,-999999999
        
        if(matrix[i][j]==1):
            #go right
            right = 1 + self.maxPath(i,j+1,n,m,matrix,dp)
        elif(matrix[i][j]==2):
            #go down
            down = 2 + self.maxPath(i+1,j,n,m,matrix,dp)
        elif(matrix[i][j]==3):
            #go right and down
            right_fin = 3 + self.maxPath(i,j+1,n,m,matrix,dp)
            down_fin = 3 + self.maxPath(i+1,j,n,m,matrix,dp)
        
        #print(max(right,down,right_fin,down_fin))
        
        dp[i][j]=max(right,down,right_fin,down_fin)
        return dp[i][j]
    
    def FindWays(self,matrix):
        # Code here
        mod = (10**9)+7
        n=len(matrix)
        m=len(matrix[0])
        dp = [[-1 for i in range(m+1)] for j in range(n+1)]
        maxi = self.maxPath(0,0,n,m,matrix,dp)
        dp = [[-1 for i in range(m+1)] for j in range(n+1)]
        ct = self.ctPath(0,0,n,m,matrix,dp)
        
        if(maxi<0):
            maxi=0
            
    
        return [ct%mod,maxi%mod]
    		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			matrix.append(cur)
		obj = Solution()
		ans = obj.FindWays(matrix)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends