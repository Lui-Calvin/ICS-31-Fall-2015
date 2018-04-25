# ICS 31, 1 October 2015, 11am

"""
Things (nouns):  In CS terms, OBJECTS
    int          float        str
    17          -3.141592653  "Hello there!"


Actions (verbs):  In CS, statements, operators, function calls, method calls
    Statements
        assignment statements        a = 17
    Function calls:  as below
    Operators:   + - * /   % (mod)     +  *

"""

print("Hello", "Good-bye")
print(float("3.9534") + 100)

"""
Things/nouns/objects:
    Single-valued data: int  float
                        bool [Boolean, from George Boole, True/False]
                        str
    Multiple-valued data:    str
        LISTS -- collection of items all the same type
                [ 88, 90, 92, 92, 95, 85, 88, 87 ]
                ["Huey", "Dewey", "Louie"]

        NAMEDTUPLES -- Package components into one multi-attribute item.
            A student might have a name (string), ID (int), GPA (float),
                Year of birth (int), major (string)
"""

student1 = ("Jones, John", 33334444, 3.45, 1996, "CS")
student2 = ("Smith, Sally", 11112222, 3.95, 1997, "CGS")

# Refer to individual items, in lists or tuples, by INDEXING

temps = [ 88, 90, 92, 92, 95, 85, 88, 87 ]
nephews = ["Huey", "Dewey", "Louie"]

print(temps, nephews)
print("The first temperature is", temps[0])
print("The third temperature is", temps[2])
#  Zero-based indexing:  Start counting at zero.
print("The name of the first student is", student1[0],
      "; that student's GPA is", student1[2])
print(temps[0:2])
print(student1[0:2])
print(temps[1:len(temps)])
print(temps[1:])
temps = temps + [100]
print(temps)
print(student1 + student2)
# print(temps + "Hello")
# NOT HOW WE'RE DOING IT:
print(temps + ["Hello"])
print(sum(temps))
from math import sqrt
print(sqrt(25))

## USING A NAMEDTUPLE

# Step 1:   Set it up (say this once at the top of the program)
from collections import namedtuple

# Step 2:  Define what your object looks like
# A student has a  name (string), ID (int), GPA (float),
#               Year of birth (int), major (string)
Student = namedtuple('Student', 'name ID GPA birth_year major')

# Step 3:  Create some objects of this new type:
s1 = Student("Jones, John", 33334444, 3.45, 1996, "CS")
s2 = Student("Smith, Sally", 11112222, 3.95, 1997, "CGS")
print(s1)

# Step 4:  Refer to the FIELDS/ATTRIBUTES as needed with dots:
print("The student", s1.name, "has a GPA of", s1.GPA,
      "in the major", s1.major)
