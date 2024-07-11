class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_space = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if not self.parking_space[carType - 1]: return False
        self.parking_space[carType - 1] -= 1
        return True