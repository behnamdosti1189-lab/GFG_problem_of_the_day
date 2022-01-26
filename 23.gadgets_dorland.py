'''
Gadgets of Doraland 

In Doraland, people have unique Identity Numbers called D-id. Doraemon owns the most popular gadget shop in Doraland. Since his gadgets are in high demand and he has only K gadgets left he has decided to sell his gadgets to his most frequent customers only. N customers visit his shop and D-id of each customer is given in an array array[ ]. In case two or more people have visited his shop the same number of time he gives priority to the customer with higher D-id. Find the D-ids of people he sells his K gadgets to.

https://practice.geeksforgeeks.org/problems/bbd15e2da95880979ce65acc7360e2c5681664e65520/1#
'''

#User function Template for python3

class Solution:
    def TopK(self, array, k):
        # code here
        store={}
        for i in array:
            if i in store:
                store[i]+=1
            else:
                store[i]=1
        sorted_store = sorted(store.items(),key=lambda x:(x[1],x[0]),reverse=True)
        #print(sorted_store)
        res=[]
        
        for i in range(k):
            res.append(sorted_store[i][0])
            
        
        return res
        
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        res = obj.TopK(array, k)
        for each in res:
            print(each, end=' ')
        print()

# } Driver Code Ends