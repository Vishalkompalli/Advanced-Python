'''Classes allow developers to logically group attributes (data) and methods (functions), 
making code easier to manage, reuse, and extend '''
class Employee:
    pass

emp_1 = Employee() #Creating instances of the Employee class
emp_2 = Employee()

# print(emp_1)
# print(emp_2)

'''Manually creating instance variables and assigning them values'''
emp_1.first = 'Vishal' # type: ignore
emp_1.last = 'Kompalli' # type: ignore
emp_1.email = 'Vishal.kompalli@email.com' # type: ignore
emp_1.pay = 1500000 # type: ignore

'''Similarly create for emp_2. emp_3 and so on....exhausting right?'''

print(emp_1.first) # type: ignore
print(emp_1.last) # type: ignore
print(emp_1.email) # type: ignore
print(emp_1.pay) # type: ignore

'''using the __init__() method we can automate the creation of instance variables'''
