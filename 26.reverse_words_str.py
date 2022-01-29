'''
Reverse words in a given string 

Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
'''

# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        arr = S.split('.')
        #print(arr)
        
        i=0
        j=len(arr)-1
        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        
        res=''
        for i in arr:
            res+=i+'.'
        
        return res[:-1]

#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends