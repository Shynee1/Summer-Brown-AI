class Course:
    def __init__(self, name, difficulty, maxStudents, teacher):
        self.name = name
        self.difficulty = difficulty
        self.maxStudents = maxStudents
        self.teacher = teacher
        self.students = []

    def enrollStudent(self, student):
        self.students.append(student)
        student.enroll(self)

    def removeStudent(self, student):
        self.students.remove(student)
        student.dropout(self)

    def isFull(self):
        return len(self.students) >= self.maxStudents
    
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = len(name) * 1234593 + age
        self.classes = []

    def enroll(self, course):
        self.classes.append(course.name)

    def dropout(self, course):
        self.classes.remove(course.name)

    def inClass(self, course):
        return course in self.classes
    
    def getInfo(self):
        return f"name: {self.name}, age: {self.age}, id: {self.id}, # of classes: {len(self.classes)}"
    
math = Course("Algebra II*", 4, 15, "Andrew Franz")
english = Course("English I", 3, 15, "Belson")
student = Student("Jack", 15)
math.enrollStudent(student)
english.enrollStudent(student)
print(student.getInfo())
print(student.inClass("English I"))