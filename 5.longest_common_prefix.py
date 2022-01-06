#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        res=max(arr, key=len)
        #print(res)
        for i in range(len(arr)-1):
            tmp = arr[i]
            tmp2 = arr[i+1]
            ct=0
            for j in range(0,min(len(tmp),len(tmp2))):
                if(tmp[j]==tmp2[j]):
                    ct+=1
                else:
                    break
            tmp3 = tmp[:ct]
            if(len(res)>=len(tmp3)):
                res=tmp3
        
        if(res==''):
            return -1
        else:
            return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends