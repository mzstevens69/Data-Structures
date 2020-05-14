import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
     
     #insert is not returning anything so returns none Recursion Insert   
    def insert(self,value):
        #check if the incoming value is less than the current node's value
        if value < self.value:
            #we know we need to go left
            #how do we need to know when to recurse again or when to stop.
            if not self.left:
                #we can park our value here
                self.left = BSTNode(value)
            else:
                #we cant park here keep searching
                self.left.insert(value)
        else:
            #we know we need to go right 
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    
    def contains(self, target):
        pass
    
    def get_max(self):
        # need to always go right till no more right.
        if not self.right:
            return self.value
       #otherwise keep going right 
        return self.right.get_max()
        
    def for_each(self, fn):
        #call the fn of the value at this node
        fn(self.value)       
        #pass it to the left 
        if self.left:
            self.left.for_each(fn)
        #pass it to the right
        if self.right:
            self.right.for_each(fn)
# similiar to traversing a linked list iteratively          
    def iterative_max(self):
        current_max = self.value
        
        current = self
        
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            current = current.right
            
        return current_max
#depth first traversal of the tree   
    def iterative_for_each(self, fn):
        stack = []
    # add to root node   
        stack.append(self)
    # loop so long as it still has elements    
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        #call fn on the curr value
            fn(current.value)


# breadth first traversal

    def breadth_first(self, fn):
        q = deque()
    # add to root node   
        q.append(self)
    # loop so long as it still has elements    
        while len(q) > 0:
            current = q.popleft()
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            
        #call fn on the curr value
            fn(current.value)