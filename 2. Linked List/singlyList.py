# Node import
from listNode import Node

class singlyList:
    
    _head_ : Node = None
    _size_ : int = 0
    
    def IndexOutOfBounds(self, index):
        raise Exception (f"Index out of bounds, requested index {index} while size is {self._occupacy_}.")
    
    def __init__(self, data : list = None) -> None:
        self._head_ = None
        self._size_ = 0
        if (data):
            for d in data:
                self.add(d)     
                
    def size(self) :
        return self._size_      
    
    def head(self):
         return self._head_
    
    def traverse(self, node : Node, index : int, h : int = None, data : any = None):
        if not node : return (node, index)
        if node.next() and (h != index) and (data != node.data()): 
            return self.traverse(node.next(), index + 1, h, data)
        else :
            return (node, index)
        
    def add(self, data): 
        node = Node(data, self._head_)
        self._head_ = node
        self._size_+=1
            
    def insert(self, index, data): 
        
        if index > self._size_ :  return self.append(data)
        if index == 0 : return self.add(data)

        prev = self.traverse(self._head_, 0, index - 1)[0]
        curr = self.traverse(self._head_, 0, index )[0]
        
        node = Node(data, curr)
        if prev is not None : prev.setNext(node)
        
        self._size_+=1        
    
    def append(self, data): 
        last = self.traverse(self._head_, 0)[0]
        node = Node(data,None)
        if last: last.setNext(node)
        if self._head_ is None: self._head_ = node
        self._size_+=1
    
    def removeHead(self) :
        if self._head_ is not None:
            next : Node = self._head_.next()
            del(self._head_)
            self._head_ = next            
    
    def deleteAt(self, index): 
        if index > self._size_: return self.IndexOutOfBounds(index)
        if index == 0 : return self.removeHead()
        
        prev = self.traverse(self._head_, 0, index -1 )[0]
        curr = self.traverse(self._head_, 0, index )[0]
        
        prev.setNext(curr.next())
        del(curr)
        
    def remove(self, data):
        res = self.traverse(self._head_, 0, None, data)
        if res[0].data() == data : self.deleteAt(res[1])
    
    def __contains__(self, data) -> bool :
        return self.traverse(self._head_, 0, None, data)[0].data()
    
    def __len__(self) -> int:
        return self._size_
     
    def __str__(self):
        if self._head_ is None : 
            return "Empty List"
        
        curr, str = self._head_, f"{self._head_.data()} --> "
        while(curr.next() is not None):
            curr = curr.next()
            str += f"{curr.data()}{' --> ' if curr.next() is not None else ''}"
        
        return str
    
    def getAt(self, index):
        if index > index : return self.IndexOutOfBounds()
        return self.traverse(self._head_, 0, index)[0]
    
    def indexOf(self, data):
        node = self.traverse(self._head_, 0, None, data )
        return node[1] if node[0].data() == data else -1  

if __name__ == '__main__':
    
    sl = singlyList()
    sl.insert(0,3)
    sl.add(1)
    sl.add(2)
    sl.add(4)
    sl.add(5)
    
    # Contains
    if 4 in sl : print(True)
    
    # Indexing has a Time Complexity O(1)
    sl.getAt(0)
    
    # Insertion at index has a Time Complexity O(n)
    sl.insert(3,10)
    
    # Search by value has a time Complexity O(n)
    print(sl.indexOf(2))
    
    print(sl)
    # Deleting has a Time Complexity O(n)
    sl.indexOf(11)
    print(sl)
    
    print("End of test")