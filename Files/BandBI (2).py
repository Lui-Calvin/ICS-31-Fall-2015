#Nina Ye 79778836 and Ethan Nguyen 88422845. ICS 31 Lab sec 3. Lab asst 9.

def antbnb(s: str) -> str:
    """Main program. Takes in the input and prints the output"""
    file = open(s, "r")
    file_lines = file.readlines()
    bedrooms = Collection_new()
    reservations = Reservation_new()
    count = []
    for i in file_lines:
        line = i.strip()
        handle_commands(bedrooms, line, reservations, count)
    handle_commands(bedrooms, 'save', reservations, count)
    return

def handle_commands(C: list, r: str, R: list, count: list) -> None:
    """Accepts and processes commands"""
    line_split = r.split()
    response = line_split[0].upper()
    if response=="NB":
        C = add_bedroom(C, int(line_split[1]))
    elif response=="LB":
        list_bedrooms(C)
    elif response=="PL":
        print_line(r)
    elif response=="##":
        return
    elif response=="RB":
        C = remove_bedroom(C, int(line_split[1]), R)
    elif response=="NR":
        R = new_reservation(R, line_split, C, count)
    elif response=="LR":
        list_reservations(R)
    elif response=="RR":
        R = remove_reservation(R, int(line_split[1]))
    elif response=="BR":
        bedroom_res(R, int(line_split[1]))
    elif response=="RG":
        res_guest(R, " ".join(line_split[1:]))
    elif response=="LA":
        list_arrivals(R, line_split[1])
    elif response=="LD":
        list_departures(R, line_split[1])
    elif response=="LF":
        list_free_bed(C, R, line_split[1], line_split[2])
    elif response=="LO":
        list_occupied_bed(C, R, line_split[1], line_split[2])
    elif response=="SAVE":
        save(C, R)
    else:
        invalid_command(response)

def save(C:list, R:list):
    """Saves current data into given file name"""
    savef = open(y, "w")
    for i in C:
        savef.write('NB ' + str(i) + '\n')
    for k in R:
        savef.write("NR {} {}/{}/{} {}/{}/{} {}".format(k.bedroom_num, k.arrival.month, k.arrival.day, k.arrival.year, k.departure.month, k.departure.day, k.departure.year, k.name) + '\n')

def invalid_command(response):  
    """ Print message for invalid menu command."""
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")

def Collection_new() -> list:
    ''' Return a new, empty collection of bedrooms available'''
    return [ ]

def add_bedroom(C: list, n: int) -> list:
    """Adds a new bedroom to the list"""
    if n in C:
        print("Sorry, can't add room {} again; it's already on the list.".format(n))
        return C
    if n in range(1, 999):
        C.append(n)
    return C

def list_bedrooms(C:list) -> None:
    """Prints out the number of rooms currently available as well as the list of
    bedrooms currently available"""
    print("Number of bedrooms in service:", len(C))
    print("------------------------------------")
    CC = C[:]
    CC.sort()
    for b in CC:
        print(b)
    return

def print_line(s: str) -> None:
    """Prints out the inputted line"""
    print(s[3:])

def remove_bedroom(C: list, n:int, R:list) -> list:
    """Removes a bedroom from the list"""
    xx = []
    if n in C:
        C.remove(n)
        for i in range(len(R)):
            if n == R[i].bedroom_num:
                print("Deleting room {} forces cancellation of this reservation:\n\t{} arriving {}/{}/{} and departing  {}/{}/{} (Conf. #{})".format(R[i].bedroom_num, R[i].name,
                                                                                                                                                    R[i].arrival.month, R[i].arrival.day,
                                                                                                                                                    R[i].arrival.year, R[i].departure.month,
                                                                                                                                                    R[i].departure.day, R[i].departure.year, R[i].confirmation_num))
                xx.append(i)
        xx.sort(reverse=True)
        for k in xx:
            R.remove(R[k])
    else:
        print("Sorry, can't delete room {}; it is not in service now".format(n))
    return C

from collections import namedtuple
Reservation = namedtuple("Reservation", "bedroom_num arrival departure name confirmation_num")

def Reservation_new() -> list:
    ''' Return a new, empty list of reservations'''
    return [ ]

import datetime

