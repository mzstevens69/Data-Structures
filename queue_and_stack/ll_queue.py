from linked_list import LinkedList

class LLQueue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def len(self):
        return len(self.storage)
   

    def enqueue(self, value):
        self.storage.add_to_end(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        
        else: 
            self.size -= 1
            return self.storage.remove_from_head()