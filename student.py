# Python code​​​​​​‌‌‌​​​​​‌‌‌‌‌‌‌‌‌‌​​‌‌​​‌ below
# Use print("messages...") to debug your solution.

import json

class Student:

    thestr = """
    {
        "title":"Intermediate Python",
        "students": [
            {
                "name":"Nick",
                "scores": [
                    56,
                    73,
                    68,
                    84
                ]
            },
            {
                "name":"Jane",
                "scores": [
                    88,
                    74,
                    91,
                    73
                ]
            },
            {
                "name":"Mark",
                "scores": [
                    93,
                    66,
                    52,
                    33
                ]
            }
        ]
    }
    """
    json_course_data = json.loads(thestr)
    scores = [65,75,85,95]

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def get_scores():
        first_test_scores = []
        return first_test_scores

student1 = Student()
print(student1.average_score())
	