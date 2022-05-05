# Partition a number into two divisible parts 

# Given a number (as string) and two integers a and b, divide the string in two non-empty parts such that the first part is divisible by a and the second part is divisible by b. In case multiple answers exist, return the string such that the first non-empty part has minimum length.

# https://practice.geeksforgeeks.org/problems/partition-a-number-into-two-divisible-parts3605/1#

class MyStack:

    def __init__(self):
        self.arr=[]
        self.size=0

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.size+=1

    def pop(self) -> int:
        if(self.size>0):
            self.size-=1
            return self.arr.pop()
        else:
            return -1
        
    def top(self) -> int:
        if(self.size>0):
            return self.arr[-1]
        else:
            return -1
        
    def empty(self) -> bool:
        # print(self.size)
        if(self.size<=0):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()