import math
import sys
sys.setrecursionlimit(10**9)
class Solution:
    # def gcd(self,a,b):
    #     if(b==0):
    #         return a
    #     else:
    #         return self.gcd(b,abs(a-b))
    
    def helper(self,root,ans):
        if(root==None or (root.left==None and root.right==None)):
            return
        
        self.helper(root.left,ans)
        
        data1 = -1
        if(root.left!=None):
            data1 = root.left.data
        
        data2 = -1
        if(root.right!=None):
            data2 = root.right.data
        
        if(data1!=-1 and data2!=-1):
            res = math.gcd(data1,data2)
            if(res>ans[0]):
                ans[0] = res
                ans[1] = root.data
    
        self.helper(root.right,ans)
        
    def maxGCD(self, root):
        # code here
        ans = [-1,0]
        self.helper(root,ans)
        return ans[1]
