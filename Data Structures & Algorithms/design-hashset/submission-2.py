class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        for k in self.hashSet:
            if k == key:
                return
        
        self.hashSet.append(key)
        

    def remove(self, key: int) -> None:
        found = False
        for k in self.hashSet:
            if k == key:
                found = True
        
        if found:
            self.hashSet.remove(key)
        

    def contains(self, key: int) -> bool:
        for k in self.hashSet:
            if k == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)