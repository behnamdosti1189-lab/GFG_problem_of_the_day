import heapq

class Solution:
    def minimizeSum(self, N, arr):
        # Code here
        heapq.heapify(arr)
        
        sumi = 0
        while(len(arr)>=2):
            tmp1 = heapq.heappop(arr)
            tmp2 = heapq.heappop(arr)
            sumi += tmp1+tmp2
            heapq.heappush(arr,tmp1+tmp2)
        
        return sumi
