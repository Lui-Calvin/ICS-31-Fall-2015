#ICs 31 Thursday 8 october 2015,11 am
from collections import namedtuple
Student = namedtuple('Student','name ID GPA major')
s1 = Student("Peter",11112222,3.95,"CSE")
s2 = Student("Paula",22222222,3.99,"CS")
s3 = Student("Jane",33334444,3.55,"Econ")
SL = [s1,s2,s3]
print(SL)
SL.sort()
print(SL)
def get_GPA(s:Student)
