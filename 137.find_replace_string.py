# Find an Replace in String 

# https://practice.geeksforgeeks.org/problems/find-an-replace-in-string/1#

#User function Template for python3

class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        res = []
        beg = 0
        for i in range(Q):
            ind = index[i]
            
            if S[ind:ind+len(sources[i])] == sources[i]:
                res.append(S[beg:ind])
                res.append(targets[i])
                beg = ind + len(sources[i])
            
            
        res.append(S[beg:len(S)])
        
        return "".join(res)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        Q=int(input())
        index=list(map(int,input().split()))
        sources=list(map(str,input().split()))
        targets=list(map(str,input().split()))
        
        ob = Solution()
        print(ob.findAndReplace(S,Q,index,sources,targets))
# } Driver Code Ends