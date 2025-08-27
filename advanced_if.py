age = 10
height = 110

if age>=8 and height>=135:
    print("You are eligible for the ride!")

if age<8 or height<120:
    print("You are not eligible for any rides.")

if height<120:
    print("You are not tall enough for any rides.")
elif height>=120 and height<135:
    print("You are eligible for class 1 rides.")
elif height>=135 and height<200:
    print("You are eligible for all rides.")
else:
    print("You are too tall for any rides.")

if age<8 and height>120 or age>=8 and height<120:
    print("You can ride the children's rides.")