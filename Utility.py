class Utility:
    @staticmethod
    def read_str(tip,default_val):
        #读取用户的输入，如果没有输入内容，则返回default_val
        #:param tip: 提示信息
        #:param default_val: 用户指定
        #:return: 返回的就是需要的新数据

        str=input(tip)
        if len(str) > 0:
            return str
        else:
            return default_val

    @staticmethod
    def read_confirm_select():
        print("请输入你的选择(Y/N):", end="")
        while True:
            key = input()
            if key.lower() == 'y' or key.lower() == 'n':
                break
            else:
                print("输入的不是Y/N,请重新输入", end="")
        return key.lower()
