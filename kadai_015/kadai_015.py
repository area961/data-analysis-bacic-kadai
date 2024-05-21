class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Humanクラスのインスタンスを作成
person = Human("Alice", 30)

# printinfoメソッドを呼び出して属性を表示
person.print()
