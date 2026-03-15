class Fancy:

    def __init__(self):
        self.seq = []
        self.mod = 10**9 + 7
        # self.ops = []

        self.multiplier = 1
        self.adder = 0
        

    def append(self, val: int) -> None:
        # self.seq.append(val)
        # print("append: ", self.seq)
        
        val = (val - self.adder) % self.mod
        val = (val * pow(self.multiplier, -1, self.mod)) % self.mod
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        # self.ops.append(("add", len(self.seq), inc))

        # for i in range(len(self.seq)):
        #     self.seq[i] +=inc
        # print("add: ", self.ops)

        self.adder = (self.adder + inc) % self.mod

    def multAll(self, m: int) -> None:
        # self.ops.append(('mult', len(self.seq), m))

        # for i in range(len(self.seq)):
        #     self.seq[i] *=m
        # print("mult: ", self.ops)

        self.multiplier = (self.multiplier * m) % self.mod
        self.adder = (self.adder * m) % self.mod

    def getIndex(self, idx: int) -> int:
        # # ((x+2)*5)+3
        # if(idx<len(self.seq)):
        #     return self.seq[idx] % self.mod
        # return -1

        # if(idx<len(self.seq)):
        #     ans = self.seq[idx]
        #     if(self.ops):
        #         for op, i, x in self.ops:
        #             if(idx<i):
        #                 if(op=='add'):
        #                     ans = (ans+x) % self.mod
        #                 else:
        #                     ans = (ans*x) % self.mod
        #     return ans
        # else:
        #     return -1

        if(idx<len(self.seq)):
            ans = self.seq[idx]
            ans = ((ans * self.multiplier) + self.adder) % self.mod

            return ans
        return -1

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)