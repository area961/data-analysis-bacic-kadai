class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Humanクラスのインスタンスを作成
person = Human("侍太郎", 31)

# printinfoメソッドを呼び出して属性を表示
person.printinfo()
