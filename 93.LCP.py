'''
LCP 

Geek is at the geek summer carnival. He is given an array of N strings. To unlock exclusive course discounts he needs to find the longest common prefix among all strings present in the array. Can you help him ?

https://practice.geeksforgeeks.org/problems/cf0cd86c66d07222499f84ec22dbcf6cae30e848/1#
'''

#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        #code here
        arr.sort()
        
        first = arr[0]
        last = arr[-1]
        ans=''
    
        for i in range(len(arr[0])):
            if(first[i]==last[i]):
                ans+=first[i]
            else:
                break
        
        if(ans==''):
            return -1
        else:
            return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends