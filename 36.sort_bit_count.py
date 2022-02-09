'''
Sort by Set Bit Count 

Given an array of integers, sort the array (in descending order) according to count of set bits in binary representation of array elements. 

Note: For integers having same number of set bits in their binary representation, sort according to their position in the original array i.e., a stable sort.

https://practice.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1#
'''

#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        return arr.sort(key=lambda x:bin(x).count('1'),reverse=True)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends