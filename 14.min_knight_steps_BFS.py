'''
Steps by Knight 

Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.

Note:
The initial and the target position co-ordinates of Knight have been given accoring to 1-base indexing.

https://practice.geeksforgeeks.org/problems/steps-by-knight5927/1
'''

class cell:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

class Solution:
    def isInside(self, x, y, N):
        if x >= 0 and x <= N and y >= 0 and y <= N:
            return True
        return False

    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        queue = []
        queue.append(cell(KnightPos[0], KnightPos[1], 0))
        visited = [[False for j in range(N+1)] for i in range(N+1)]
        visited[KnightPos[0]][KnightPos[1]] = True
        while len(queue) > 0:
            front = queue[0]
            queue.pop(0)
            if front.x == TargetPos[0] and front.y == TargetPos[1]:
                return front.dist
            for i in range(8):
                x = front.x+dx[i]
                y = front.y+dy[i]
                if self.isInside(x, y, N) and not visited[x][y]:
                    visited[x][y] = True
                    queue.append(cell(x, y, front.dist+1))

#{ 
#  Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends

## REFER PDF SOLUTION OF CODE LIBRARY