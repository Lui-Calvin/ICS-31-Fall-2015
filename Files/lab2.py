#Calvin Lui 84152100 & Benedict mbakogu 35091947 lab sec 2

#part c.1--------------------------------------------------------
print('How many hours?')
hours = int(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = int(input())
print('This many dollars per hour:$ ', rate)
print('Weekly salary:$ ', hours * rate)

#part c.2-----------------------------------------------------------
print('Hello.  What is your name?')
name = str(input())
print('hello, ',name)
print('It\'s nice to meet you.')
print('How old are you?')
age = int(input())
print('Next year you will be',age+1, 'years old.')
print('Good-bye!')

#part d------------------------------------------------------------
krone_per_euro = 7.46
krone_per_pound = 10.33
krone_per_dollar = 6.66
print('hello, what is the name of your business?')
business = str(input())
print('how many euros does', business, 'own?')
euroAmount = float(input())
print('how many pounds does', business, 'own?')
poundAmount = float(input())
print('how many dollars does', business, 'own?')
dollarAmount = float(input())
print('Copenhagen Chamber of Commerce')
print('Business name: ',business)
print(euroAmount,'euros is', euroAmount*krone_per_euro, 'krone')
print(poundAmount,'pounds is', poundAmount*krone_per_pound, 'krone')
print(dollarAmount,'dollar is', dollarAmount*krone_per_dollar, 'krone')
print('')
print('Total krone: ',(euroAmount*krone_per_euro)+(poundAmount*krone_per_pound)+(dollarAmount*krone_per_dollar))

#part e---------------------------------------------
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

print(still_another.title)
print('the price of',another.title,'is',another.price)
print('the average price of all three books is',(favorite.price + another.price + still_another.price)/3)
print(favorite.title,'was written before 1900:',favorite.year < 1900)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 26.00)
print('the current price of ', still_another.title,'is ',still_another.price)
temp_current_price = still_another.price
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, temp_current_price * 1.2)
print('the current price of ', still_another.title,'is ',still_another.price)

#part f-----------------------------------------------------------------------
Animal = namedtuple('Animal','name species age weight fav_food')
elephant = Animal('Jumbo','elephant',50,1000.0,'peanuts')
platypus = Animal('Perry','platypus',7,1.7,'shrimp')
print('an elephant is heavier than a platypus', elephant.weight > platypus.weight)

#part g.1--------------------------------------------------------------------
booklist = [favorite, another, still_another]
print('the first book is cheaper than the second book: ', booklist[0].price < booklist[1].price)

#part g.2-----------------------------------------------------------
print('the first book in the list is more recent than the last book in the list:',booklist[0].year > booklist[-1].year)

#part h-------------------------------------------------------------------
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
print('the name of the third restaurant is ',RC[2].name)
print('the first and fourth restaurant serve the same type of food: ',RC[0].cuisine == RC[3].cuisine)
print('the price of the best dish of the last restaurant is ',RC[-1].price)
RC = sorted(RC,key=lambda restaurant: restaurant.name)
print('the best dish of the last restaurant is ',RC[-1].dish)
newRC = [RC[0:2],RC[-1],RC[-2]]
print(newRC)

#part i-----------------------------------------------------------------------
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
#my_canvas.create_polygon(100,200,200,100,300,200,200,300,fill= 'white')
my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line
#drawing square below
my_canvas.create_line(100,100,300,100)
my_canvas.create_line(300,100,300,300)
my_canvas.create_line(300,300,100,300)
my_canvas.create_line(100,300,100,100)
#drawing diamond
my_canvas.create_line(100,200,200,100)
my_canvas.create_line(200,100,300,200)
my_canvas.create_line(300,200,200,300)
my_canvas.create_line(200,300,100,200)
#drawing house
my_canvas.create_polygon(200,300,150,350,250,350,fill = 'brown')
my_canvas.create_rectangle(150,350,250,425,fill = 'white')
my_canvas.create_rectangle(160,360,180,380,fill = 'blue')
my_canvas.create_line(170,360,170,380)
my_canvas.create_line(160,370,180,370)
my_canvas.create_rectangle(190,388,210,425,fill = 'brown')
#drawing eye
my_canvas.create_oval(1,1,100,100,fill = 'white')
my_canvas.create_oval(25,25,75,75,fill = 'blue')
my_canvas.create_oval(40,40,60,60,fill = 'black')


tkinter.mainloop()          # Combine all the elements and display the window
