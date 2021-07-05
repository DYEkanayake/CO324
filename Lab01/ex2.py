from ex1 import *

student_list=load_course_registrations("data.txt")

x=(sorted(student_list, key = lambda s: s.surname + s.given_name))

print("\n")
print("Sorted by surname and given_name")
print(x)
print("\n")

y=(sorted(student_list, key = lambda s: len(s.registered_courses)))

print("Sorted by number of courses students registered to")
print(y)
print("\n")