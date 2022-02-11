'''
Remove leading zeros from an IP address 

Given an IP address, remove leading zeros from the IP address. Note that our IP address here can be a little different. It can have numbers greater than 255. Also, it does not necessarily have 4 numbers. The count can be lesser/more.

https://practice.geeksforgeeks.org/problems/remove-leading-zeros-from-an-ip-address3530/1#
'''
#User function Template for python3

class Solution:
    def newIPAdd(self, S):
        # code here
        arr=S.split(".")
        res=[]
        for i in arr:
            tmp=i.lstrip('0')
            if(len(tmp)==0):
                tmp+='0'
            res.append(tmp)
        
        ans=''
        for i in res:
            ans+=i+'.'
        
        #print(res,ans)    
        return ans[:-1]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends