#Learning resources: Bro Code - Youtube
#https://github.com/CoreyMSchafer/code_snippets/tree/master/Exceptions

# Safe Division Calculator


a = int(input("Enter the first number "))
b = int(input("Enter the second number "))

try: 
    result = a/b
except:
     ZeroDivisionError
     print("Division by zero is undefined as per standard mathematics, dumbass")
else:
    print("The result of the operation is",int(result))

finally:
    pass