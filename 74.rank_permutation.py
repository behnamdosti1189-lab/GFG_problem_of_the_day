'''
Rank The Permutations

Given a string, find the rank of the string amongst its permutations sorted lexicographically. 

https://practice.geeksforgeeks.org/problems/rank-the-permutations2229/1
''' 

#User function Template for python3

class Solution:
	def factorial(self,n):
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
        return fact
       
    def findRank(self, S):
     #Code here
        rank = 1
        for i in range (len(S)-1):
            count = 0
            for j in range(i+1,len(S)):
                if S[i]>S[j]:
                    count+=1
            rank += count * self.factorial(len(S) - 1 - i)
        return rank

#{ 
#  Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	str = input().strip()
    	obj = Solution()
    	ans = obj.findRank(str)
    	print(ans)
# } Driver Code Ends