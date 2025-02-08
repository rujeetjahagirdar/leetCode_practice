class NumberContainers:

    def __init__(self):
        # self.numberToIndex = defaultdict(list)
        self.numberToIndex = defaultdict(SortedSet)
        self.indexToNumber = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if(index not in self.indexToNumber):
            self.indexToNumber[index] = number
            # self.numberToIndex[number].append(index)
            # heapq.heappush(self.numberToIndex[number], (index, number))
            # heapq.heappush(self.numberToIndex[number], (index))
            self.numberToIndex[number].add(index)
        else:
            self.numberToIndex[self.indexToNumber[index]].remove(index)
            # heapq.heapify(self.numberToIndex[self.indexToNumber[index]])
            if(len(self.numberToIndex[self.indexToNumber[index]])==0):
                del self.numberToIndex[self.indexToNumber[index]]
            self.indexToNumber[index] = number
            # self.numberToIndex[number].append(index)
            # heapq.heappush(self.numberToIndex[number], (index))
            self.numberToIndex[number].add(index)
        # print(self.numberToIndex)
        # print(self.indexToNumber)

    def find(self, number: int) -> int:
        if(number in self.numberToIndex):
            return self.numberToIndex[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)