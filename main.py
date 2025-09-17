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