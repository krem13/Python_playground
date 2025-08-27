direction = input("Enter the direction (up, down, left, right): ")

match direction:
    case "up":
        print("You are moving north.")
    case "down":
        print("You are moving south.")
    case "left":
        print("You are moving west.")
    case "right":
        print("You are moving east.")
    case _:
        print("Invalid direction.")

age = int(input("Enter your age: "))

match age:
    case _ if age < 0:
        print("Invalid age.")
    case _ if age < 18:
        print("You are a minor.")
    case _ if age < 65:
        print("You are an adult.")
    case _:
        print("You are a senior.")