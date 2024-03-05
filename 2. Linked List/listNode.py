class Node:
    
    _data_ : any = None
    _next_ : any = None
    _prev_ : any = None
    
    def __init__(self, data, next : any = None, prev : any = None ) :
        self._data_ = data
        self._next_ = next
        self._prev_ = prev       
        
    def data(self):
        return self._data_

    def next(self):
        return self._next_
    
    def prev(self):
        return self._prev_
    
    def setData(self, data):
        self._data_ = data
    
    def setNext(self, node):
        self._next_ = node
    
    def setPrev(self, prev):
        self._prev_ = prev
