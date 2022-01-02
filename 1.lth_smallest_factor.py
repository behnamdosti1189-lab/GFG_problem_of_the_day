#User function Template for python3

class Solution:
    def kThSmallestFactor(self, N , K):
        # code here 
        from math import sqrt
        v1=[]
        v2=[]
        i=1
        p = int(sqrt(N)) + 1
        for i in range(1,p,1):
            if(N%i==0):
                v1.append(i)
                if(i!=sqrt(N)):
                    v2.append(N//i)
        
        v2.reverse()
        #print(v1,v2)
        if(K>len(v1)+len(v2)):
            return -1
        elif(K<=len(v1)):
            return v1[K-1]
        else:
            return v2[K-len(v1)-1]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        
        ob = Solution()
        print(ob.kThSmallestFactor(N,K))
# } Driver Code Ends