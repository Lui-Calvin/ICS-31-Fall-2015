#Calvin Lui 84152100 and Mark Lewis 10171060. Ics 31 lab sec 2.
print(2*3)
print(4**5)

#part 1 number 1
integer = 2
total = 0
while integer <= 10:
    total = total + integer
    integer = integer + 2
print(total)

#part 1 number 2
testScores = [75,83.5,61,43]
i = 0
average = 0
while i < len(testScores):
    average = average + testScores[i]
    i = i + 1
average = average / len(testScores)
print(average)

#part 1 number 3
print('2 to the power of 10 is', 2**10)

#part 1 number 4
mass = 50
velocity = 15
kineticEnergy = 0.5 * mass * velocity
print('the kinetic energy of the moving anteater is',kineticEnergy,'joules')

#part 2------------------------------------------------------------------------
wall = 'w'
cannon = 'c'
print(wall+cannon)
print(wall+cannon+wall)
print(wall*3+cannon+wall*3)
print((wall + cannon *2)*4)
#print(wall+cannon*2+wall+cannon*2+wall+cannon*2+wall+cannon*2)
print((wall*3+cannon)*4+wall)
#print(wall*3,cannon,wall*3,cannon,wall*3,cannon,wall*3,cannon,wall)
print((wall*4+cannon)*4+wall*4)
#print(wall*4+cannon+wall*4+cannon+wall*4+cannon+wall*4+cannon+wall*4)

#part 3-------------------------------------------------------------------
test_scores = "4325220523455023"
print('the first student\'s test score is', test_scores[0])
print('the fifth student\'s test score is', test_scores[4])
print('the tenth student\'s test score is', test_scores[9])
print('the sixteenth student\'s test score is', test_scores[15])

#part 4--------------------------------------------------------------------
s = 'anteater'
print('The first character of string s is \'a\'', s[0] == 'a')
print('The last character of string s is ‘r’', s[len(s)-1] == 'r')
print('The fourth character of string s is ‘x’', s[3] == 'x')
print('The first three characters of string s match the string ‘zot’', s[:2]== 'zot')

#part5--------------------------------------------------------------------------------------
pi = 3.14159
make = 'Toyota'
model = 'Camry'
year = '2014'
ics_majors = ['Computer Science', 'Informatics', 'Computer Game Science']
num = 3
total = 0
while num <= 9:
    total = total +num
    num = num +2
a = total/4
print(a)

#part6---------------------------------------------------------------------
print('20 plus 35 is geater than 2 to the power of 4',20+35 > 2**4)
print('The string ‘hello’ is not equivalent to the string ‘goodbye’','hello' != 'goodbye')
print('The remainder when 10 is divided by 3 is less or equal to 1.',10%3 <=1)
print('The list [‘apple’, ‘orange’, ‘banana’, ‘mango’] contains 5 elements.', len(['apple', 'orange', 'banana', 'mango']) == 5)
print('The number 63 is an even number.', 63%2 == 0)

#part7---------------------------------------------------------------------------------------------------------------
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[3]+s[14]+s[6])
print(s[19]+s[21])
print(s[8]+s[2]+s[18])
print(s[20]+s[2]+s[8])
      
