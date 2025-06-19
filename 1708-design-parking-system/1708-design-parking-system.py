class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = {1: big, 2: medium, 3: small}
        self.parking = {1: 0, 2: 0, 3: 0}

    def addCar(self, carType: int) -> bool:

        if(self.parking[carType]<self.space[carType]):
            self.parking[carType]+=1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)