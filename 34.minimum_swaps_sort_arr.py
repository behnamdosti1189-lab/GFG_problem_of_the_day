'''
Minimum Swaps to Sort 

Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

https://practice.geeksforgeeks.org/problems/minimum-swaps/1#
'''
class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        #Code here
        v=[]
        for i in range(len(nums)):
            v.append([nums[i],i])
        v.sort()
        ct=0
        i=0
        while(i<len(v)):
            tmp = v[i][1]
            if(tmp!=i):
                ct+=1
                v[i],v[tmp]=v[tmp],v[i]
                i-=1
            i+=1
        return ct

#{ 
#  Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)

# } Driver Code Ends