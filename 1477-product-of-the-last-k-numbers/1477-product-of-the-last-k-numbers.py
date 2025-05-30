# class ProductOfNumbers:

#     def __init__(self):
#         self.stream = []
#         self.totalProduct = 1
#         self.prefixProduct = [1]

#     def add(self, num: int) -> None:
        
#         self.stream.append(num)
#         if(num==0):
#             self.totalProduct*=1
#             self.prefixProduct.append(self.prefixProduct[-1]*1)
#         else:
#             self.totalProduct*=num
#             self.prefixProduct.append(self.prefixProduct[-1]*num)
#         # print(self.stream)
#         # print(self.totalProduct)
#         # print(self.prefixProduct)

#     def getProduct(self, k: int) -> int:
#         if(0 in self.stream[-k:]):
#             return 0
#         else:
#             idx = (len(self.stream) - k)
#             return(self.totalProduct//self.prefixProduct[idx])
        


# # Your ProductOfNumbers object will be instantiated and called as such:
# # obj = ProductOfNumbers()
# # obj.add(num)
# # param_2 = obj.getProduct(k)
##############################
class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct = []
        self.runningProduct = 1

    def add(self, num: int) -> None:
        if(num==0):
            self.prefixProduct = []
            self.runningProduct = 1 
        else:
            self.runningProduct *=num
            self.prefixProduct.append(self.runningProduct)

    def getProduct(self, k: int) -> int:
        if(k>len(self.prefixProduct)):
            return 0
        elif(k==len(self.prefixProduct)):
            return self.prefixProduct[-1]
        else:
            return self.prefixProduct[-1]//self.prefixProduct[-(k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)