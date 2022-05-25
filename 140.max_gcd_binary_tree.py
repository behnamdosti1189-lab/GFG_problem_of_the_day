# Maximum GCD of siblings of a binary tree 

# https://practice.geeksforgeeks.org/problems/maximum-gcd-of-siblings-of-a-binary-tree/1

class Solution:
    def maxBinTreeGCD(self, arr, N):
        # Contributed By: Mridul Bhaskar
        dict_ = {}
        res = 0
        if(N<=2):
            return res
        else:
            for i in range(0,len(arr),1):
                if(arr[i][0] not in dict_):
                    dict_[arr[i][0]] = arr[i][1]
                else:
                    temp = gcd(arr[i][1],dict_[arr[i][0]])
                    res = max(temp,res)
        return res