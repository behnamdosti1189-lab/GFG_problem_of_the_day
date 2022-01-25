'''
Capacity To Ship Packages Within D Days 

Given an array arr[] of N weights. Find the least weight capacity of a boat to ship all weights within D days.
The ith weight has a weight of arr[i]. Each day, we load the boat with weights given by arr[i].We may not load more weight than the maximum weight capacity of the ship.

Note: You have to load weights on the boat in the given order.

https://practice.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1#

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

'''

#User function Template for python3

class Solution:
    def leastWeightCapacity(self,weights,N,D):
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True
    
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends