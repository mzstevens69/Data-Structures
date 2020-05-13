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
    def __init__(self):
        #first node in the list
        self.head = None
        
    def add_to_end(self, value):
        #always needs to be wrapped in a node 
        new_node = Node(value)
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
        