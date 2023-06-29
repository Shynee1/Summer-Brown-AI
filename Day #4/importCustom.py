from student import Course, Student

math = Course("Algebra II*", 4, 15, "Andrew Franz")
english = Course("English I", 3, 15, "Belson")
student = Student("Jack", 15)
math.enrollStudent(student)
english.enrollStudent(student)
print(student.getInfo())
print(student.inClass("English I"))