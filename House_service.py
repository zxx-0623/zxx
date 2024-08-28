from House import *

class HouseService:
    houses=[]
    def __init__(self):
        house1=House(1, "tim", "118","海淀",800,"未出租")
        self.houses.append(house1)
        house2=House(2, "tom", "119","朝阳",900,"未出租")
        self.houses.append(house2)
        house3=House(3, "jim", "120","西城",1000,"未出租")
        self.houses.append(house3)
        
    def get_houses(self):
        return self.houses
