class Cat:
    info = "This is a cat class."

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        return "Meow!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

cat = Cat("Whiskers", 2)
print(cat.get_info())
print(cat.meow())

cat.food = "Fish"
print(cat.food)