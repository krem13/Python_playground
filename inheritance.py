class Animal:
    info = "This is an animal class."

    def __init__(self, name, age):
        print(Animal.info)
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old."

class Dog(Animal):
    info = "This is a dog instance."

    def __init__(self, name, age):
        super().__init__(name, age)
        print("A dog is created.")

    def bark(self):
        return "Woof!"

    def get_info(self):
        return super().get_info()

dog = Dog("Buddy", 3)
print(dog.bark())
print(dog.get_info())

class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        print("A cat is created.")

    def meow(self):
        return "Meow!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

cat = Cat("Whiskers", 2)
print(cat.meow())
print(cat.get_info())

cat.food = "Fish"
print(cat.food)

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Square(Shape):
    sides = 4

    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * Square.sides

square = Square(5)
print(square.area())
print(square.perimeter())
