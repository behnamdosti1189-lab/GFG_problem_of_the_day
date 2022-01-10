'''
Add 1 to a number represented as linked list 

A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1#
'''

#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self,head):
        cur = head
        prev = None
        while(cur):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev
    def addOne(self,head):
        #Returns new head of linked List.
        head = self.reverse(head)
        cur = head
        fg = 1
        while(cur.next):
            if(cur.data==9):
                cur.data=0
                cur=cur.next
            else:
                cur.data = cur.data+1
                fg=0
                break
        
        if(fg):
            if(cur.data==9):
                tmp = Node(1)
                cur.data=0
                cur.next=tmp
            else:
                cur.data = cur.data+1
        
        head = self.reverse(head)
        return head
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends