'''
Subsets

returns the list of list containing the subsets of the given set of numbers in lexicographical order.

https://practice.geeksforgeeks.org/problems/subsets-1613027340/1#
'''

#User function Template for python3

class Solution:
    
    def solve(self,idx,arr,ds,ans):
        if(idx==len(A)):
            ans.append([*ds])
            return
        
        
        ds.append(arr[idx])
        pick = self.solve(idx+1,arr,ds,ans)
        ds.pop()
        
        nonpick = self.solve(idx+1,arr,ds,ans)
    
    def subsets(self, A):
        #code here
        
        idx = len(A)-1
        ans=[]
        self.solve(0,A,[],ans)
        
        ans.sort()
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends