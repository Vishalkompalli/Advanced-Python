
class Employee:
    raise_amount = 1.04 #Class Variable
    number_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.number_of_emps += 1

        '''Methods: These are functions associated with a class created to perform actions on instance data. 
           full_name method returns the full name of the employee'''

    def fullname(self):  
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amount) 
        '''or Employee.raise_amount. Just raise_amount doesn't work because Class variables need to be accessed via either the
          Class name or that specific instance name'''
        
    @classmethod # A Decorator
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    '''Created a class method. It takes Cls as the first argument just like how in a regular method, the same instance that 
    is created is passed as the first argument(self)'''   

emp_1 = Employee('Vishal', 'Kompalli', 1500000)
emp_2 = Employee('V', 'K', 1200000)

print(Employee.raise_amount)
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
