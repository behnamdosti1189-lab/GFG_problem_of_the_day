'''
Maximum sum of increasing order elements from n arrays 

Given n arrays of size m each. Find maximum sum obtained by selecting a number from each array such that the element selected from the i-th array is more than the element selected from (i-1)-th array. If maximum sum cannot be obtained then return 0.

https://practice.geeksforgeeks.org/problems/maximum-sum-of-increasing-order-elements-from-n-arrays4848/1
'''
#User function Template for python3

def maximumSum (n, m, arr) : 
    #Complete the function
    sumi = 0
    maxi = -999999999
    prevmax = 999999999
    for i in range(len(arr)-1,-1,-1):
        tmp = maxi
        for j in range(len(arr[i])):
            if(arr[i][j]<prevmax):
                maxi = max(arr[i][j],maxi)
        if(maxi==tmp):
            return 0
        prevmax = maxi
        sumi+=maxi
        maxi = -999999999
    
    return sumi
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n, m = map(int , input().split())
    arr = []
    for i in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    ans = maximumSum(n, m, arr)
    print(ans)




# } Driver Code Ends