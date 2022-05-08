class Solution:
    def nthItem(self, L1, L2, A, B, N):
        # code here
        
            
            
        mulArr = L1*L2
        newArr = {}

        for i in range(L1):
            for j in range(L2):
                temp = A[i]+B[j]
                if(temp not in newArr):
                    newArr[temp] = 1
                
        ans = list(newArr.keys())
        ans.sort()
        #print(newArr)
        
        #print(newArr)
        try:
            
            return ans[N-1]
            
        except:
            return -1