class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        store = dict()
        for i in s:
            if i in store:
                store[i]+=1
            else:
                store[i]=1
            
        mini = 1E9
        ct_l = 0
        ct_o = 0
        keys = ['b','a','l','o','n']
        for key,val in store.items():
            if((val < mini) and (key in keys)):
                mini = val
            if(key=='l'):
                ct_l = val
            if(key=='o'):
                ct_o = val
        
        if(ct_l>=mini*2 and ct_o>=mini*2):
            return mini
        else:
            return min(ct_l//2,ct_o//2)
