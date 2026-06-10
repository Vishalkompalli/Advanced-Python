#Bro Code - Youtube
#https://github.com/CoreyMSchafer/code_snippets/tree/master/Exceptions


a = 10
b = 0

try: 
    c = a/b
except:
     ZeroDivisionError
     print("You cannot divide by zero")