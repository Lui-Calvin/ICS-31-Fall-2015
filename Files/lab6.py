#Calvin Lui 84152100 and Ryan Liu 73638562. ICS lab sec 9
print('Calvin Lui 84152100 and Ryan Liu 73638562. ICS lab sec 9')
print()
print()
print('---- c.1----')
def contains(s1:str,s2:str)->bool:
    '''Returns a boolean whether second string is in the first string'''
    return s2 in s1
assert contains('banana', 'ana')
assert not contains('racecar', 'ck')
print()
print()
print('---- c.2----')
def Punc_blank(s:str)-> str:
    '''takes in a string and returns the string with no punctuations'''
    key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ret_str = ""
    for C in s:
        if C in key:
            ret_str += C
        else:
            ret_str+= " "
    return ret_str
    
def sentence_stats(w:str)->None:
    '''returns information about a string such as average length of words, character count, and word count'''
    s = Punc_blank(w)
    L = s.split()
    avg_sum = 0
    for item in L:
        avg_sum += len(item)
    characters = len(w)
    avg_sum /= len(L)
    words = len(L)
    print( "Characters: " + str(characters) + "\n"+
            "Words: " + str(words) + "\n" +
            "Average word length: " + str(avg_sum) + "\n\n")
print('Sentence stats for "hello dude"')
sentence_stats('hello dude')
print('Sentence stats for "we are in lab section nine"')
sentence_stats('we are in lab section nine')
print('Sentence stats for "***The ?! quick brown fox:  jumps over the lazy dog."')
sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.')
print()
print()
print('---- part c.3----')
def initials(s:str)->str:
    '''returns the first letter every word of the string in uppercase letters'''
    L = s.split()
    ret_str = ""
    for item in L:
        ret_str += item[0]
    return ret_str.upper()
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'
print('The initials for "Ryan y liu" are ',initials("Ryan y liu"))
print('The initials for "Calvin wei kin Lui" are ',initials("Calvin wei kin Lui"))
print()
print()
print('----part d.1----')
from random import randrange
print("printing random numbers from 0 to 10, 50 times")
for i in range(0,50):
    print(randrange(0,11))
print("printing random numbers from 0 to 6, 50 times")
for i in range(0,50):
    print(randrange(1,7))
print()
print()
print('----part d.2----')
def roll2dice()->int:
    '''returns the value of two die after being randomly rolled'''
    d1 = randrange(1,7)
    d2 = randrange(1,7)
    return d1+d2
print("The result of two die rolled 50 times: ")
for i in range(0,50):
    print(roll2dice())
print()
print()
print("---- d.3----")
def star_str(n:int)->str:
    '''helper method to return n amount of stars'''
    ret_str = ""
    for i in range(0,n):
        ret_str += "*"
    return ret_str
def distribution_of_rolls(n:int)-> None:
    '''simulates n amount of rolls and prints statistics'''
    Occ_list = [0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,n):
        roll = roll2dice()
        Occ_list[roll-2]+=1
    ret_str = ""
    for num in range(0,len(Occ_list)):
         ret_str += "{:2}:\t{:2} ( {:4.1f}%) {}\n".format(num+2,str(Occ_list[num]),Occ_list[num]/(n/100),star_str(Occ_list[num]))
    ret_str += "-----------------------------------\n\t" + str(n) + 'rolls\n'
    print(ret_str)
distribution_of_rolls(200)
distribution_of_rolls(150)
print()
print()
print("----part e.1----")
def Caeser_encrypt(message:str,key:int)->str:
    '''encrypt a message according to a key with a shift of a given number'''
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    cyph_key = str.maketrans(ALPHABET,ALPHABET[key%26:]+ ALPHABET[0:key%26])
    return message.lower().translate(cyph_key)
assert Caeser_encrypt("hello",2) == 'jgnnq'
assert Caeser_encrypt("whatsup",2) == 'yjcvuwr'
print('The caeser encryption for "hello" with a shift of two is ',Caeser_encrypt("hello",2))
print('The caeser encryption for "whatsup" with a shift of two is ',Caeser_encrypt("whatsup",2))

def Caeser_decrypt(message:str,key:int)->str:
    '''decrypt a message according to a key with a shift of a given number'''
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    decyph_key = str.maketrans(ALPHABET[key%26:]+ ALPHABET[0:key%26],ALPHABET)
    return message.lower().translate(decyph_key)
assert Caeser_decrypt("jgnnq",2) == 'hello'
assert Caeser_decrypt("yjcvuwr",2) == 'whatsup'
print('The caeser decryption for "jgnnq" with a shift of two is ',Caeser_decrypt("jgnnq",2))
print('The caeser decryption for "yjcvuwr" with a shift of two is ',Caeser_decrypt("wyjcvuwr",2))
print()
print()
print('----part f.1----')
def print_line_numbers(str_list:'list of str')->None:
    '''prints each item of a list of strings with a number next to them'''
    for n in range(0,len(str_list)):
        print("{:2}:  {}".format(n,str_list[n]))
text = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        ","" ]
print_line_numbers(text)
def stats(str_list:'list of str')->None:
    '''prints statistics for a list of strings that print out number of lines,
    number of empty lines, averager characters per line, and average characters
    per non_empty line'''
    lines = len(str_list)
    e_lines = 0
    characters = 0
    for n in str_list:
        if len(n.strip()) < 1:
            e_lines += 1
        else:  
            characters += len(n)
    print("{:6} lines in the list".format(lines))
    print('{:6} empty lines'.format(e_lines))
    print("{:6.1f} average characters per line".format(characters/lines))
    print("{:6.1f} average characters per non-empty line".format(characters/(lines-e_lines)))
stats(text)
def list_of_words(L:'list of str')->'list of str':
    '''lists every word in a list of strings'''
    L_copy = L[:]
    words = []
    punc_key = str.maketrans("!@#$%&*()-_=+{}[]\|:;\"<,>.?/","                            ")
    for s in range(0,len(L_copy)):
        words += L_copy[s].translate(punc_key).split()
    return words
print(list_of_words(text))
print(Caeser_encrypt("hello friend",6))
    
