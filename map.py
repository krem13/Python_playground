class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_info(self):
        return f"Name: {self.name}, Score: {self.score}"

students = [
    Student("Alice", 85),
    Student("Bob", 92),
    Student("John", 69),
    Student("Helly", 58),
    Student("Charlie", 78)
]

students_result = []
for student in students:
    if student.score >= 70:
        students_result.append(f"Name: {student.name} Passed")
    else :
        students_result.append(f"Name: {student.name} Failed")

print(students_result)

map_students = list(map(lambda student: f"Name: {student.name} Passed" if student.score >= 70 else f"Name: {student.name} Failed", students))
print(map_students)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x*2, numbers))
print(squared_numbers)
