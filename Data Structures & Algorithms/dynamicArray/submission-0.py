class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity < 0:
            return "Error"
        self.capacity = capacity
        self.size = 0
        self.array = [0 for i in range(self.capacity)]


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity <= self.size:
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]
 

    def resize(self) -> None:
        temp = [0 for i in range(self.capacity)]
        self.capacity *= 2
        self.array = self.array + temp

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity