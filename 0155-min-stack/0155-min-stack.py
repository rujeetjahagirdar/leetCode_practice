class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_heap = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.min_heap, val)

    def pop(self) -> None:
        val = self.stack.pop(-1)
        self.min_heap.remove(val)
        heapq.heapify(self.min_heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()