def new_reservation(R: list, x: list, C:list, count:int) -> list:
    """Adds a new reservation to the list"""
    aa = x[2].split("/")
    arrival = datetime.date(int(aa[2]), int(aa[0]), int(aa[1]))
    bb = x[3].split("/")
    departure = datetime.date(int(bb[2]), int(bb[0]), int(bb[1]))
    for k in R:
        if int(x[1]) == k.bedroom_num and departure > k.arrival and arrival < k.departure or int(x[1]) == k.bedroom_num and k.departure > arrival and k.arrival < departure:
            print("Sorry, can't reserve room {} ({}/{}/{} to {}/{}/{});\n\tit's already booked (Conf. #{})".format(x[1], arrival.month, arrival.day, arrival.year, departure.month, departure.day, departure.year, k.confirmation_num))
            return R
        
    if int(x[1]) not in C:
        print("Sorry; can't reserve room {}; room not in service".format(x[1]))
    elif departure.year < arrival.year or departure.year == arrival.year and departure.month < arrival.month or departure.year == arrival.year and departure.month == arrival.month and departure.day < arrival.day:
        print("Sorry, can't reserve room {} ({}/{}/{} to {}/{}/{});\n\tcan't leave before you arrive.".format(x[1], arrival.month, arrival.day, arrival.year, departure.month, departure.day, departure.year))
    elif departure.year == arrival.year and departure.month == arrival.month and departure.day == arrival.day:
        print("Sorry, can't reserve room {} ({}/{}/{} to {}/{}/{});\n\tcan't arrive and leave on the same day.".format(x[1], arrival.month, arrival.day, arrival.year, departure.month, departure.day, departure.year))
    else:
        count.append(1)
        R.append(Reservation(int(x[1]), arrival, departure, " ".join(x[4:]), len(count)))
        print("Reserving room {} for {} -- Confirmation #{}\n\t(arriving {}/{}/{}, departing {}/{}/{})".format(R[-1].bedroom_num, R[-1].name, R[-1].confirmation_num, R[-1].arrival.month,R[-1].arrival.day, R[-1].arrival.year, R[-1].departure.month, R[-1].departure.day, R[-1].departure.year))
    return R

def list_reservations(R: list) -> None:
    """Prints all the reservations"""
    print("Number of reservations: ", len(R))
    print("No. Rm. Arrive      Depart     Guest")
    print("------------------------------------------------")
    RR = R[:]
    RR.sort(key = arrival_date)
    for i in RR:
        print("  {} {} {:2d}/{:2d}/{:4d} {:2d}/{:2d}/{:4d} {}".format(i.confirmation_num, i.bedroom_num, i.arrival.month, i.arrival.day, i.arrival.year, i.departure.month, i.departure.day, i.departure.year, i.name))

def arrival_date(a:Reservation) -> datetime.date:
            '''Returns the date of a reservation'''
            return a.arrival

def remove_reservation(R: list, n: int) -> list:
    """Removes a reservation from the list of reservations"""
    for i in R:
        if n == i.confirmation_num:
            R.remove(i)
            return R
    print("Sorry, can't cancel reservation; no confirmation number {}".format(n))
    return R

def bedroom_res(R: list, n:int) -> None:
    """Prints all reservations for given bedroom n"""
    print("Reservations for room {}:".format(n))
    for i in R:
        if i.bedroom_num == n:
            print("   {:2d}/{:2d}/{:4d} to {:2d}/{:2d}/{:4d}:  {}".format(i.arrival.month, i.arrival.day, i.arrival.year, i.departure.month, i.departure.day, i.departure.year, i.name))

def res_guest(R:list, n:str) -> None:
    """Prints all the reservations for given guest"""
    print("Reservations for {}:".format(n))
    for i in R:
        if i.name == n:
            print("   {:2d}/{:2d}/{:4d} to {:2d}/{:2d}/{:4d}:  {}".format(i.arrival.month, i.arrival.day, i.arrival.year, i.departure.month, i.departure.day, i.departure.year, i.name))

def list_arrivals(R:list, n:str) -> None:
    """Prints all the guests on the arrival date"""
    print("Guests arriving on {}:".format(n))
    cc = n.split("/")
    arrival = datetime.date(int(cc[2]), int(cc[0]), int(cc[1]))
    for i in R:
        if arrival == i.arrival:
            print("   {} (room {})".format(i.name, i.bedroom_num))

def list_departures(R:list, n:str) -> None:
    """Prints all the guests leaving on the departure date"""
    print("Guests departing on {}:".format(n))
    cc = n.split("/")
    departure = datetime.date(int(cc[2]), int(cc[0]), int(cc[1]))
    for i in R:
        if departure == i.departure:
            print("   {} (room {})".format(i.name, i.bedroom_num))

def list_free_bed(C: list, R: list, x: str, y:str) -> None:
    """List all the bedrooms free between the arrival and departure date"""
    zz = x.split("/")
    arrival = datetime.date(int(zz[2]), int(zz[0]), int(zz[1]))
    yy = y.split("/")
    departure = datetime.date(int(yy[2]), int(yy[0]), int(yy[1]))
    print("Bedrooms free between {} to {}:".format(x, y))
    result = C[:]
    result.sort()
    xx = []
    for i in range(len(C)):
        for a in R:
            if C[i] == a.bedroom_num:
                if a.departure > arrival and a.departure < departure or a.arrival > arrival and a.arrival < departure or a.departure > arrival and a.arrival < arrival:
                    xx.append(i)
    xx.sort(reverse=True)
    for k in xx:
        result.remove(result[k])
    for x in result:
        print("   " + str(x))

