#Calvin Lui 84152100 lab section 9
from collections import namedtuple
print("Calvin Lui 84152100 lab section 9")
print()
print()
print('----part C.1----')
Dish = namedtuple('Dish', 'name price calories')
def read_menu_with_count(file:str)->'list of Dish':
    '''takes as an argument a string naming a file in this format,
    reads the file, and returns a list of Dish structures created from the data'''
    ret_list = []
    infile = open(file,'r')
    last = eval(infile.readline())
    for D in range(0,last):
        dish_text = infile.readline().split('\t')
        ret_list.append(Dish(dish_text[0],float(dish_text[1][1:]),int(dish_text[2])))
    return ret_list
print("This is the Dish list of menu1: \n",read_menu_with_count('menu1.txt'))
print()
print("This is the Dish list of menu2: \n",read_menu_with_count('menu2.txt'))
print()
print()
print("----part c.2----")
def read_menu(file:str)->'list of Dish':
    '''takes as an argument a string naming a file in this format,
    reads the file, and returns a list of Dish structures created from the data.'''
    ret_list = []
    infile = open(file,'r')
    while True:
        dish_text = infile.readline().split('\t')
        if len(dish_text) == 3:
            ret_list.append(Dish(dish_text[0],float(dish_text[1][1:]),int(dish_text[2])))
        else:
            break
    return ret_list
print("This is the Dish list of menu2: \n",read_menu('menu3.txt'))
print()
print()
print('----part c.3 ----')
def write_menu(D:'list of Dish',file:str)->None:
    outfile = open(file,'w')
    outfile.write(str(len(D))+ "\n")
    for dish in D:
        outfile.write("{}\t{}\t{}\n".format(dish.name,dish.price,dish.calories))
    outfile.close()
write_menu(read_menu('menu3.txt'),'delete.txt')
print()
print()
print("----part d.1----")
Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)

Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])

StudentBody = [sW, sX, sY, sZ]
def Course_names(CL:'list of Course')->str:
    ret_str = ''
    for c in CL:
        ret_str += c.dept + c.num + " "
    return ret_str
def Studentlist_toStr(SL:'list of Student')->str:
    ret_str = ''
    
    for s in SL:
        
        ret_str += "ID: {}\t Name:{:20} Level: {}      Major: {:10} StudyList: {} \n\n".format(s.ID,s.name,s.level,s.major,Course_names(s.studylist))
    return ret_str        
def Students_at_level(SL:'list of Student',CL:str)->'list of Student':
    '''takes a list of Students and a string (representing a class level,
    e.g., 'FR' or 'SO') and returns a list of students whose class level
    matches the parameter.'''
    ret_list = []
    for student in SL:
        if student.level == CL:
            ret_list.append(student)
    return ret_list
assert Students_at_level(StudentBody,'FR') == [Student(ID='11223344', name='Anteater, Peter', level='FR', major='PSB', studylist=[Course(dept='ICS', num='31', title='Intro to Programming', instr='Kay', units=4.0), Course(dept='Writing', num='39A', title='Intro Composition', instr='Alexander', units=4.0), Course(dept='Biology', num='97', title='Genetics', instr='Smith', units=4.0), Course(dept='Management', num='1', title='Intro to Management', instr='Jones', units=2.0)]), Student(ID='31223344', name='Programmer, Paul', level='FR', major='COG SCI', studylist=[Course(dept='ICS', num='32', title='Programming with Libraries', instr='Thornton', units=4.0), Course(dept='Writing', num='39A', title='Intro Composition', instr='Alexander', units=4.0), Course(dept='Biology', num='97', title='Genetics', instr='Smith', units=4.0)])]
print("The students at the freshmen level are: \n" + Studentlist_toStr(Students_at_level(StudentBody,'FR')))
print()
print()
print('----part d.2----')
print()
def Students_in_majors(SL:'list of Student',majors:'list of major'):
    '''takes a list of Students and a list of strings
    (where each string represents a major) and returns a list
    of Students that have majors on the specified list.'''
    ret_list = []
    for student in SL:
        if student.major in majors:
            ret_list.append(student)
    return ret_list
