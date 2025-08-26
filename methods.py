class Animal:
    info = "This is an animal class."

    def __init__(self, name, age):
        print(Animal.info)
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old."

dog1 = Animal("Buddy", 3)
dog2 = Animal("Max", 5)
print(dog1.get_info())
print(dog2.get_info())

class Square:
    sides = 4

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * Square.sides

square = Square(5)
print(square.area())
print(square.perimeter())
