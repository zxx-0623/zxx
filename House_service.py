from House import *


class HouseService:
    houses = []
    id_counter = 1

    def add(self, new_house:House):
        self.id_counter += 1
        new_house.id_counter = self.id_counter
        self.houses.append(new_house)

    def find_by_id(self, find_id):
        for house in self.houses:
            if house.id == find_id:
                return house

    def del_by_id(self, del_id):
        house = self.find_by_id(del_id)
        if house is None:
            return False
        self.houses.remove(house)
        return True

    def __init__(self):
        house1 = House(1, "tim", "118", "海淀", 800, "未出租")
        self.houses.append(house1)

    def get_houses(self):
        return self.houses
