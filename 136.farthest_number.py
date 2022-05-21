# Farthest number 

# https://practice.geeksforgeeks.org/problems/1a31d09f7b8e9c0633339df07858deb3a728fe19/1#

#User function Template for python3

class Solution:
    def farNumber(self,N,Arr):
        #code here
        ans=[-1]*N
        for i in range(N):
            for j in range(N-1,i,-1):
                if Arr[j]<Arr[i]:
                    ans[i]=j
                    break
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        N=int(input())
        Arr=[int(x) for x in input().split()]
        
        ob = Solution()
        ans = ob.farNumber(N,Arr)
        
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends