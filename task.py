class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_course = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def gv_a_rt(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in lector.courses_attached and 
        (course in self.courses_in_progress or course in self.finished_course)):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg()}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\n"
                f"Завершенные курсы: {self.finished_course}")
    
    def avg(self):
        return (round(sum(sum(i) for i in self.grades.values())/
                      sum(len(i) for i in self.grades.values()), 2))
    
    def __lt__(self, other):
        return self.avg() < other.avg()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg()}")
    
    def avg(self):
        return round(sum(sum(i) for i in self.grades.values())/sum(len (i) for i in self.grades.values()), 2)
    
    def __lt__(self, other):
        return self.avg() < other.avg()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
            (course in student.courses_in_progress or course in student.finished_course)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def __str__(self, name, surname):
        return (f"Имя: {name}\n"
                f"Фамилия: {surname}")
    

def avg_course_student(list, course):
    avg = []
    for student in list:
        if (isinstance(student, Student) and 
            (course in student.finished_course or course in student.courses_in_progress)):
            avg.append(sum(student.grades[course])/len(student.grades[course]))
        else:
            print("Ошибка") 
    return round(sum(avg)/len(avg), 2)


def avg_course_lector(list, course):
    avg = []
    for lector in list:
        if isinstance(lector, Lecturer) and course in lector.courses_attached:
            avg.append(sum(lector.grades[course])/len(lector.grades[course]))
        else:
            print("Ошибка")
    return round(sum(avg)/len(avg), 2)


student_n1 = Student("Оля", "Башурова", "ж")
student_n1.courses_in_progress.append("Git")
student_n1.add_courses("Python")

student_n2 = Student("Олег", "Орлов", "м")
student_n2.courses_in_progress.append("Python")
student_n2.add_courses("Git")

lector_n1 = Lecturer("Олег", "Булыгин")
lector_n1.courses_attached.append("Python")
lector_n2 = Lecturer("Максим", "Кучеров")
lector_n2.courses_attached.append("Python")
lector_n2.courses_attached.append("Git")

rew_n1 = Reviewer("Сергей", "Добрин")
rew_n1.courses_attached.append("Python")
rew_n1.courses_attached.append("Git")
rew_n2 = Reviewer("Никита", "Проценко")
rew_n1.courses_attached.append("Git")

student_n1.gv_a_rt(lector_n1, "Python", 10)
student_n1.gv_a_rt(lector_n2, "Python", 5)
student_n1.gv_a_rt(lector_n2, "Git", 7)
student_n2.gv_a_rt(lector_n1, "Python", 6)
student_n2.gv_a_rt(lector_n2, "Python", 10)
student_n2.gv_a_rt(lector_n2, "Git", 2)
print(lector_n1)
print()
print(lector_n2)
print()
print(f"Лектор {lector_n1.name} лучше чем лектор {lector_n2.name}? {lector_n1 > lector_n2}")
print()
print(f"Cредняя оценка за лекции всех лекторов в рамках курса 'Python': "
      f"{avg_course_lector([lector_n1, lector_n2], "Python")}")
print()

rew_n1.rate_hw(student_n1, "Python", 10)
rew_n1.rate_hw(student_n1, "Git", 7)
rew_n1.rate_hw(student_n2, "Python", 8)
rew_n1.rate_hw(student_n2, "Git", 9)
print(student_n1)
print()
print(student_n2)
print()
print(f"Студент {student_n1.name} лучше чем студент {student_n2.name}? {student_n1 > student_n2}")
print()
print(f"Средняя оценки за домашние задания по всем студентам в рамках курса 'Python': "
      f"{avg_course_student([student_n1, student_n2], "Python")}")