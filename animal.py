class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("동물의 울음소리")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("멍멍")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("야옹")
