# ICS 31, Tuesday 13 October 2015, 11am

"""
Things/nouns/objects:  Data structures
Actions/verbs/functions,methods,operators:  Control structures
    Sequence
    Modularity (function calling)
    Selection (if statements)
    Repetition (loops and recursion)
        for-each:  Go through a sequence, item by item.
        for
        while
        recursion (ICS 32)

"""
'''
ducks = ['Huey', 'Dewey', 'Louie']
for item in ducks:
    print(item[0], 'is a hot duck.')
for d in ducks:
    print(d, 'is a hot duck.')
for IReallyReallyReallyLoveICS31 in ducks:
    print(IReallyReallyReallyLoveICS31, 'is a hot duck.')
for a_duck in ducks:
    print(a_duck, 'is a hot duck.')
print("That's it.")
"""
Syntax:
    for VARIABLE in SEQUENCE:
        STATEMENT(S)     # The BODY of the loop
Semantics:
    VARIABLE gets the value of the first item in SEQUENCE
    Execute the body of the loop with VARIABLE having that value.
    End of sequence?  Then go on to the next statement after the for.
    Otherwise, go back:
    VARIABLE gets the value of the SECOND item in SEQUENCE
    Execute the body with VARIABLE having that value.
    End of sequence?  Then go on.
    Otherwise, go back ...

"""

for duck_num in range(len(ducks)):
    print(duck_num, ".  ", ducks[duck_num])
for duck_num in range(len(ducks)):
    print(duck_num+1, ".  ", ducks[duck_num])
print()
for duck_num in range(len(ducks)):
    print(duck_num, ".  ", ducks[duck_num])
    print(duck_num+1, ".  ", ducks[duck_num])
"""
Syntax:  Same as above (where sequence is a range of numbers
Semantics:  Also same as above.


While-loop:  For indefinite repetition, until something becomes
    true or while somethine remains true.

    Syntax:
        while BOOLEAN-EXPRESSION:
            STATEMENT(S)            # BODY of loop
    Semantics:
        Test the B.E.  If it's false, skip body entirely.
        If true, do the body. Then go back.

One special pattern with while loops:  "N-and-a-half-times loop"
    while True:   # Essentially, "do forever" ... but wait.
        ... first part of body ...
        if BOOLEAN-EXPRESSION:
            break [or return]   # Ejector seat.  Quit the loop [function]
        ... rest of body ...
    Next statement

"""
'''

## RESTAURANT PROGRAM VERSION 1.
## Organization:  Model/View.  So we can adapt it to new platforms
##   without having to change the internal model of restaurants/lists.

def restaurants() -> None:
    ''' Main restaurants program:  Create and maintian a
        database of restaurants
    '''
    print("Welcome to the Restaurants Program")
    print()
    our_rests = []   # Here we might read the initial list in from a file
    our_rests = handle_commands(our_rests)
    # Here we would write our_rests out to a file.
    print()
    print("Thank you.  Good-bye.")
    return

def handle_commands0(RC: 'list of Restaurant') -> 'list of Restaurant':
    pass   # This is a PROGRAM STUB, a placeholder.

from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
def handle_commands1(RC: [Restaurant]) -> [Restaurant]:
    pass   # This is a PROGRAM STUB, a placeholder.

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
"""

def handle_commands2(RC: 'list of Restaurant') -> 'list of Restaurant':
    ''' Print menu, accept and execute commands to maintain list
    '''
    # This is a program stub, too; it doesn't do everything it's
    # eventually going to do.
    while True:
        command = input(MENU)
        if command == 'q':
            return RC
        else:
            print("You typed: ", command)
    return RC

def handle_commands3(RC: 'list of Restaurant') -> 'list of Restaurant':
    ''' Print menu, accept and execute commands to maintain list
    '''
    while True:
        command = input(MENU)
        if command == 'q':
            return RC
        else:
            if command == 'a':
                print("You want to add a restaurant")
            else:
                if command == 'r':
                    print("You want to remove a restaurant")
                else:
                    if command == 's':
                        print("You want to search for a restaurant")
                    else:
                        if command == 'p':
                            print("You want to display the restaurants")
                        else:
                            print("You typed: ", command)
    return RC

def handle_commands(RC: 'list of Restaurant') -> 'list of Restaurant':
    ''' Print menu, accept and execute commands to maintain list
    '''
    while True:
        command = input(MENU)
        if command == 'q':
            return RC
        elif command == 'a':
            print("You want to add a restaurant")
        elif command == 'r':
            print("You want to remove a restaurant")
        elif command == 's':
            print("You want to search for a restaurant")
        elif command == 'p':
            print("You want to display the restaurants")
        else:
            print("You typed: ", command)
    return RC

restaurants()
