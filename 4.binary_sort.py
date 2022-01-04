#User function Template for python3

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        #Your code here
        #No need to print the array
        ct1=0
        ct0=0
        for i in A:
            if i==1:
                ct1+=1
            else:
                ct0+=1
                
        res=[]
        
        for i in range(ct0):
            res.append(0)
        
        for i in range(ct1):
            res.append(1)

        for i in range(len(res)):
            A[i] = res[i]
        
        return A
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            obj = Solution()
            obj.binSort(A,N)
            
            for i in A:
                print(i,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends