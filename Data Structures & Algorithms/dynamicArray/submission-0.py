class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.end = 0
        self.items = [None] * capacity


    def get(self, i: int) -> int:
        return self.items[i]

    def set(self, i: int, n: int) -> None:
        self.items[i] = n

    def pushback(self, n: int) -> None:
        if self.end >= self.capacity:
            self.resize()
        
        self.items[self.end] = n
        self.end += 1

    def popback(self) -> int:
        popped = self.items[(self.end-1)]
        self.items[(self.end-1)] = None
        self.end -= 1
        return popped
 
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_items = [None] * (self.capacity * 2)
        for i in range(0, self.end, 1):
            new_items[i] = self.items[i]
        self.items = new_items

    def getSize(self) -> int:
        return self.end
        
    
    def getCapacity(self) -> int:
        return self.capacity
