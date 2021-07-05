from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Student:
    """A student's course registration details"""
    given_name: str
    surname: str
    registered_courses: List[str]


def load_course_registrations(filename: str) -> List[Student]:
    
    #List of Student Objects
    studentList=[]
    
    #To keep the read data of the line being read
    details=[] 
   
    with open(filename) as f:
        for line in f:
            details= line.strip().split(",")
            #given_name=details[0],surname=details[1],registered_courses=details[2:len(details)]
            studentList.append(Student(details[0],details[1],details[2:len(details)]))
             
    """ Returns a list of Student objects read from filename"""
    return studentList

print("For Q1")    
print(load_course_registrations("data.txt"))
print("\n")