class Array():
    """Class that replicates the List class from the Python Collection
    """
    
    _value_ : any = [None] * 1
    _size_ : int = 1
    _occupacy_ : int = 0
    
    def IndexOutOfBounds(self, index):
        raise Exception (f"Index out of bounds, requested index {index} while size is {self._occupacy_}.")
    
    def __init__(self, value : list = None):
        if value:
            if len(value) > self._size_ :
                self._size_ = len(value) + int(len(value)/2)
                
            self._value_ = [None] * self._size_
            for i in range(0, len(value)) : self._value_[i] = value[i]
            self._occupacy_ = len(value)
    
    def __delitem__(self, index) :        
        if index >= self._size_:
            self.IndexOutOfBounds(index)
        
        self._value_[index] = None        
        for i in range(index, self._occupacy_ - 1 ):
            self._value_[i] = self._value_[i+1]
        
        self._occupacy_ -= 1
        if self._occupacy_ <= (int(self._size_/2)) :
            self._size_ = self._occupacy_  + 1
            self._value_ = [self._value_[i] for i in range(0, self._occupacy_)]
        
    
    def __setitem__(self, index : int, item : any):
        
        if index >= self._size_:
            self.IndexOutOfBounds(index)
            
        self._occupacy_+=1
        self._value_[index] = item
    
    def __getitem__(self, index : int):
        if index >= self._occupacy_:
            self.IndexOutOfBounds(index)
        return self._value_[index]
    
    def get(self, index : int) :
        return self.__getitem__(index)
    
    def __len__(self) -> int:
        return self._occupacy_
    
    def _increaseSize_(self) :
        if self._occupacy_+1 >= self._size_:
            self._size_ = self._size_*2
            new_value = [None] * self._size_
            for i in range(0, self._occupacy_) : new_value[i] = self._value_[i]
            self._value_ = new_value
    
    def append(self, item):        
        self._increaseSize_()
        
        self._value_[self._occupacy_] = item
        self._occupacy_+=1
    
    def pop(self):
        if self._occupacy_ > 0 :
            item = self.get(self._occupacy_-1)
            self.__delitem__(self._occupacy_-1)
            return item
        else: return self.IndexOutOfBounds(0)
        
    def insert(self, index : int, item : any) :        
        if index >= self._occupacy_:            
            if self._value_[self._occupacy_] is not None:
                self.append(item)
            else:
                self._value_[self._occupacy_] = item
        else:            
            self._increaseSize_()
            displacedItems = [self._value_[i] for i in range(index, self._occupacy_)]
            for i in range(1, len(displacedItems)+1):
                self._value_[index + i] = displacedItems[i-1]
            self._value_[index] = item
    
    def indexOf(self, item) -> int:
        for idx, i in enumerate(self._value_):
            if i == item: return idx
        return -1
    
    def __contains__(self, key):
        for i in self._value_:
            if i == key: return True
        return False
        
if __name__ == '__main__':
    
    arr = Array([1,2,3,4,5])
    
    # Indexing has a Time Complexity O(1)
    arr[0] = 1
    
    # Insertion at index has a Time Complexity O(n)
    arr.insert(2,6)
    
    # Search by value has a time Complexity O(n)
    arr.indexOf(2)
    if 2 in arr : print(True)
    
    # Deleting has a Time Complexity O(n)
    del(arr[2])
    
    print("End of test")
    