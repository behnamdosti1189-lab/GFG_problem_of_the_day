'''
Maximum Winning score 

In an online game, N blocks are arranged in a hierarchical manner. All the blocks are connected together by a total of N-1 connections. Each block is given an ID from 1 to N. A block may be further connected to other blocks. Each block is also assigned a specific point value.

A player starts from Block 1. She must move forward from each block to a directly connected block until she reaches the final block, which has no further connection. When the player lands on a block, she collects the point value of that block. The players score is calculated as the product of point values that the player collects.
Find the maximum score a player can achieve.
Note: The answer can always be represented with 64 bits.

https://practice.geeksforgeeks.org/problems/4ead9c3991a3822f578309e2232bc5415ac35cb9/1#
'''

#User function Template for python3

#structure of class Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def findMaxScore(self, root):
        #code here
        if(root==None):
            return 1
        
        le = self.findMaxScore(root.left)
        ri = self.findMaxScore(root.right)
        
        return root.data*max(le,ri)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        print(ob.findMaxScore(root))

# } Driver Code Ends
