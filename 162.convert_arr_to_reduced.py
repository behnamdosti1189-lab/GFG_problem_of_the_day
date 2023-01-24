def convert(self,arr, n):
		# code here
		nums = arr[:]
		
		nums.sort()
        store = dict()
        ct = 0
        for i in nums:
            store[i] = ct
            ct+=1
        
        for i in range(len(arr)):
            arr[i] = store[arr[i]]
        
        return arr
