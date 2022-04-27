# Killing Spree 

# https://practice.geeksforgeeks.org/problems/killing-spree3020/1#


#User function Template for python3

class Solution:
    def killinSpree (self, n):
        # code here
        low = 1
        high = 1000000
        count = 0
        while(low<=high):
            mid = low+(high-low)//2
            val = mid*(mid+1)*(2*mid+1)//6
            if val <= n:
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)




# } Driver Code Ends