def list_occupied_bed(C: list, R: list, x: str, y:str) -> None:
    """List all the bedrooms occupied between the arrival and departure date"""
    zz = x.split("/")
    arrival = datetime.date(int(zz[2]), int(zz[0]), int(zz[1]))
    yy = y.split("/")
    departure = datetime.date(int(yy[2]), int(yy[0]), int(yy[1]))
    print("Bedrooms occupied between {} to {}:".format(x, y))
    xx = []
    for i in range(len(C)):
        for a in R:
            if C[i] == a.bedroom_num:
                if (a.arrival <= arrival and a.departure > departure or
                    a.arrival < arrival and a.departure < departure and a.departure > arrival or
                    a.arrival > arrival and a.arrival < departure and a.departure > departure or
                    a.departure > arrival and a.departure >= departure and a.arrival < departure):
                    xx.append(C[i])
    xx.sort()
    for x in xx:
        print("   " + str(x))

        
y = input("Please enter the name of the save file: ")
print()
x = input("Please enter the file you would like to read: ")
print()
xx = open(x,'r')
yy = open(y, 'a+')
xxx = xx.readlines()
for i in xxx:    
    yy.write(i)
yy.close()
antbnb(y)

'''
PART a) INPUT
## adding rooms for test case
nb 101
nb   102
  NB  103
nB 104
Nb 106
## out of order rooms
nb 105
nb 200
nb 201
## adding numerous reservations
nr 101 1/1/2000 1/2/2000 N. Ethan
Nr 101 1/3/2000 1/4/2000 N. Ethan
nR 102 12/12/1999 12/14/1999 R. Abraham
nr 103 5/25/2008 7/2/2008 N. Andrew
nr 201 3/11/2015 5/22/2016 A. Ahri
nr 200 4/20/2010 4/20/2011 L. Calvin
nR 201 1/1/2000 1/4/2000 P. Harrison
nr 103 12/22/1999 1/1/2000 A. Ahri
## printing reservations
LR
BR 101
RG N. Ethan
RG A. Ahri
LA 1/1/2000
LD 12/14/1999
LO 1/1/2000 1/1/2000
LO 12/13/1999 12/14/1999
LO 5/11/2010 5/12/2010
LB
PL

PART a) OUTPUT
Reserving room 101 for N. Ethan -- Confirmation #1
	(arriving 1/1/2000, departing 1/2/2000)
Reserving room 101 for N. Ethan -- Confirmation #2
	(arriving 1/3/2000, departing 1/4/2000)
Reserving room 102 for R. Abraham -- Confirmation #3
	(arriving 12/12/1999, departing 12/14/1999)
Reserving room 103 for N. Andrew -- Confirmation #4
	(arriving 5/25/2008, departing 7/2/2008)
Reserving room 201 for A. Ahri -- Confirmation #5
	(arriving 3/11/2015, departing 5/22/2016)
Reserving room 200 for L. Calvin -- Confirmation #6
	(arriving 4/20/2010, departing 4/20/2011)
Reserving room 201 for P. Harrison -- Confirmation #7
	(arriving 1/1/2000, departing 1/4/2000)
Reserving room 103 for A. Ahri -- Confirmation #8
	(arriving 12/22/1999, departing 1/1/2000)
Number of reservations:  8
No. Rm. Arrive      Depart     Guest
------------------------------------------------
  3 102 12/12/1999 12/14/1999 R. Abraham
  8 103 12/22/1999  1/ 1/2000 A. Ahri
  1 101  1/ 1/2000  1/ 2/2000 N. Ethan
  7 201  1/ 1/2000  1/ 4/2000 P. Harrison
  2 101  1/ 3/2000  1/ 4/2000 N. Ethan
  4 103  5/25/2008  7/ 2/2008 N. Andrew
  6 200  4/20/2010  4/20/2011 L. Calvin
  5 201  3/11/2015  5/22/2016 A. Ahri
Reservations for room 101:
    1/ 1/2000 to  1/ 2/2000:  N. Ethan
    1/ 3/2000 to  1/ 4/2000:  N. Ethan
Reservations for N. Ethan:
    1/ 1/2000 to  1/ 2/2000:  N. Ethan
    1/ 3/2000 to  1/ 4/2000:  N. Ethan
Reservations for A. Ahri:
    3/11/2015 to  5/22/2016:  A. Ahri
   12/22/1999 to  1/ 1/2000:  A. Ahri
Guests arriving on 1/1/2000:
   N. Ethan (room 101)
   P. Harrison (room 201)
Guests departing on 12/14/1999:
   R. Abraham (room 102)
Bedrooms occupied between 1/1/2000 to 1/1/2000:
   101
   201
Bedrooms occupied between 12/13/1999 to 12/14/1999:
   102
Bedrooms occupied between 5/11/2010 to 5/12/2010:
   200
Number of bedrooms in service: 8
------------------------------------
101
102
103
104
105
106
200
201

PART B)OUTPUT FILE CONTENT
NB 101
NB 102
NB 103
NB 104
NB 106
NB 105
NB 200
NB 201
NR 101 1/1/2000 1/2/2000 N. Ethan
NR 101 1/3/2000 1/4/2000 N. Ethan
NR 102 12/12/1999 12/14/1999 R. Abraham
NR 103 5/25/2008 7/2/2008 N. Andrew
NR 201 3/11/2015 5/22/2016 A. Ahri
NR 200 4/20/2010 4/20/2011 L. Calvin
NR 201 1/1/2000 1/4/2000 P. Harrison
NR 103 12/22/1999 1/1/2000 A. Ahri
'''
