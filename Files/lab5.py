__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
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
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")))


#### COLLECTION
# A collection is a list of restaurants

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

#restaurants()
#Calvin Lui 84152100 & jasraj singh manjit singh kochhar 11471536
from collections import namedtuple
print("Calvin Lui 84152100 & jasraj singh manjit singh kochhar 11471536")
#print("----part c.1----")
Dish = namedtuple("Dish","name price calories")
d1 = Dish('Pad Thai',10.15,300)
d2 = Dish('Pizza',4.50,500)
d3 = Dish('Chicken Alfredo', 12.0, 550)
print()
print()
print('----part c.2----')
def Dish_str(D:Dish)-> str:
    '''returns a string that represens a dish'''
    return D.name + ' ($' + str(D.price) + '): ' + str(D.calories) + 'cal'
assert Dish_str(d1) == 'Pad Thai ($10.15): 300cal'
assert Dish_str(d2) == 'Pizza ($4.5): 500cal'
print('The dish string for d1 is ',Dish_str(d1) )
print('The dish string for d1 is ',Dish_str(d2) )
print()
print()
print('----part c.3----')
test_dish = Dish('Pad Thai',10.15,300)
def Dish_same(dx:Dish,dy:Dish) ->bool:
    '''compares two dishes and checks if name and calorie count are same'''
    if dx.name == dy.name:
        if dx.calories == dy.calories:
            return True
    return False
assert Dish_same(test_dish,d1)
print('d1 and a copy of d1 are run through Dish_same and returns:',Dish_same(test_dish,d1))
print('d1 and d2 are run through the Dish_same function and returns:',Dish_same(d2,d1))
print()
print()
print('---- c.4 ----')
def Dish_change_price(D:Dish, n_price:float)-> Dish:
    '''Changes the price of a Dish namedtuple'''
    D= D._replace(price= D.price*(1+(n_price/100)))
    return D
assert Dish_change_price(d1,20) == Dish(name='Pad Thai', price=12.18, calories=300)
print('d1 with a changed price of 20% is ',Dish_change_price(d1,20))
print()
print()
print('---- c.5----')
def Dish_is_cheap(D:Dish,N:float)->bool:
    '''Returns true or false if the dish is cheaper than the given price '''
    return D.price < N
assert Dish_is_cheap(d1,15.0)
assert not Dish_is_cheap(d1,5.0)
print('D1 is cheaper than $15: ',Dish_is_cheap(d1,15.0))
print('D2 is cheaper than $2: ',Dish_is_cheap(d1,2.0))
print()
print()
print('----part c.6----')
d4 = Dish('Paht Woon Sen',9.50,330)
d5 = Dish('Cheese Burger', 2.0,410)
DL = [d1,d2,d3,d4,d5]
print('length of DL is ',len(DL))
DL.sort()
print('DL sorted: ')
print(DL)
print()
print()
d6 = Dish('Noodles',3.50,270)
DL.append(d6)
print('DL with new Dish: ')
print(DL)
print()
print()
d7 = Dish('Fried rice', 5.0,250)
d8 = Dish('Soup',2.50,320)
d9 = Dish('Salad',4.0,100)
d10 = Dish('BBQ Chicken', 7.0,700)
DL2 = [d7,d8,d9,d10]
DL3 = []
DL3 += DL + DL2
print('DL3 with DL + DL2 is')
print(DL3)
print()
print()
def Dishlist_display(L:'list of Dish')->str:
    '''returns a string representation of a list of Dishes'''
    ret_str = ''
    for i in L:
        ret_str += Dish_str(i) + "\n"
    return ret_str
print('The string representation of DL3 is')
print(Dishlist_display(DL3))
print()
print()
print('----part c.7----')
def Dishlist_all_cheap(L:'list of Dish',n:float)->bool:
    '''checks if every dish in a list is cheaper than the given price'''
    for item in L:
        if not Dish_is_cheap(item,n):
            return False
    return True
assert Dishlist_all_cheap(DL3,100.0)
assert not Dishlist_all_cheap(DL3,1.0)
print('checking if dishes in DL3 are cheaper than $100: ', Dishlist_all_cheap(DL3,100.0))
print('checking if dishes in DL3 are cheaper than $1: ', Dishlist_all_cheap(DL3,1.0))
print()
print()
print('----part c.8----')
def Dishlist_change_price(L:'list of Dish',n:float)->'list of Dish':
    '''Returns a list of the given dishes but changed by the given percentage'''
    list_copy = L[:]
    for i in range(0,len(list_copy)):
        list_copy[i] = Dish_change_price(list_copy[i],n)
    return list_copy
print(Dishlist_change_price(DL3,20.0))
print()
print()
print('---- part c.9----')
def Dishlist_price(L:'list of dish')->'list of float':
    '''returns the prices of the dishes in a list '''
    prices = []
    for i in L:
        prices.append(i.price)
    return prices
