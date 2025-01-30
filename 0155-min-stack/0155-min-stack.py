class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minstack, val)
        

    def pop(self) -> None:
        self.minstack.remove(self.stack[-1])
        heapq.heapify(self.minstack)
        self.stack.pop(-1)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()