'''
Maximum selections 

Geek wants to select the maximum number of course bundles at the Geek Summer Carnival. 

You are given a finite number of courses and N range of numbers each depicting a bundle of courses. Select the maximum number of bundles such that no courses overlap in any of the bundle.

Note: The ending of a range being the same as start of another isn't considered as an overlap.

https://practice.geeksforgeeks.org/problems/87ecf96cfd61e511c697c8c94d21c5de7f471fcb/1#
'''

# ranges[i][0] is the start of ith range
# ranges[i][1] is the end of ith range

class Solution:
    def max_non_overlapping(self,ranges):
        ranges = sorted(ranges, key=lambda x: x[1])
        res = 1
        prev = ranges[0]
        for i in range(1,len(ranges)):
            if ranges[i][0] >= prev[1]:
                res += 1 
                prev = ranges[i]
        return res

#{ 
#  Driver Code Starts
# driver code
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        line = input().strip().split()
        ranges = [[]  for j in range(n)]
        j=0
        for i in range(0,2*n,2):
            ranges[j].append(int(line[i]))
            ranges[j].append(int(line[i+1]))
            j+=1
            
        obj=Solution()
        print( obj.max_non_overlapping(ranges) )
# } Driver Code Ends