assert Dishlist_price(DL3) == [2.0, 12.0, 10.15, 9.5, 4.5, 3.5, 5.0, 2.5, 4.0, 7.0]
print('prices in DL3: ',Dishlist_price(DL3))
print()
print()
print('----part c.10----')
def Dishlist_average(L:'list of Dish')-> float:
    '''takes the average of all the price'''
    sum = 0
    for i in Dishlist_price(L):
        sum += i
    return sum/len(L)
assert Dishlist_average(DL3) == 6.015
print(Dishlist_average(DL3))
print()
print()
print('----part c.11 ----')
def Dishlist_keep_cheap(L:'list of Dish',n:float)->'list of Dish':
    '''creates a list of dishes cheaper than a given price'''
    cheap_list = []
    for i in L:
        if Dish_is_cheap(i,n):
            cheap_list.append(i)
    return cheap_list
print('all the dishes in DL3 cheaper than 5 dollars are',Dishlist_keep_cheap(DL3,5.0))
print()
print()
print('----part c.12----')
d11= Dish('Noodle Bar', 5.6,420)
d12= Dish('French Toast', 6.8,440)
d13= Dish('Sandwhich', 7.2,560)
d14= Dish('Pasta', 10.0,600)
d15= Dish('Egg Roll', 3.6,250)
d16= Dish('Bacon&Cheese', 6.6,620)
d17= Dish('Mac&Cheese', 7.5,520)
d18= Dish('Veggy Burger',4.8,360)
d19= Dish('Hot Fries', 1.6,350)
d20= Dish('Butter Chicken', 9.6,680)
d21= Dish('Kabob', 6.6,520)
d22= Dish('Mashed patato',3.4,220)
d23= Dish('Turkey', 8.6,790)
d24= Dish('Bean Roll', 4.3,421)
d25= Dish('Chocolate Cake', 4.1,235)

DL4 =[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25]
def before_and_after()->None:
    number = eval(input('Hi!,please choose a percentage to change Dish prices by: '))
    print(Dishlist_display(DL4))
    print(Dishlist_display(Dishlist_change_price(DL4,number)))
before_and_after()

print()
print()
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])			
#print('---- e.1----')
r3 = Restaurant('Pascal','French','940-752-0107',[Dish('escargots',12.95,250),
                                                  Dish('poached salmon',18.50,550),
                                                  Dish('rackk of lamb',24.0,850),
                                                  Dish('marjolaine cake',8.50,950)])
print()
print()
print('----part e.2----')

def Restaurant_first_dish_name(R:Restaurant)->str:
    '''returns the name of the first dish on the menu'''
    return R.menu[0].name
assert Restaurant_first_dish_name(r1) == 'Mee Krob'
assert Restaurant_first_dish_name(r3) == 'escargots'
print('the first dish of r1 is ',Restaurant_first_dish_name(r1))
print('the first dish of r3 is ',Restaurant_first_dish_name(r3))
print()
print()
print('----part e.3----')
def Restaurant_is_cheap(R:Restaurant,n:float)->bool:
    '''returns true of the average price of the
    restaurant's menu item is less than the given number'''
    average = Dishlist_average(R.menu)
    return average < n
assert Restaurant_is_cheap(r1,15)
assert not Restaurant_is_cheap(r1,5)
print('the average price of the menu items of r1 is cheaper than 15: ',Restaurant_is_cheap(r1,15))
print('the average price of the menu items of r1 is cheaper than 5: ',Restaurant_is_cheap(r1,5))
print()
print()
print('----part e.4----')
RL = [r1,r2,r3]
import copy
def Collection_raise_price(L:'list of Restaurant')->'list of Restaurant':
    '''raise the prices of every dish at every restaurant by 2.50'''
    copy_list = copy.deepcopy(L)
    for R in copy_list:
        for D in range(0,len(R.menu)):
            R.menu[D] = R.menu[D]._replace(price = R.menu[D].price + 2.5)
    return copy_list
print('The original RL is:')
print(RL)
print()
print()
print('The RL after Collection_raise_price is')
print(Collection_raise_price(RL))
print()
print()

def Collection_change_price(L:'list of Restaurant',N:float)->'list of Restaurant':
    '''raise the prices of every dish at every restaurant by the given perce'''
    copy_list = copy.deepcopy(L)
    for x in range(0,len(copy_list)):
        copy_list[x] = copy_list[x]._replace(menu = Dishlist_change_price(copy_list[x].menu,N))
    return copy_list
print(Collection_change_price(RL,20))

print()
print()
print('----part G----')
Count = namedtuple('Count','letter number')
def letter_count(message:str,characters:str)-> 'list of Count':
    list_counts = []
    for c in characters:
        list_counts.append(Count(c,message.count(c)))
    return list_counts
print(letter_count('i heart bad bitches','swag'))
