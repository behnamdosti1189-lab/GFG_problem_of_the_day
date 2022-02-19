'''
Find the number of islands 

Given a grid of size n*m (n is number of rows and m is number of columns grid has) consisting of '0's(Water) and '1's(Land). Find the number of islands.
Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1#

Flood filling algorithm based on BFS or DFS

if we find 1 in grid we will call our recursive func to make it zero in all directions
basically we are flooding the islands
'''

#User function Template for python3
import sys
sys.setrecursionlimit(10**9) 

class Solution:
    
    def flood(self,grid,i,j):
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1):
            return
        
        grid[i][j]=0
        
        self.flood(grid,i+1,j)
        self.flood(grid,i,j+1)
        self.flood(grid,i-1,j)
        self.flood(grid,i,j-1)
        
        self.flood(grid,i+1,j-1)
        self.flood(grid,i-1,j-1)
        self.flood(grid,i+1,j+1)
        self.flood(grid,i-1,j+1)
        
    
    def numIslands(self,grid):
        #code here
        ct=0
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if(grid[i][j]==1):
                    
                    self.flood(grid,i,j)
                    ct+=1
                    #print(ct)
        
        return ct
                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends