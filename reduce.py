class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [
    Student("Alice", 85),
    Student("Bob", 92),
    Student("John", 69),
    Student("Helly", 58),
    Student("Charlie", 78)
]

try:
    score_total = sum(student.score for student in students)
    score_average = score_total / len(students)
    print(score_average)
except ZeroDivisionError:
    print("No students available to calculate average.")

from functools import reduce

reduced_score_total = reduce(lambda acc, student: acc + student.score, students, 0)
print(reduced_score_total / len(students) if students else 0)

numbers = [1, 2, 3, 4, 5]
reduced_mult = reduce(lambda mult, x: mult * x, numbers)
print(reduced_mult)