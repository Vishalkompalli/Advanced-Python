
class Employee:
    raise_amount = 1.04 #Class Variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        '''Methods: These are functions associated with a class created to perform actions on instance data. 
           full_name method returns the full name of the employee'''

    def fullname(self):  
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amount) 
        '''or Employee.raise_amount. Just raise_amount doesn't work because Class variables need to be accessed via either the
          Class name or that specific instance name'''
        

emp_1 = Employee('Vishal', 'Kompalli', 1500000)
emp_2 = Employee('V', 'K', 1200000)

# print(emp_1.pay) #->print the initial pay value for emp_1
# print(Employee.raise_amount) #->Print the raise_amount value for Employee Class - Class Variable
# emp_1.raise_amount = 2.0   #-> Update the raise_amount value only for emp_1
# print(emp_1.raise_amount) #->Print the newly update raise_amount value
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.__dict__)
# print(emp_2.__dict__)
print(Employee.__dict__)
