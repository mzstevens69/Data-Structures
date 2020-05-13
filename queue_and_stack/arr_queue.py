

class ArrQueue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def len(self):
        return len(self.storage) 


    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)