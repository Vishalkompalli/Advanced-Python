
'''The __init__ Method: Think of this as an initializer or constructor. 
It automatically sets up attributes for each new instance when it is created'''

'''The self Argument: Every method within a class automatically receives the instance as the first argument, 
conventionally named self. 
This allows the method to access and modify the data of the specific instance being used'''

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        '''Methods: These are functions associated with a class created to perform actions on instance data. 
           full_name method returns the full name of the employee'''

    def fullname(self):  
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Vishal', 'Kompalli', 1500000)
emp_2 = Employee('V', 'K', 1200000)

print(emp_1.fullname()) # An attribute after the dot operator doesn't need parenthesis but a method needs parenthesis.
print(emp_2.fullname())