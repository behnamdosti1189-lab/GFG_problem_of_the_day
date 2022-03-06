'''
Compute Before Matrix 

https://practice.geeksforgeeks.org/problems/85781966a9db2a1ac17eaaed26a947eba5740d56/1#
'''
#User function Template for python3

class Solution:
    def computeBeforeMatrix(self, N, M, after):
        for j in range(M-1, -1, -1):
            for i in range(N-1, -1, -1):
                if i - 1 < 0:
                    val1 = 0
                else:
                    val1 = after[i-1][j]
                if j - 1 < 0:
                    val2 = 0
                else:
                    val2 = after[i][j-1]
                if i-1 < 0 or j-1 < 0:
                    val3 = 0
                else:
                    val3 = after[i-1][j-1]
                    
                after[i][j] = after[i][j] - (val1+val2) + val3
        return after 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, M =[int(i) for i in input().split()]
        after= []
        for j in range (N):
            after.append([int(i) for i in input().split()])
        ob = Solution()
        before=ob.computeBeforeMatrix(N,M,after)
        for i in range(len(before)): 
            for j in range(len(before[i])):
                print(before[i][j],end=' ')
            print()
        
        
        T -= 1
# } Driver Code Ends