import sys
sys.setrecursionlimit(10**9)
class Solution:
	
	def subs(self,idx,arr,dp):
	    if(idx==0):
	        return arr[0]
	    if(idx<0):
	        return 0
	       
	    if(dp[idx]!=-1):
	        return dp[idx]
	    
	    pick = arr[idx] + self.subs(idx-2,arr,dp)
	    nonpick = 0 + self.subs(idx-1,arr,dp)
	
	    dp[idx] =  max(pick,nonpick)
	    return dp[idx]
	
	def tabs(self,arr):
	    dp = [-1]*(n+1)
	    dp[0] = arr[0]
	    
	    for idx in range(1,n):
	        pick = arr[idx]
	        if(idx-2>=0):
	            pick += dp[idx-2]
	        nonpick = 0 + dp[idx-1]
	        dp[idx] = max(pick,nonpick)
	   # print(dp)
	    return dp[n-1]
	        
	def findMaxSum(self,arr, n):
		# code here
# 		dp = [-1]*(n+1)
# 		ans = self.subs(n-1,arr,dp)
        ans = self.tabs(arr)
		return ans
