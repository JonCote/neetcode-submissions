class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        for pair in self.hashMap:
            if pair[0] == key:
                pair[1] = value
                return

        self.hashMap.append([key, value])
        

    def get(self, key: int) -> int:
        for pair in self.hashMap:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        ind = -1
        for idx, pair in enumerate(self.hashMap):
            if pair[0] == key:
                ind = idx
                break

        if ind != -1:
            self.hashMap.pop(ind)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)