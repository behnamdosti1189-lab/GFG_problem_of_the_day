class Solution():
    def solve(self, N, A):
        #your code here
        for i in range(len(A)-1,-1,-1):
            if(A[i]<9):
                return i+1
        
        return -1
