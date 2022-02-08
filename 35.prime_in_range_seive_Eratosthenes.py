'''
Find Prime numbers in a range 

Given two integers M and N, generate all primes between M and N.

https://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range4718/1

mycodeschool Solution:
https://www.youtube.com/watch?v=eKp56OLhoQs

Very easy algorithm just go through video
'''

#User function Template for python3

class Solution:   
    
    def primeRange(self,M,N):
        #code here
        arr=[1]*(N+1)
        arr[0]=0
        arr[1]=0
        for i in range(2,N):
            if(arr[i]==1):
                j=2
                while(i*j<=N):
                    arr[i*j]=0
                    j+=1
                    

        ans=[]
        for i in range(len(arr)):
            if(i>=M):
                if(arr[i]==1):
                    ans.append(i)
                    
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends