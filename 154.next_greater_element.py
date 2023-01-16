class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stk = [arr[-1]]
        ans = [-1]
        for i in range(len(arr)-2,-1,-1):
            while(len(stk) and stk[-1]<arr[i]):
                stk.pop()
            if(len(stk)):
                ans.append(stk[-1])
            else:
                ans.append(-1)
            stk.append(arr[i])
        
        return ans[::-1]
