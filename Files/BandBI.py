# Jeffrey Lee Ye 68342291 & Calvin Lui 84152100
from collections import namedtuple
import datetime
#STAGE I

#Global variables to manipulate
bedrooms = [] #String of numbers. Allows 12A or 12B and so on
reservation_list = []
Reservation = namedtuple('Reservation', "room arrdate depdate name num")
reservation_counter = 1
def reserve(line:str,num:int)-> Reservation:
    '''takes a line of text and converts information to a Reservation namedtuple'''
    info = line.split()
    name = ""
    for i in range(3,len(info)):
        name += info[i] + " "
    name = name.strip()
    return(Reservation(info[0],info[1],info[2], name,num))
def date_Tostring(date:str)->str:
    '''converts a date string into a specific date format'''
    date_info = date.split('/')
    for n in range(0,3):
        if len(date_info[n]) < 2:
            date_info[n] = ' ' + date_info[n]
    return "{}/{}/{}".format(date_info[0],date_info[1],date_info[2])
def reservation_Tostring(R:Reservation)->str:
    """takes a reservation and converts data into a readable string"""
    return "{:3} {:3} {} {} {}".format(R.num,R.room,date_Tostring(R.arrdate),date_Tostring(R.depdate),R.name)
def date_to_datetime(date:str)->datetime:
    '''converts a date string to a datetime date object'''
    date_info = date.split('/')
    return datetime.date(int(date_info[2]),int(date_info[0]),int(date_info[1]))
def within_dates_arrival(arrdate:str,depdate:str,testdate:str)->bool:
    '''checks if the arrival date is in between an arrival and departure'''
    if date_to_datetime(testdate) >= date_to_datetime(arrdate) and date_to_datetime(testdate) < date_to_datetime(depdate):
        return True
    return False
def within_dates_departure(arrdate:str,depdate:str,testdate:str)->bool:
    """checks if the departure date is in between an arrival and departure"""
    if date_to_datetime(testdate) > date_to_datetime(arrdate) and date_to_datetime(testdate) <= date_to_datetime(depdate):
        return True
    return False
def remove_reservation_by_room(room:str)->None:
    for R in range(len(reservation_list)-1,-1,-1):
        if reservation_list[R].room == room:
            print("Deleting room %s forces cancellation of this reservation:\n\t%s arriving %s and departing  %s(Conf. #%s)"%(reservation_list[R].room,reservation_list[R].name,date_Tostring(reservation_list[R].arrdate),date_Tostring(reservation_list[R].depdate),reservation_list[R].num))
            reservation_list.remove(reservation_list[R])
def bedroom_avail_on_dates(bedroom:str,arrival:str,departure:str)->bool:
    """returns boolean to represent if room is available between dates"""
    arr = date_to_datetime(arrival)
    dep = date_to_datetime(departure)
    for R in reservation_list:
        if R.room == bedroom:
            arrDate = date_to_datetime(R.arrdate)
            depDate = date_to_datetime(R.depdate)
            if arr > arrDate and  arr< depDate or dep > arrDate and dep < depDate:
                return False
    return True
def bedroom_occupied_on_dates(bedroom:str,arrival:str,departure:str):
    arr = date_to_datetime(arrival)
    dep = date_to_datetime(departure)
    for R in reservation_list:
        if R.room == bedroom:
            arrDate = date_to_datetime(R.arrdate)
            depDate = date_to_datetime(R.depdate)
            if arr > arrDate and arr < depDate or dep > arrDate and dep <depDate:
                return True
    return False
def get_res_arrival_date(R:Reservation)->datetime:
    return date_to_datetime(R.arrdate)
def executeCmdFile():
    '''Executes the Command File and prints what needs to be printed'''
    txt = input("please type the name of the file you would like to be read: ")
    infile = open(txt, "r")

    #Go through the file, line by line
    for line in infile:
        #Get rid of any empty space in front and newLine character at back
        command = line.lstrip().rstrip("\n")

        #Activates commands based on the stripped line
        activateCommand(command)
    activateCommand("SV")
    infile.close()

