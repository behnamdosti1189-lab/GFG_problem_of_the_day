'''
Merge two binary Max heaps 

Given two binary max heaps as arrays, merge the given heaps to form a new max heap.

https://practice.geeksforgeeks.org/problems/merge-two-binary-max-heap0144/1#
'''

class Solution():

    def maxHeapify(self,arr,n,idx):
        if(idx>=n):
            return
        
        l = 2*idx+1
        r = 2*idx+2
        
        Max=0
        
        if(l<n and arr[l]>arr[idx]):
            Max=l
        else:
            Max=idx
        
        if(r<n and arr[r]>arr[Max]):
            Max=r
                
        if(Max!=idx):
            arr[Max],arr[idx] = arr[idx],arr[Max]
            self.maxHeapify(arr,n,Max)
    
    def buildMaxHeap(self,arr, n):
        for i in range((n//2)-1,-1,-1):
            self.maxHeapify(arr,n,i)
    
    def mergeHeaps(self, a, b, n, m):
        #your code here
        merged = []
        for i in a:
            merged.append(i)
            
        for j in b:
            merged.append(j)
        
        self.buildMaxHeap(merged,n+m)
        
        return merged

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def isMerged(arr1, arr2, merged):
    if (len(arr1) + len(arr2) != len(merged)):
        return False
    arr1 += arr2
    arr1.sort()
    mergedCopy = sorted(merged)
    if (arr1 != mergedCopy):
        return False
    for i in range(1, len(merged)):
        if merged[i] > merged[(i-1)//2]:
            return False

    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        copyA = a[:]
        copyB = b[:]
        obj = Solution()
        merged = obj.mergeHeaps(a, b, n, m)
        flag = isMerged(copyA, copyB, merged)
        print(0 if flag == False else 1)

# } Driver Code Ends