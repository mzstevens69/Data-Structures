import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from linked_list import LinkedList
  
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def len(self):
#         return len(self.storage)

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop(-1)

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def len(self):
        return len(self.storage)

    def push(self, value):
        self.storage.add_to_end(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        
        else: 
            self.size -= 1
            return self.storage.remove_from_end()

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()

#     def push(self, value):
        
#             self.size += 1
#             self.storage.add_to_tail(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else: 
#             self.size -= 1
#             return self.storage.remove_from_tail()

#     def len(self):
#         return len(self.storage)
