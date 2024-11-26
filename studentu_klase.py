class Student():

    def __init__(self,name,student_id,grades):
        self.name = name
        self.student_id = student_id
        self.grades = []



    def calculate_average(self):
        return self.grades


    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Error: Atzīmei ir jābūt no 0 līdz 10.")


objekts1 = Student("Anna",5035,[4])

print(objekts1.grades)