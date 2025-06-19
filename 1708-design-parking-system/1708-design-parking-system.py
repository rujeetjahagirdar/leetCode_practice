class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.parking = {1: 0, 2: 0, 3: 0}

    def addCar(self, carType: int) -> bool:
        if(carType==1):
            if(self.parking[carType]<self.big):
                self.parking[carType]+=1
                return True
            else:
                return False
        if(carType==2):
            if(self.parking[carType]<self.medium):
                self.parking[carType]+=1
                return True
            else:
                return False
        if(carType==3):
            if(self.parking[carType]<self.small):
                self.parking[carType]+=1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)