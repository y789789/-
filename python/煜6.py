class Student:
    def  __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文":0, "数学":0, "英语":0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

     def print_grades(self):
         print(f"学生{self.name} (学号：{self.student_id})的成绩为：")

chen = Student("小陈", "100618")
chen.set_grade("语文","92")
chen.set_grade("数学",94)
chen.print_grades()


#zeng = Student("小曾","100622")
#print(chen.name)
#zeng.set_grade("数学",95)
#print(zeng.grades)

