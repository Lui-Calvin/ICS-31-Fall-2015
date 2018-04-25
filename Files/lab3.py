#Calvin Lui 84152100 & Balpreet hehar 56124754 Lab section 8 assignment 3
#
#
#part C
#
#
print("----part C-----")
def abbreviate(S:str) -> str:
        return S[:3]
assert abbreviate('January') == 'Jan'
assert abbreviate('abril') == 'abr'
print('the abbreviation of december is', abbreviate('december'))
print('the abreviation of june is', abbreviate('june'))
print()
print()
def find_area_square(F:float)->float:
    return F*F
assert find_area_square(1) == 1
assert find_area_square(5) == 25
print('the square of 6 is',find_area_square(6))
print('the square of 9 is',find_area_square(9))
print()
print()

pi = 3.14159
def find_area_circle(f:float)->float:
    return f*f*pi

assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975
print('the area of a circle with a radius of 3 is',find_area_circle(3))
print('the area of a circle with a radius of 5 is',find_area_circle(5))
print()
print()

def print_even_numbers(l:list):
    for item in l:
        if item % 2 == 0:
            print(item)

print('the even numbers in list [2, 47, 31, 99, 20, 19, 23, 105, 710, 1004] are:')
print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004])
print()
print()

def calculate_shipping(f:float) -> float:
    price = 0
    if f < 2:
        price = 2.0
    else:
        if f < 10:
            price = 5.0
        else:
            price = 5.0 + (1.5 * (f-10))
    return price

assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50
assert calculate_shipping(2) == 5.00
assert calculate_shipping(10) == 5.00

print('the price of a package of weight 15 is', calculate_shipping(15))
print('the price of a package of weight 23 is', calculate_shipping(23))
print()
print()

import tkinter
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()

#creates a square inside the tkinter window
def create_square(x:float,y:float,length:float) -> None:
    my_canvas.create_rectangle(x,y,x+length,y+length)
create_square(100,100,100)
create_square(200,200,200)

#creates a circle in the tkinter window
def create_circle(x:float,y:float,radius:float)-> None:
    my_canvas.create_oval(x,y,x+radius*2,y+radius*2)
create_circle(100,100,50)
create_circle(200,200,100)

    
#
#
#part D
#
#
print("----part D----")
#d.1
print()
print()
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

def restaurant_price(R:Restaurant)-> float:
    return R.price

assert restaurant_price(RC[1]) == 5.5
assert restaurant_price(RC[0]) == 12.5
assert restaurant_price(RC[2]) == 25.5
#testing our restaurant_price function
print('the price of',RC[1].name+'\'s', 'best dish is', restaurant_price(RC[1]))
print('the price of',RC[2].name+'\'s', 'best dish is', restaurant_price(RC[2]))
print()
print()

RC.sort(key = restaurant_price)
print('restaurant list sorted by price:')
print(RC)

print()
print()
#reassigns RC to its original order
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
#printing list before running costliest function
print('before running costliest, our restaurant list is:')
print(RC)
print()

def costliest() -> str:
    RC.sort(key = restaurant_price)
    return RC[-1].name
assert costliest() == 'Noma'
#testing to see if costliest function works and is correct
print('the costliest restaurant is', costliest())
print()
#printing list after running costliest function to prove list has been reordered
print('after running costliest, our restaurant list is:')
print(RC)
print()
def costliest2() -> str:
    temp = sorted(RC,key = restaurant_price)
    return temp[-1].name
assert costliest2() == 'Noma'

#
#
#part e
#
#
print()
print('----part E----')
print()
print()
Book = namedtuple('Book', 'author title genre year price instock')
BSI = [Book('James Gordon','nightly adventures','science fiction',2003,13.50,12),
       Book('Calvin Harris','Batty man','romance comedy',1995,19.0,23),
       Book('Jeff young','woman in black','adventure',1999,9.0,0),
       Book('Matt Davis','Football','sports/ non-fiction',2014,30.0,33),
       Book('Lisa Simpson','Homer','comedy',2004,10.0,10),
       Book('Jake Jester','Life of an immigrant','Technology',2008,35.0,3)]
print('the list of book titles:')
for item in BSI:
      print(item.title)
print()
print()
print('the list of book titles in alphabetical order:')
def get_title(B:Book) -> str:
    return B.title
for item in sorted(BSI, key = get_title):
      print(item.title)

temp = BSI
BSI = []
for item in temp:
    BSI.append(Book(item.author,item.title,item.genre,item.year,item.price*1.1,item.instock))
print('BSI after price increase:')
print(BSI)
print()
print()

for item in BSI:
    if item.genre == 'Technology':
        print(item)
print()
print()
def book_stock(L:list) -> int:
        num_total_books = 0
        for item in L:
                num_total_books = num_total_books + item.instock
        return num_total_books
print('the total number of books is',book_stock(BSI))
    
before_year_2000 = []
after_year_2000 = []
for book in BSI:
        if book.year >= 2000:
                after_year_2000.append(book)
        else:
                before_year_2000.append(book)
print('More titles 2000 or later (',book_stock(after_year_2000),'vs.',book_stock(before_year_2000),')')

print()
print()
def inventory_value(B:Book) ->float:
        return B.price *B.instock
print(inventory_value(BSI[0]))

def top_value(l:list) ->Book:
        highest = BSI[0]
        for book in l:
                if inventory_value(book) > inventory_value(highest):
                        highest = book
        return highest
print("The highest-value book is", top_value(BSI).title, "at a value of $",inventory_value(top_value(BSI)))
print()
print()

second_window = tkinter.Tk()    # Create the graphics window
second_canvas = tkinter.Canvas(second_window, width=500, height=500)  # Create a 500x500 canvas to draw on
second_canvas.pack()  
def draw_eye(x,y) ->None:
        second_canvas.create_oval(x,y,x+100,y+100,fill='white')
        second_canvas.create_oval(x+25,y+25,x+75,y+75,fill = 'blue')
        second_canvas.create_oval(x+40,y+40,x+60,y+60,fill = 'black')
second_canvas.create_oval(1,1,499,499,fill='beige')
second_canvas.create_polygon(250,200,300,300,200,300)
second_canvas.create_polygon(125,350,375,350,300,400,250,405,200,400,fill ='white')

draw_eye(100,100)
draw_eye(300,100)
