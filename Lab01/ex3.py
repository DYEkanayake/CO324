from ex1 import *

def load_course_registrations_dict(filename: str) -> List[Student]:
    
    #Dictionary of Student Objects
    studentDetails=dict()
    
    #To keep the read data of the line being read
    details=[]
   
    with open(filename) as f:
        for line in f:
            details= line.strip().split(",")
            #given_name=details[0],surname=details[1],registered_courses=details[2:len(details)]
            #key=(surname, given_name) i.e. key=(details[1],details[0])
           
           ## studentDetails[details[1],details[0]]=Student(details[0],details[1],details[2:len(details)])
             
            keyTuple=(details[1],details[0])
            studentDetails[keyTuple]=Student(details[0],details[1],details[2:len(details)])
 
    """ Returns a dictionary of Student objects read from filename"""
    return studentDetails
 
#print(load_course_registrations("data.txt")) 

print("Eg for searching by a key: key is ('Kariyawasam','Nimali') ")
print(load_course_registrations_dict("data.txt")['Kariyawasam','Nimali'])