from House_service import *

class HouseView:
    house_service = HouseService()
    def list_houses(self):
        print("房屋列表".center(60,"="))
        print("编号\t\t房主\t\t电话\t\t地址\t\t租金\t\t状态(未出租/已出租)")
        houses=self.house_service.get_houses()
        for house in houses:
            print(house)

        print("房屋列表显示完毕".center(60,"="))
    def main_menu(self):
        while True:
            print()
            print("房屋出租系统菜单".center(32,"="))
            print("\t\t\t1 新 增 房 源")
            print("\t\t\t2 查 找 房 屋")
            print("\t\t\t3 删 除 房 屋 信 息")
            print("\t\t\t4 修 改 房 屋 信 息")   
            print("\t\t\t5 房 屋 列 表")
            print("\t\t\t6 退 出 系 统")
            choice = input("请选择功能(1-6): ")
            if choice in ['1', '2', '3', '4', '5', '6']:
                if choice=='1':
                    self.add_house()
                elif choice=='2':
                    self.find_house()
                elif choice=='3':
                    self.delete_house()
                elif choice=='4':
                    self.update_house()
                elif choice=='5':
                    self.list_houses()
                elif choice=='6':
                    break