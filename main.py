print("hello world")

# Variables store data 
lucky_num = 9 # int
my_name = "Paige" # str 
cash = 1.27 # float 
is_raining = True # bool
is_sunny = False 

# CONCATENATE string literal + string variable
greeting = "Hello, " + my_name
print(greeting)
greeting = 'Hey it\'s me'
print(greeting)
greeting = """
           we were both young
           when i first saw you
           i close my eyes
           """
print(greeting)

# type() function tells you a variable'a data type
print(type(lucky_num)) # nested functions run from inner to outer 

# f-strings are FORMATTED  strings 
print(f"Hello, my name is {my_name}, and my lucky number is {lucky_num}")

# common error: str + number concatenation 
print(str(3) + "3")
print(3 + int("3"))

# the keyword DEF defines a new function 
def multiply(x, y):
    # function BODY
    result = x * y; 
    return result

# CALL function with arguments 
print(multiply(6, 7))
# OR, store output in variable 
math = multiply(12, 7)
print(math)

# void function does not return output
def greet(name):
    print(f"Hey there, {name}!!!")
greet("Natalie")
greet(3.14)