# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)
print('Calvin Lui 84152100 and Ryan Liu 73638562. ICS lab sec 9')
def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 e:  To erase all the restaurants from the collection
 c:  To change prices for the dishes served
 RM: open up the menu options for the Restaurant menu
 sc: Search for all restaurants that serve a specific dish
 sd: search for dishes with names that contain specific words
 q:  Quit
"""
R_MENU_SCREEN = """
Restaurant Menu options --- pick one
 m: add Dishes to your Restaurant menu
 q: quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response == 'e':
            C=Collection_new()
            print(Collection_str(C))
        elif response == 'c':
            number= eval(input("Enter the percentage you wanna change dish price with : "))
            print(number)
            for x in range(0,len(C)):
                C[x] = Restaurant_change_price(C[x],number)
        elif response == 'RM':
            ans = input('Which restaurant do you want to select?(Or type q to quit)')
            if ans != 'q':
                R = get_restaurant_by_name(C,ans)
                if R != -1:
                    C[R] = Restaurant(C[R].name,C[R].cuisine,C[R].phone,C[R].dish,C[R].price, C[R].menu + Menu_enter())
        elif response == 'sc':
            inp = input('which cuisine are you looking for?')
            for item in C:
                if item.cuisine == inp:
                    print("{}: the average price of all the items on the menu are {}".format(item.name,avg_price(item)))
        elif response == "sd":
            sd_inp = input('what do you want to search for in all the dishes?(or q to quit)')
            if sd_inp != "q":
                print("printing all Dishes with the string ",sd_inp,":")
                for R in C:
                    for D in R.menu:
                        if sd_inp in D.name:
                            print("{} serves {}".format(R.name,D.name))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)
def avg_price(R:Restaurant)-> float:
    '''returns the average price'''
    avg_p = 0
    for i in R.menu:
        avg_p += i.price
    if len(R.menu) > 0:  
        return avg_p / len(R.menu)
    return 0
def Restaurant_str(self: Restaurant) -> str:
    ''' to print the details of the restaurant'''
    avg_c = 0
    for i in self.menu:
        avg_c += i.calories
    if len(self.menu)>0:
        avg_c/= len(self.menu)
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n"+
        "The current Menu is: "+"\n"+
        Dishlist_display(self.menu)+"\n"+
        "Average price:{:6.2f}.  Average calories:{:6.1f}".format(avg_price(self),avg_c)
        )

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")),[])


#### COLLECTION
# A collection is a list of restaurants
def get_restaurant_by_name(C:list,s:str)->int:
    '''returns index of restaurant of specified name'''
    for R in range(0,len(C)):
        if C[R].name == s:
            return R
    return -1
def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
def Restaurant_change_price(R:Restaurant,n:float)-> Restaurant:
    '''return the given restaurant with n percentage change in price'''
    return Restaurant(R.name,R.cuisine,R.phone,R.dish,R.price * (1+(n/100.0)),R.menu)
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]
Dish = namedtuple("Dish","name price calories")
def Dish_str(D:Dish)-> str:
    '''returns a string that represens a dish'''
    return D.name + ' ($' + str(D.price) + '): ' + str(D.calories) + 'cal'
def Dishlist_display(L:'list of Dish')->str:
    '''returns a string representation of a list of Dishes'''
    ret_str = ''
    for i in L:
        ret_str += Dish_str(i) + "\n"
    return ret_str
def Dish_get_info()->Dish:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Dish(input('please enter the name of the Dish: '),
                float(input('please enter the price of the Dish: ')),
                float(input('please enter the calorie count of the Dish: ')))
    
def Menu_enter()->'list of Dish':
    '''asks the user if they want to enter dish or no'''
    ans = input('do you want to add a Dish?(yes or no): ')  
    result = []
    while ans == 'yes':
        result.append(Dish_get_info())
        ans = input('do you want to add another Dish?')
    return result
restaurants()
