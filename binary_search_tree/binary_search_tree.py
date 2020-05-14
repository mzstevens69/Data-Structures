import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from collections import deque

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        #if node value is less than go left
        if value < self.value:
            if self.left:
            #if empty put it there
                self.left.insert(value)
            else:
            # less than node put it left
                self.left = BinarySearchTree(value)
        elif self.right:
            self.right.insert(value)
        else:
            self.right = BinarySearchTree(value)
            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target): #recursion
        #when we start searching self will be the root
        #compare the target against self.root
        if target == self.value:
        # if target matches self value return true
            return True
        if target < self.value:
            #go left if left is a BST node
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            #go right if right is a BST node
            if not self.right:
                return False
            return self.right.contains(target)
        
      
        
        

    # Return the maximum value found in the tree
    def get_max(self):
        
        if self is not None:
            
            current_max = self
    
            while current_max.right is not None:
                
                current_max = current_max.right
                
            return current_max.value 
            
        
        
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, fn):
        fn(self.value)
    # no children it is the value
    #check each side for childeren
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #print left node
        if self.left:
            self.left.in_order_print(self.left)       
        # print current
        print(self.value)
        #right node
        if self.right:
            self.right.in_order_print(self.right)
            
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            print(current.value)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            print(current.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):        
        print(node.value)
        
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)
        
      
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        if self.right:
            self.right.post_order_dft(self.right)
        print(self.value)
        