from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import email_validator

class Student(BaseModel):
  name: str 
  default: str = "Default value"
  email: Optional[EmailStr] = None
  age: Optional[int] = None
  cgpa: Optional[float] = Field(None, ge=0.0, le=10.0, description="CGPA must be between 0.0 and 10.0")
  
new_student = {'name': 'John Doe'}

student = Student(**new_student)

print(student.name)
print(student)

neww_student = {'name': 'Jane Doe', 'age': 25}

neww_student_obj = Student(**neww_student)
print(neww_student_obj)

#coerce
neeww_student = {'name': 'Jane Doe', 'age': '25'}

neeww_student_obj = Student(**neeww_student)
print(neeww_student_obj)

#email validation

e_neeww_student = {'name': 'Jane Doe', 'age': '25', 'email': 'jane.doe@example.com', 'cgpa': 8} #or abc bhej du error aayega 

e_neeww_student_obj = Student(**e_neeww_student)
print(e_neeww_student_obj)

d_student = dict(e_neeww_student_obj)
print(d_student['age'])

student_json = e_neeww_student_obj.model_dump_json()
print(student_json)