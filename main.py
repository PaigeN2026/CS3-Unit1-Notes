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

print(" ")

# ** LISTS **
# ordered, mutable, sequences 
empty_list = list() # constructor
another_empty_list = []

class_roster = ["Bryce", "Finny", "Jackson", "Kevin", "Maia", "Natalie", "Paige"]
print(class_roster)
print(len(class_roster))

# Indexes start at 0 
first_item = class_roster[0]
print(first_item)

# Update an item in a list, access by index
class_roster[2] = "Jack"
print(class_roster)

print(" ")

# Sorting lists 
lottery_nums = [5,148, 12, 589, 1, 999, 32039458, 51]
print(sorted(lottery_nums))
print(sorted(lottery_nums, reverse=True))
print(lottery_nums) # sorted() does not modify OG list
# Sort IN PLACE -> modifies OG list
lottery_nums.sort()
print(lottery_nums)

print(" ")

class_roster.sort(reverse=True)
print(class_roster)

# List operations
class_roster.append("Alex")
class_roster.insert(0, "Zoie")
print(class_roster)
class_roster.remove("Zoie")
class_roster.pop() # remove last item
print(class_roster)

print(" ")

# Check if item exists in a list
print(13 in lottery_nums)
print(1 in lottery_nums)

print(" ")

# ** Tuples **
# ordered & immutable (can't change items)
# useful for "snapshot" of a row of data
student = ('Paige', 17, 'Post-AP Comp Sci', 4.0)
print(student)
# student[3] = 2.6 # CAN'T RE-ASSIGN ITEM!

print(" ")

# ** SETS **
# unsorted, stores other immutable types
# NO DUPLICATES allowed 
songs = {'Stranger', '3005', '7', '3', 'Mutt', 'Freeze', '3005'}
print(songs)
# sets can be used to de-duplicate list items
colors = ['red', 'pink', 'orange', 'yellow', 'blue', 'purple', 'pink']
print(set(colors))
# you CAN add/remove items
songs.add('Nobody New')
songs.add('Stranger') # duplicate value 
print(songs)
# look up set OPERATIONS to compare items between sets

print(" ")

# ** DICTIONARIES **
# mutable, but the KEYS can only be immutable types 
# { key: value } pairs. Keys must be UNIQUE
# unordered (no index, can't sort in place)
characters =  {'Aelin': 'assassin queen', 
               'Karate Kid': 'pupil',
               'Mr. Miyagi': 'sensei',
               'Phil Dunphy': 'dad',
               'Wall-E': 'trash robot', 
               'Princess Peach': 'damsel in distress',
               'Dexter': 'serial killer (justified?)',
               'Lara Jean': 'letter writer'
               }
print(len(characters))
# disctionary with numerical keys, list valued
grade_requirements = { 9: ['Bio', 'Math', 'English', 'History', 'PE'],
                      10: ['Chem', 'Math', 'English', 'History', 'PE'],
                      11:['Physics', 'Math', 'English', 'History', 'PE'],
                      12: ['Math', 'English', 'PE']
                      }

print(" ")

# Boolean Expressions: True or False
print(10 > 5) # True
print(5 > 10) # False
print(10 >= 10) # True
print(7 <= 5) # False
print(5 == 5) # True
print(5 != 5) # False
print('a' > 'b') # False
print('cat' < 'cot') # o is GREATER bc it comes LATER
print('T' == 't') # False (calse-sensitive)
print('T' < 't') # True, capital letters come first

print(" ")

# Checking equality vs. identity
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(list_a == list_b) # True, list contains same items 
print(list_a is list_b) # False, not the same object
# Typically only use "is" when comparing to None, True, False
boolean_a = True
print(boolean_a is True) # True
print(boolean_a is not False) # True

print(" ")

# Compound boolean operators: and, or, not
boolean_b = True
boolean_c = False
print(boolean_a and boolean_b) # True
print(boolean_b and boolean_c) # False
print(boolean_a or boolean_c) # True
print(boolean_a and (boolean_b or boolean_c)) # True 

print(" ")

# Conditionals/branching/selection
def can_drive(age):
    if (age  >= 17):
        print('You can get a license in NY state!')
    elif (age == 16):
        print('You cang get a permit in NY state. Take some lessons!')
    else: 
        print("Too young to drive.")
# Test out function with different values
can_drive(18)
can_drive(16)
can_drive(13)

print(" ")

# ITERATION (repetition)
# while loop: run until a condition is no longer True
max = 16
counter = 6
while (counter <= max):
    print (f'Count is {counter}')
    counter += 1

print(" ")

# for-in loop: iterates through a collection
print(class_roster)
for student in class_roster:
    print(student)

print(" ")

# for-in range 
# prints 0 until 3
for num in range(4):
    print(num)

print(" ")

# range(start, stop) -> not inclusive of stop
for num in range(1,6):
    print(num)

print(" ")

# range(start, stop, step)
for num in range(10, 51, 5):
    print(num)

# BTW, python has a help function
# help(range)

print(" ")

# enumerate() lets you loo[ through index AND items
# useful for LIST collections
for index, item in enumerate(class_roster):
    print(f'Item: {item} is at index {index}')

print(" ")

# use .items() on a dictionary to loop over keys AND values
for character, description in characters.items():
    print(f'{character} is a {description}')

# review: setting up a dictionary
word = {
    'red': '#FF0000',
    'green': '#008000',
    'blue': '#0000FF'

}