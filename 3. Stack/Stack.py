class Node() :
    
    data : any = None
    prev : any = None
    
    def __init__(self, data = None, prev = None) -> None:
        self.data = data
        self.prev = prev

class Stack() :
    
    __front__ : Node = None
    __size__ : int = 0
    
    def __init__(self, data: list = None):
        self.__size__ = 0
        if data is not None:
            for d in data: self.push(d)
    
    def push(self, data) : 
        
        node : Node = Node(data, self.__front__)
        self.__front__ = node
        self.__size__+=1
        
    def pop(self) -> any:
        item = None
        if self.__size__ > 0 :
            node = self.__front__
            item = node.data
            self.__front__ = node.prev
            del(node)
            self.__size__-=1
            
        return item
    
    def top(self) -> any:
        return self.__front__.data if self.__front__ is not None else None
    
    def empty(self) -> any:
        return self.__size__ == 0
    
    def size(self) -> any:
        return self.__size__
    
    def __str__(self):
        items = []
        node = self.__front__
        while (node is not None):
            items.append(node.data)
            node = node.prev
        return str(items)
    
if __name__ == '__main__':
    
    s = Stack([1,2,3,4,5])
    s.push(6)
    print(s.size())
    print(s.empty())
    print(s)