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

failed_students = list(filter(lambda student: student.score < 70, students))
print(failed_students)

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

def m_students():
	filtered_students = list(filter(lambda student: student.name.startswith("C"), students))
	return filtered_students

print(m_students())