def activateCommand(line: str) -> bool:
    '''Figures out the command in the line and does what is supposed to do'''
    CMD = line[0:2].upper()
    phrase = line[2:]

    #Takes away space in front of the phrase
    phrase = phrase.lstrip()
    

    if CMD == "NB": #Adds a bedroom using a 3 digit value
        if phrase not in bedrooms:
            bedrooms.append(phrase)
        else:
            print("Sorry, can't add room %s again; it's already on the list."%phrase)
    elif CMD == "LB": #Prints The number of bedrooms in service, followed by their values       
        print("Number of bedrooms in service:", len(bedrooms))
        print("------------------------------------")
        for room in sorted(bedrooms):
            print(room)
            
    elif CMD == "PL": #Prints the phrase       
        print(phrase)
    elif CMD == "RB":
        if phrase in bedrooms:
            bedrooms.remove(phrase)
            remove_reservation_by_room(phrase)
        else:
            print("Sorry, can't delete room %s;\n\t it is not in service now"% (phrase))
    elif CMD == 'NR':
        global reservation_counter
        new_res = reserve(phrase, reservation_counter)#potential reservation
        arrdate = date_to_datetime(new_res.arrdate)
        depdate = date_to_datetime(new_res.depdate)
        if arrdate > depdate:
            print('Sorry, can\'t reserve room %s (%s to %s);\n\tcan\'t leave before you arrive.'%(new_res.room,new_res.arrdate,new_res.depdate))
        elif arrdate == depdate:
            print('Sorry, can\'t reserve room %s (%s to %s);\n\tcan\'t arrive and leave on the same day.'%(new_res.room,new_res.arrdate,new_res.depdate))
        elif new_res.room in bedrooms:
            for R in reservation_list:
                if (new_res.room == R.room and within_dates_arrival(R.arrdate,R.depdate,new_res.arrdate)) or (new_res.room == R.room and within_dates_departure(R.arrdate,R.depdate,new_res.depdate)):
                    #print(within_dates_arrival(R.arrdate,R.depdate,new_res.arrdate))
                    #print(within_dates_departure(R.arrdate,R.depdate,new_res.depdate))
                    print("Sorry, can\'t reserve room %s (%s to %s);\n\tit\'s already booked (Conf. #%s)"%(new_res.room,date_Tostring(new_res.arrdate),date_Tostring(new_res.depdate),R.num))
                    return        
            print("reserving room {:3} for {} -- Confirmation #{}\n\t(arriving {}, departing {}".format(new_res.room,new_res.name,new_res.num,date_Tostring(new_res.arrdate),date_Tostring(new_res.depdate)))
            reservation_list.append(new_res)
            reservation_counter += 1
        else:
            print("Sorry; can\'t reserve room %s; room not in service"%(new_res.room))
    elif CMD == 'LR':
        print('number of reservations: ' + str(len(reservation_list)))
        print('No. Rm. Arrive      Depart     Guest\n------------------------------------------------')
        for res in sorted(reservation_list,key = get_res_arrival_date) :
              print(reservation_Tostring(res))# prints Tostring of a reservation
    elif CMD == "RR":
        confirmation_num = []
        for i in reservation_list:
            confirmation_num.append(str(i.num))#makes a list of conf numbers
        if phrase in confirmation_num:
            for res in range(0,len(reservation_list)):
                if str(reservation_list[res].num) == phrase:
                             reservation_list.remove(reservation_list[res])
                             break
                           
        else:
            print("Sorry, can't cancel reservation;\n\t no confirmation number %s"%phrase)
            
                
    elif CMD == "BR":
        print('reservations for room %s' %phrase)
        for R in reservation_list:
            if R.room == phrase:
                 print("\t{} to {} {}".format(R.arrdate,R.depdate,R.name))
    elif CMD == "RG":
        print('reservations for %s'%phrase)
        for R in reservation_list:
            if R.name == phrase:
                print("\t{} to {} room {}".format(R.arrdate,R.depdate,R.room))
    elif CMD == "LA":
        print('Guests arriving on %s:'%phrase)
        for R in reservation_list:
            if R.arrdate == phrase:
                print('\t'+ R.name)
    elif CMD == "LD":
        print('Guests departing on %s:'%phrase)
        for R in reservation_list:
            if R.depdate == phrase:
                print('\t'+ R.name)
    elif CMD == "LF":
        dates = phrase.split()
        print("Bedrooms free between %s to %s:"%(dates[0],dates[1]))
        for B in bedrooms:
            if bedroom_avail_on_dates(B,dates[0],dates[1]):
                print('\t' + B)
    elif CMD == "LO":
        dates = phrase.split()
        print("Bedrooms occupied between %s to %s"%(dates[0],dates[1]))
        for B in bedrooms:
            if bedroom_occupied_on_dates(B,dates[0],dates[1]):
                print('\t'+ B)
    elif CMD == "SV":
        filename = input("please enter the name of the save file: ")
        savefile = open(filename,'w')
        for b in bedrooms:
            savefile.write("NB " + b + "\n")
        for r in reservation_list:
            savefile.write("NR {:3} {:10} {:10} {}".format(r.room,r.arrdate,r.depdate,r.name)+'\n')
        
    elif CMD != "##": #Invalid CMD
        print("Line error in command file (<:o) ")
    
