class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        
        # reference to the next node in the list
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        #set this nodes next_node refernece, to the passed in node
        self.next_node = new_next
    
            
class LinkedList:
    def __init__(self, node=None):
        #first node in the list
        self.end = node
        self.head = node
        self.next = None
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
        
    def add_to_end(self, value):
        #always needs to be wrapped in a node 
        new_node = Node(value)
        self.length += 1
        #is the list empty
        if not self.head:
            self.head = new_node
        #List is not empty
        else:
            #what node do we want to add the new node to
            #the last node in the list
            #traverse to the last node in the list
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            #the end of the list
            current.set_next(new_node)
    
    def remove_from_end(self):
        self.length -= 1
        if not self.head: 
            return None
        else:        
            second_last = None 
            current = self.head
            while current.get_next() is not None: 
                second_last = current 
                current = current.get_next()
        if second_last is not None:
            second_last.next_node = None
        else:
            self.head = None
        value = current.get_value() 
        return value
    
      
    def add_to_head(self, value):
        new_node = Node(value)
        self.length += 1
        if not self.head :
            self.head = new_node
            
        else:
            current = self.head
            current.get_next = new_node
            self.head = new_node
            
    def remove_from_head(self):
        #list is empty?
        if not self.head:
            return None
        #not empty
        else: 
            #we want to return the value at the current head
            value = self.head.get_value()
            #remove the value
            #update self.head
            
            self.head = self.head.get_next()
            return value
    
    def delete(self, node):
        self.length -= 1
    #if this is the only node
        if self.head is self.end:
            self.head = None
            self.end = None
        else: 
            
            self.head = node.next
            node.delete()  