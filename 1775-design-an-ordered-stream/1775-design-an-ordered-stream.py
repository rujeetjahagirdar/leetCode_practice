class OrderedStream:

    def __init__(self, n: int):
        self.stream = [-1]*n
        self.n = n
        self.ptr=0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value

        ans= []
        
        while(self.ptr<self.n and self.stream[self.ptr]!=-1):
            ans.append(self.stream[self.ptr])
            self.ptr+=1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)