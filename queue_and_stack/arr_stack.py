class ArrStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def len(self):
        return len(self.storage)

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(-1)