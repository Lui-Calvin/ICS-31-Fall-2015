#Calvin Lui 84152100 & Balpreet hehar 56124754 Lab section 9 assignment 4
print("Calvin Lui 84152100 lab section")
#
#
#part 1
#
#
print('----part 1----')
def test_number(i:int,s:str)->bool:
    if s == 'even':
        return i%2==0
    elif s == 'odd':
        return i%2!=0
    elif s == 'positive':
        return i >= 0
    elif s == 'negative':
        return i < 0

assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')
print('testing number to see if 30 is odd:',test_number(30,'odd'))
print('testing number to see if -1 is negative:',test_number(-1,'negative'))
print()
print()
print("----part 2----")
def display()->None:
    inp = str(input('please type in a word '))
    print('\n')
    for i in range(len(inp)):
        print(inp[i])
display()
print()
print()
print('----part 3----')
def square_list(l:list)->None:
    for i in l:
        print(i**2)
square_list([2, 3, 4, 10])
print()
print()
print('----part 4----')
def match_first_letter(s:str,l:list)->None:
    for i in l:
        if i[0] == s:
            print(i)
match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])
print()
print()
print('----part 5----')
def match_area_code(AC:list,TN:list)-> None:
    for area in AC:
        if len(area) == 3:
            for number in TN:
                if number[1:4] == area:
                    print(number)
match_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])
print()
print()
print('----part 6----')
def match_area_codes(AC:list,TN:list)->list:
    phone_numbers = []
    for area in AC:
        if len(area) == 3:
            for number in TN:
                if number[1:4] == area:
                    phone_numbers.append(number)
    return phone_numbers
assert match_area_codes(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234']) == ['(949)555-1234', '(714)824-1234']
print(match_area_codes(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234']))
print()
print()
print('----part d.1----')
def is_vowel(character:str)->bool:
    vowel_list = 'aeiou'
    if character in vowel_list:
        return True
    return False
assert is_vowel('a') == True
assert is_vowel('b') == False
print('checking if \'a\' is a vowel:',is_vowel('a'))
print('checking if \'c\' is a vowel:',is_vowel('c'))
print()
print()
print('----part d.2----')
def print_nonvowels(word:str)->None:
    for i in range(len(word)):
        if not is_vowel(word[i]):
            print(word[i])
print('printing nonvowels for hello')
print_nonvowels('hello')
print('printing nonvowels for anteater')
print_nonvowels('anteater')
print()
print()
print('----part d.3----')
def nonvowels(word:str)->str:
    ret_str = ''
    for i in range(len(word)):
        if not is_vowel(word[i]):
            ret_str = ret_str + word[i]
    return ret_str
assert nonvowels('hello') == 'hll'
assert nonvowels('anteater') == 'nttr'
assert nonvowels('calvin') == 'clvn'
print('all the nonvowels in \'hello\' are:', nonvowels('hello'))
print('all the nonvowels in \'bang\' are:', nonvowels('bang'))
print()
print()
print('----part d.4----')
def consonants(word:str)->str:
    cons = 'bcdfghjklmnpqrstvwxyz'
    ret_str = ''
    for i in range(len(word)):
        if word[i] in cons:
            ret_str = ret_str + word[i]
    return ret_str
assert consonants("bam!!!!!!!!!!!") == 'bm'
assert consonants("what sup?") == 'whtsp'
print('all consonants in \'hey buddy whatsup?\' is:',consonants('hey buddy whatsup?'))
print()
print()
print('----part d.5----')
def vowels(word:str)->str:
    ret_str = ''
    for i in range(len(word)):
        if is_vowel(word[i]):
            ret_str += word[i]
    return ret_str
def select_letters(str1:str,str2:str)-> str:
    if str1 == 'v':
        return vowels(str2)
    elif str1 == 'c':
        return consonants(str2)
    else:
        return ""
assert select_letters('c',"california") == 'clfrn'
assert select_letters('v',"california") == 'aioia'
print('if we select all the consonants out of \'new york\' we would have',select_letters('c','new york'))
print('if we select all the vowels out of \'new york\' we would have',select_letters('v','new york'))
print()
print()
print('----part d.6----')
def hide_vowels(word:str)->str:
    ret_str = ''
    for i in range(len(word)):
        if is_vowel(word[i]):
            ret_str += '-'
        else:
            ret_str += word[i]
    return ret_str
assert hide_vowels('banana')== 'b-n-n-'
assert hide_vowels('watermelon') == 'w-t-rm-l-n'
print('hiding vowels in \'grapefruit\'',hide_vowels('grapefruit'))
print('hiding vowels in \'orange county\'',hide_vowels('orange county'))
print()
print()
print('----part e----')
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
def Restaurant_change_price(R:Restaurant,number:float)->Restaurant:
    return Restaurant(R.name,R.cuisine,R.phone,R.dish, R.price + number)
a1 = Restaurant('beep','Thai','415-860-6678','pad thai', 5.0)
print(a1)
print('after running Restaurant_change_price:')
print(Restaurant_change_price(a1,2.0))
print()
print()
print('----part f----')
R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]
print()
print()
print('----part f.1----')

def R_toString(R:Restaurant) -> str:
    return 'Name:    ' + R.name + "\n" + \
           'Cuisine: ' + R.cuisine + "\n" + \
           'Phone:   ' + R.phone + "\n" + \
           'Dish:    ' + R.dish + "\n" + \
           'price    ' + str(R.price) + "\n\n"
def restaurant_name(R:Restaurant)->str:
    return R.name
assert restaurant_name(R1) == 'Taillevent'

def alphabetical(L:'list of Restaurant') -> 'list of Restaurant':
    return sorted(L,key = restaurant_name)
assert alphabetical([Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75),Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50)]) == [Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50),Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)]
print('list of restaurants in alphabetical order')

