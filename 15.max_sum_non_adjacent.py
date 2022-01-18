'''
Maximum sum of Non-adjacent nodes 

Given a binary tree with a value associated with each node, we need to choose a subset of these nodes such that sum of chosen nodes is maximum under a constraint that no two chosen node in subset should be directly connected that is, if we have taken a node in our sum then we can’t take its any children or parents in consideration and vice versa.

https://practice.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/1#
'''

#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
  
    def max_sum(self, root):
        if not root:
            return 0, 0
  
        no_root_l, root_l = self.max_sum(root.left)
        no_root_r, root_r = self.max_sum(root.right)
  
        root_sum_max = max(root.data, root.data+no_root_l,
                           root.data+no_root_r, root.data+no_root_r+no_root_l)
        no_root_sum_max = max(root_l, root_r, root_l + root_r, no_root_l+no_root_r, 
                              root_l + no_root_r, root_r + no_root_l)
  
        return no_root_sum_max, root_sum_max
  
    def getMaxSum(self, root):
        return max(self.max_sum(root))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
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
    
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.getMaxSum(root))
        
# } Driver Code Ends