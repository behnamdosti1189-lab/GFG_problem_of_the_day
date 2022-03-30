'''
Counts Zeros Xor Pairs 

Given an array A[] of size N. Find the number of pairs (i, j) such that
Ai XOR Aj = 0, and 1 ≤ i < j ≤ N.

https://practice.geeksforgeeks.org/problems/counts-zeros-xor-pairs0349/1#
'''

#User function Template for python3


def calculate (arr, n) : 
    #Complete the function
    #Brute Force
    # ct=0
    # for i in range(n):
        # for j in range(i+1,n):
            # if(arr[i]^arr[j]==0):
                # ct+=1
    # return ct
    
    #xor of same values is zero so we have to find the combination in which we can choose them
    # 5 5 5 5 -> nC2 -> n*n-1/2
    
    store = dict()
    for i in arr:
        if i in store:
            store[i]+=1
        else:
            store[i] = 1
            
    ct = 0
    for key,val in store.items():
        if(val>1):
            ct += (val*(val-1))//2
    
    return ct 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = calculate(arr, n)
    print(res)


# } Driver Code Ends