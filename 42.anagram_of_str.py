'''
Anagram of String 

Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.

https://practice.geeksforgeeks.org/problems/anagram-of-string/1#
'''

# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    
    #add code here
    if(len(str1)>len(str2)):
        val=str1
        val2=str2
    else:
        val=str2
        val2=str1

    store=dict()
    for i in val:    
        if i in store:
            store[i]+=1
        else:
            store[i]=1
    
    #print(store)
    ct=0
    for i in val2:
        if i in store and store[i]>0:
            store[i]-=1
        else:
            ct+=1
    
    #print(store)
    
    for key,val in store.items():
        ct+=val
    
    return ct

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends