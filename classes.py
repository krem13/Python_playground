class Dog:
    info = "This is a dog class."

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

dog = Dog("Buddy", 3)
print(dog.get_info())
print(dog.bark())

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