executeCmdFile()
'''
Part a) INPUT
nb 100
nb   102
   NB 103
nB 104
NB 107
##out of order rooms
nB 200
NB 201
nb 106
##adding reservations
NR 100 2/23/2000 2/25/2000 L. Calvin
NR 100 2/25/2000 2/28/2000 L. Calvin
nR 102 11/12/2000 11/13/2000 L. Kimin
Nr 103 11/12/2000 11/28/2000 L. Kimin
NR 107 5/16/2001 5/30/2001 N. Steven
NR 200 10/3/2002 10/14/2002 V. Justin
nR 201  3/6/2002 3/9/2002 C. Lance
NR 106 7/12/2001 7/15/2001 H. Raymond
##printing reservation
LR
BR 100
RG L. Calvin
RG L. Kimin
LA 11/12/2000
LO 2/23/2000 2/28/2000
LO 11/12/2000 11/28/2000
LF 2/12/2002 2/14/2002
LB
PL

part b)OUTPUT
reserving room 100 for L. Calvin -- Confirmation #1
	(arriving  2/23/2000, departing  2/25/2000
reserving room 100 for L. Calvin -- Confirmation #2
	(arriving  2/25/2000, departing  2/28/2000
reserving room 102 for L. Kimin -- Confirmation #3
	(arriving 11/12/2000, departing 11/13/2000
reserving room 103 for L. Kimin -- Confirmation #4
	(arriving 11/12/2000, departing 11/28/2000
reserving room 107 for N. Steven -- Confirmation #5
	(arriving  5/16/2001, departing  5/30/2001
reserving room 200 for V. Justin -- Confirmation #6
	(arriving 10/ 3/2002, departing 10/14/2002
reserving room 201 for C. Lance -- Confirmation #7
	(arriving  3/ 6/2002, departing  3/ 9/2002
reserving room 106 for H. Raymond -- Confirmation #8
	(arriving  7/12/2001, departing  7/15/2001
number of reservations: 8
No. Rm. Arrive      Depart     Guest
------------------------------------------------
  1 100  2/23/2000  2/25/2000 L. Calvin
  2 100  2/25/2000  2/28/2000 L. Calvin
  3 102 11/12/2000 11/13/2000 L. Kimin
  4 103 11/12/2000 11/28/2000 L. Kimin
  5 107  5/16/2001  5/30/2001 N. Steven
  8 106  7/12/2001  7/15/2001 H. Raymond
  7 201  3/ 6/2002  3/ 9/2002 C. Lance
  6 200 10/ 3/2002 10/14/2002 V. Justin
reservations for room 100
	2/23/2000 to 2/25/2000 L. Calvin
	2/25/2000 to 2/28/2000 L. Calvin
reservations for L. Calvin
	2/23/2000 to 2/25/2000 room 100
	2/25/2000 to 2/28/2000 room 100
reservations for L. Kimin
	11/12/2000 to 11/13/2000 room 102
	11/12/2000 to 11/28/2000 room 103
Guests arriving on 11/12/2000:
	L. Kimin
	L. Kimin
Bedrooms occupied between 2/23/2000 to 2/28/2000
Bedrooms occupied between 11/12/2000 to 11/28/2000
Bedrooms free between 2/12/2002 to 2/14/2002:
	100
	102
	103
	104
	107
	200
	201
	106
Number of bedrooms in service: 8
------------------------------------
100
102
103
104
106
107
200
201


PART B) OUTPUT FILE CONTENT
NB 100
NB 102
NB 103
NB 104
NB 107
NB 200
NB 201
NB 106
NR 100 2/23/2000  2/25/2000  L. Calvin
NR 100 2/25/2000  2/28/2000  L. Calvin
NR 102 11/12/2000 11/13/2000 L. Kimin
NR 103 11/12/2000 11/28/2000 L. Kimin
NR 107 5/16/2001  5/30/2001  N. Steven
NR 200 10/3/2002  10/14/2002 V. Justin
NR 201 3/6/2002   3/9/2002   C. Lance
NR 106 7/12/2001  7/15/2001  H. Raymond


'''
