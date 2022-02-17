'''
Corona Vaccine 

Geek has developed an effective vaccine for Corona virus and he wants each of the N houses in 
Geek Land to have access to it. Given a binary tree where each node represents a house in Geek Land, 
find the minimum number of houses that should be supplied with the vaccine kit if one vaccine kit is 
sufficient for that house, its parent house and it's immediate child nodes.  

https://practice.geeksforgeeks.org/problems/d1afdbd3d49e4e7e6f9d738606cd592f63e6b0f0/1

https://www.youtube.com/watch?v=fORHMo5yzNk
'''
#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    noVaccine=0
    
    def vaccine(self,root):
        if(root==None):
            return "OK"
        
        left=self.vaccine(root.left)
        right=self.vaccine(root.right)
        
        if(left=="WANT" or right=="WANT"):
            self.noVaccine+=1
            return "PROVIDE"
        elif(left=="PROVIDE" or right=="PROVIDE"):
            return "OK"
        
        return "WANT"
         
    def supplyVaccine(self, root):
        # Your code goes here
        
        if(self.vaccine(root)=="WANT"):
            self.noVaccine+=1
        
        return self.noVaccine
        


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
        ob = Solution()
        print(ob.supplyVaccine(root))
        
# } Driver Code Ends
