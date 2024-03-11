class Node() :
    
    data : any = None
    prev : any = None
    next : any = None
    
    def __init__(self, data = None, prev = None, next = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next
        
    def setNext(self, node = None) : 
        if node is not None: self.next = node
        
    def setPrev(self, node = None) : 
        if node is not None: self.prev = node

class Queue() :
    
    __back__ : Node = None
    __front__ : Node = None
    __size__ : int = 0
    
    def __init__(self, data: list = None):
        self.__back__ = None
        self.__front__ = None
        self.__size__ = 0
        if data is not None:
            for d in data: self.push(d)
    
    def push(self, data) : 
        
        node : Node = Node(data)
        if self.__back__ is None :
            self.__back__ = node
            
        if self.__front__ is None :
            self.__front__ = node
        else:
            node.prev = self.__front__
            self.__front__.setNext(node)
            self.__front__ = node
            
        self.__size__+=1
        
    def pop(self) -> any:
        item = None
        if self.__size__ > 0 : 
            
            node = self.__back__
            item = node.data
            self.__back__ = node.next
            del(node)
            self.__size__-=1
            if self.__size__ == 1 : self.__front__ = self.__back__
            if self.__size__ == 0 : self.__front__ = None            
            
        return item
    
    def front(self) -> any:
        return self.__front__.data if self.__front__ else None
    
    def back(self) -> any:
        return self.__back__.data if self.__back__ else None
    
    def empty(self) -> any:
        return self.__size__ == 0
    
    def size(self) -> any:
        return self.__size__
    
    def __str__(self):
        items = []
        node = self.__back__
        while (node is not None):
            items.append(node.data)
            node = node.next
        return str(items)
    
if __name__ == '__main__':

    q = Queue([1,2,3,4,5])
    q.push(6)
    print(q.size())
    print(q.empty())
    print(q)