for i in alphabetical(RL):
    print( R_toString(i))
print()
print()
print('----part f.2----')

def alphabetical_names(L:'list of Restaurant')-> 'list of str':
    names = []
    for i in alphabetical(L):
        names.append(i.name)
    return names

assert alphabetical_names([Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75),Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50)]) == ['Addis Ababa', 'Burger King']
print('the list of restaurant names in alphabetical order is: \n')
print(alphabetical_names(RL))      
print()
print()
print('----part f.3----')
#to be used in asserts
list_for_testing = [Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75),Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)]
def all_Thai(L:'list of Restaurant')-> 'list of Restaurant':
    Thai_list = []
    for R in L:
        if R.cuisine == "Thai":
            Thai_list.append(R)
    return Thai_list
assert all_Thai(list_for_testing) == [Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)]
print('all the Thai restaurants in RL are: \n')
for R in all_Thai(RL):
    print(R_toString(R))
print()
print()
print('----part f.4----')
def select_cuisine(L:'list of Restaurant', S:str) -> 'list of Restaurant':
    R_list = []
    for R in L:
        if R.cuisine == S:
            R_list.append(R)
    return R_list
assert select_cuisine(list_for_testing,"Burgers") == [Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)]
print('in our restaurant list, if we look for burgers using select_cuisine, we find: \n')
for i in select_cuisine(RL,"Burgers"):
    print(R_toString(i))

print()
print()
print('----part f.5----')
def select_cheaper(L:'list of Restaurant', number: float) -> 'list of Restaurant':
    cheaper_list = []
    for R in L:
        if R.price < number:
            cheaper_list.append(R)
    return cheaper_list
assert select_cheaper(list_for_testing,9.0) == [Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)]
print('all restaurants with cuisine cheaper than 4 dollars are: ')
for i in select_cheaper(RL,4.0):
    print(R_toString(i))
print()
print()
print('----part f.6----')
def average_price(L:'list of Restaurant')-> float:
    price_sum = 0
    for item in L:
        price_sum += item.price
    return price_sum/len(L)
assert average_price(list_for_testing) == 7.35
print('the average price for all restaurants in RL is')
print(average_price(RL))
print()
print()
print('----part f.7----')
print('the average price of indian food in RL is')
print(average_price(select_cuisine(RL,"Indian")))
print()
print()
print('----part f.8----')
print('the average price of chinese and thai food in RL is')
print(average_price(select_cuisine(RL,"Chinese")+select_cuisine(RL,"Thai")))
print()
print()
print('----part f.9----')
print('restaurants with dishes cheaper than 15$ are: ')
for item in select_cheaper(RL,15.0):
    print(R_toString(item))
print()
print()
print('----part g----')
import tkinter
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()
def create_rectangle_from_center(x:float,y:float,height:float,width:float)-> None:
    my_canvas.create_rectangle(x-width/2,y-height/2,x+width/2,y+height/2)
    return 
create_rectangle_from_center(250,250,100,100)
tkinter.mainloop()
