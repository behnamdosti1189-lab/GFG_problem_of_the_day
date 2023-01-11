class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        arr.sort()
        store = dict()
        for val in arr:
            if val in store:
                store[val]+=1
            else:
                store[val]=1
        
        ct=0 
        for i in range(len(arr)):
            if(arr[i] in store and store[arr[i]]>1):
                tmp = arr[i]
                while(tmp in store):
                    tmp+=1
                    ct+=1
                store[arr[i]]-=1
                # print(arr[i],tmp,ct)
                if(tmp in store):
                    store[tmp]+=1
                else:
                    store[tmp]=1
    
        return ct
