from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):

    name : str = 'srijan'  ## this means name must be strictly a string 
    age: Optional[int] = None  ## optinal values can be set or not it depends
    email: EmailStr

new_student = {} ## if we change srijan to 32 which is a integer it will throw an error.

# student = Student(**new_student)

# print(student)
# print(type(student))
# print(student.name)  ## we can also put default values and fetch it 
new_student = {'age':32 , 'email' : 'abc'}
# student = Student(**new_student)
print(new_student)