class LinkedList:
    
    def __init__(self):
        self.nodes = []
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        return self.nodes[index]
        
    def insertHead(self, val: int) -> None:
        if self.length == 0:
            self.nodes.append(val)
        else:    
            new_nodes = [val] + self.nodes
            self.nodes = new_nodes
        
        self.length += 1


    def insertTail(self, val: int) -> None:
        self.nodes.append(val)
        print(self.nodes)
        self.length += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        if self.length == 1:
            self.nodes = []
        else:
            before = self.nodes[0:index]
            after = self.nodes[index+1:self.length]
            self.nodes = before + after

        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        return self.nodes
        
