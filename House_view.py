from House_service import *
from Utility import *


class HouseView:
    house_service = HouseService()
    def update_house(self):
       update_id=int(input("请输入要修改的房屋id号(-1表示退出）："))
       if update_id==-1:
           print("放弃修改房屋信息".center(32,"="))
           return
       house=self.house_service.find_by_id(update_id)
       if not house:
           print("不存在该房屋信息".center(32,"=") )
           return

       house.name=Utility.read_str(f"姓名({house.name}):",house.name)
       house.phone=Utility.read_str(f"电话({house.phone}):",house.phone)
       house.address=Utility.read_str(f"地址({house.address}):",house.address)
       house.rent=Utility.read_str(f"租金({house.rent}):",house.rent)
       house.state=Utility.read_str(f"状态({house.state}):",house.state)

    def find_house(self):
        print("查找房屋信息".center(32, '='))
        find_id=int(input("请输入要查找房屋的ID："))
        house=self.house_service.find_by_id(find_id)
        if house:
            print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
            print(house)
        else:
            print(f"房屋id{find_id}信息不存在，查找失败")

    def exit_sys(self):
        key=Utility.read_confirm_select()
        if key == "y":
            return True
        else:
            return False


    def del_house(self):
        print("删除房屋信息".center(32, '='))
        del_id = int(input("请输入待删除的编号（-1放弃删除）："))
        if del_id == -1:
            print("放弃删除".center(32, '='))
            return

        choice = Utility.read_confirm_select()
        if choice == "y":
          if self.house_service.del_by_id(del_id):
              print("删除房屋信息成功".center(32, '='))
          else:
            print("房屋编号不存在，删除失败".center(32, '='))

        else:
          print("放弃删除".center(32, '='))

    def add_house(self):
        print("添加房屋".center(32, "="))
        name = input("姓名：")
        phone = input("电话： ")
        address = input("地址：")
        rent = int(input("租金："))
        state = input("状态：")
        new_house = House(0,name, phone, address, rent, state)
        self.house_service.add(new_house)

    def list_houses(self):
        print("房屋列表".center(60, "="))
        print("编号\t\t房主\t\t电话\t\t地址\t\t租金\t\t状态(未出租/已出租)")
        houses = self.house_service.get_houses()
        for house in houses:
            print(house)

        print("房屋列表显示完毕".center(60, "="))

    def main_menu(self):
        while True:
            print()
            print("房屋出租系统菜单".center(32, "="))
            print("\t\t\t1 新 增 房 源")
            print("\t\t\t2 查 找 房 屋")
            print("\t\t\t3 删 除 房 屋 信 息")
            print("\t\t\t4 修 改 房 屋 信 息")
            print("\t\t\t5 房 屋 列 表")
            print("\t\t\t6 退 出 系 统")
            choice = input("请选择功能(1-6): ")
            if choice in ['1', '2', '3', '4', '5', '6']:
                if choice == '1':
                    self.add_house()
                elif choice == '2':
                    self.find_house()
                elif choice == '3':
                    self.del_house()
                elif choice == '4':
                    self.update_house()
                elif choice == '5':
                    self.list_houses()
                elif choice == '6':
                    if self.exit_sys():
                     break
