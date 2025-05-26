class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.flatten = []
        self.pointer = -1
        for i in vec:
            for j in i:
                self.flatten.append(j)
                

    def next(self) -> int:
        if(self.hasNext):
            self.pointer+=1
            return self.flatten[self.pointer]

    def hasNext(self) -> bool:
        if(self.pointer+1 < len(self.flatten)):
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()