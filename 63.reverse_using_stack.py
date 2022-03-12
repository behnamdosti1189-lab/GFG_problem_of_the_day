'''
Reverse a string using Stack 

You are given a string S, the task is to reverse the string using stack.

https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1
'''

#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    stack = []
    for i in S:
        stack.append(i)
    n = len(stack)
    res=''
    while(n>0):
        res+=stack.pop()
        n-=1
    return res
    #Add code here

#{
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends