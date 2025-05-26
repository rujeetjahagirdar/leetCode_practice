class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.zipped_list = []
        max_length = max(len(v1), len(v2))
        self.pointer=-1

        for i in range(max_length):
            if(i<len(v1)):
                self.zipped_list.append(v1[i])
            if(i<len(v2)):
                self.zipped_list.append(v2[i])
        
        print(self.zipped_list)

    def next(self) -> int:
        self.pointer+=1
        return self.zipped_list[self.pointer]
        
    def hasNext(self) -> bool:
        if(self.pointer+1 < len(self.zipped_list)):
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())