print("Students that are PSB and CS majors: \n",Studentlist_toStr(Students_in_majors(StudentBody,['PSB','CS'])))
print()
print()
print('----part D.3----')
def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    return c1.dept == c2.dept and c1.num == c2.num
def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    return c in SL
def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     studylist (and False otherwise)
    '''
    for course in S.studylist:
        if course.dept == department and course.num == coursenum:
            return True
    return False
def Student_in_class(SL:'list of Student',dn:str,cn:str)->'list of Student':
    '''takes a list of Students, and two strings—a department name and a course
    number (e.g., 'ICS' and '31')—and returns a list of those Students
    who are enrolled in the specified class.'''
    ret_list = []
    for student in SL:
        if Student_is_enrolled(student,dn,cn):
            ret_list.append(student)
    return ret_list
assert Student_in_class(StudentBody,'ICS','31') == [Student(ID='11223344', name='Anteater, Peter', level='FR', major='PSB', studylist=[Course(dept='ICS', num='31', title='Intro to Programming', instr='Kay', units=4.0), Course(dept='Writing', num='39A', title='Intro Composition', instr='Alexander', units=4.0), Course(dept='Biology', num='97', title='Genetics', instr='Smith', units=4.0), Course(dept='Management', num='1', title='Intro to Management', instr='Jones', units=2.0)]), Student(ID='21223344', name='Anteater, Andrea', level='SO', major='CS', studylist=[Course(dept='ICS', num='31', title='Intro to Programming', instr='Kay', units=4.0), Course(dept='Writing', num='39B', title='Intermediate Composition', instr='Gross', units=4.0), Course(dept='Biology', num='97', title='Genetics', instr='Smith', units=4.0), Course(dept='Management', num='1', title='Intro to Management', instr='Jones', units=2.0)])]
print('the list of students in ICS 31 are: \n',Studentlist_toStr(Student_in_class(StudentBody,'ICS','31')))
print()
print()
print('----part d.4----')
def Student_names(SL:'list of Student')->'list of Str':
    ret_list = []
    for S in SL:
        ret_list.append(S.name)
    return ret_list 
print(Student_names(StudentBody))
print()
print()
print('----part d.5----')
StudentBody += [Student('12345678','Pickle, Dill','SR','BIM',[ics32,mgt1]),
                Student('87654321','Pie, Banana','JR','CSE',[ics32,wr39b]),
                Student('43215678','Pi, Raspberry','FR','Biology',[bio97,wr39a]),
                Student('11111111','Mega, Arduino','SR','INFX',[ics32,wr39b,mgt1]),
                Student('22222222','Bot, Maker','FR','SE',[ics31,wr39a])]
ICS_majors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']
print("List of Students who are majors from the School of ICS: \n"+
      Studentlist_toStr(Students_in_majors(StudentBody,ICS_majors)))
print()
print("List of names of students who are majors from the School of ICS: \n",
      Student_names(Students_in_majors(StudentBody,ICS_majors)))
print()
print("The number of students who are majors from the School of ICS is ",
      len(Students_in_majors(StudentBody,ICS_majors)))
print()
print('The list of names of Seniors who are majors in the School of ICS is: \n',
      Student_names(Students_at_level(Students_in_majors(StudentBody,ICS_majors),'SR')))
print()
print("The number of Seniors who are majors in the School of ICS is ",
      len(Student_names(Students_at_level(Students_in_majors(StudentBody,ICS_majors),'SR'))))
print()
print('the percentage of majors from the school of ICS who are seniors is',
      str(float(len(Student_names(Students_at_level(Students_in_majors(StudentBody,ICS_majors),
        'SR'))))/float(len(StudentBody))*100) + '%')
print()
print('The number of freshmen who are majors from the School of ICS and enrolled in ICS31 is',
      len(Student_in_class(Students_at_level(StudentBody,'FR'),'ICS','31')))
print()
FR_ICS31 = Student_in_class(Students_at_level(StudentBody,'FR'),'ICS','31')

avg_sum = 0
for student in FR_ICS31:
    for c in student.studylist:
        avg_sum += c.units
avg_sum/= len(FR_ICS31)

print('The average number of units that freshmen in ICS 31 are enrolled in is ',avg_sum)
print()
print()
print('---- part e.1----')
