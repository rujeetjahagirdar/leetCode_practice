class TwoSum:

    def __init__(self):
        self.numbers = []

    def add(self, number: int) -> None:
        bisect.insort_left(self.numbers, number)

    def find(self, value: int) -> bool:
        l, r = 0, len(self.numbers)-1

        while(l<r):
            sm = self.numbers[l]+self.numbers[r]
            if(sm<value):
                l+=1
            elif(sm>value):
                r-=1
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)