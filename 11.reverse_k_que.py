'''
Reverse First K elements of Queue 

Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.

https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
'''

#User function Template for python3
'''
Function Arguments :
		@param  : q ( given queue to be used), k(Integer )
		@return : list, just reverse the first k elements of queue and return new queue
'''

#Function to reverse first k elements of a queue.
def modifyQueue(q,k):
    # code here
    stk = []
    que=[]
    ct=0
    for i in q:
        if(ct>=k):
            break
        stk.append(i)
        ct+=1
    
    #print(stk)
    while(len(stk)>0):
        tmp = stk.pop()
        que.append(tmp)
    
    #print(que)
    for i in range(k,len(q)):
        que.append(q[i])
        
    return que
    
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))

        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*modifyQueue(queue,k))
# } Driver Code Ends