from ex1 import *

from dataclasses import asdict
from json import dumps
import json

s1 = Student("Saman","Silva",["CO324","CO321","CO325"])
dumps(asdict(s1))
print(dumps(asdict(s1)))

stud_list=[]
stud_list.append(s1)
stud_list.append(Student("Kamal","Perera",["CO324","CO323","CO325"]))
stud_list.append(Student("Amara","Peiris",["CO324","CO323","CO322"]))
stud_list.append(Student("Nayana","Silva",["CO324","CO323","CO321"]))


st_list=map(asdict,stud_list)
print("\nFor Q4 part(c)")
print(list(st_list))


with open("student_registrations.json","w") as write_file:
    json.dump(list(map(asdict,stud_list)),write_file)

   
    