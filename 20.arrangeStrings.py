#User function Template for python3

class Solution:
    def arrangeString(self, s):
        # code here
        sumi=0
        res=[]
        for i in s:
            if i.isdigit():
                sumi+=int(i)
            else:
                res.append(i)
        res.sort()
        ans=""
        for i in res:
            ans+=i
        ans+=str(sumi)
        
        return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends