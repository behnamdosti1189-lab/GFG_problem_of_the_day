# A Special Keyboard 
# https://practice.geeksforgeeks.org/problems/228d0aa9f26db93ee5b2cb3583dbd4b197447e16/1

#User function Template for python3

class Solution:
    def findTime(self, S1, S2):
        # code here
        time=0
        for i in range(len(S2)):
            if i==0:
                time+=S1.index(S2[i])
            else:
                ab=abs(S1.index(S2[i])-S1.index(S2[i-1]))
                time+=ab
        return time

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1=input()
        S2=input()
        
        ob = Solution()
        print(ob.findTime(S1,S2))
# } Driver Code Ends