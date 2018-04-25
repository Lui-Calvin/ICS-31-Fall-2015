# Calvin Lui 84152100 & Patrick Hahn 15714896 lab section 9
from random import randrange
print('Calvin Lui 84152100 & Patrick Hahn 15714896 lab section 9')
print()
print()
print('---- c.1----')
surname_data = open('surnames.txt','r')
s_data = surname_data.read()
surnames = []
surnamA = s_data.split()
surname_data.close()
for gt in surnamA:
    if gt[0] in "QWERTYUIOPLKJHGFDSAZXCVBNM":
        surnames.append(gt)

female_data = open('femalenames.txt','r')
f_data = female_data.read()
female_names = []
fema = f_data.split()
female_data.close()
for y in fema:
    if y[0] in "QWERTYUIOPLKJHGFDSAZXCVBNM":
        female_names.append(y)

male_data = open('malenames.txt','r')
m_data = male_data.read()
male_names = []
ma = m_data.split()
male_data.close()
for y in ma:
    if y[0] in "QWERTYUIOPLKJHGFDSAZXCVBNM":
        male_names.append(y)

def create_single_name()-> str:
    '''generate a single random name—a random surname, a random choice of male or female, and a random first name chosen from that list'''
    gender = randrange(0,2)
    name = ''
    if gender == 0:
        name += female_names[randrange(0,len(female_names))]
    else:
        name += male_names[randrange(0,len(male_names))]
    name += " "
    name += surnames[randrange(0,len(surnames))]
    return name

def random_names(i:int)-> 'list of str':
    '''takes an integer and returns a list of that many strings, with each string a randomly generated name'''
    ret_str = []
    for n in range(0,i):
        ret_str.append(create_single_name())
    return ret_str
print("list of random names:")
for i in random_names(30):
    print(i)

print('---- part D.1 ----')
def Caesar_decrypt(message:str,key:int)->str:
    '''decrypt a message according to a key with a shift of a given number'''
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    decyph_key = str.maketrans(ALPHABET[key%26:]+ ALPHABET[0:key%26],ALPHABET)
    return message.lower().translate(decyph_key)

word_data = open('wordlist.txt')
word_list = word_data.readlines()
word_data.close()

def Caesar_break (x: str) -> str:
    ''' takes a ciphertext string (encrypted using a Caesar cipher as we did last week) and returns the plaintext
for that string, without having the key. '''
    max_matched = 0
    saved_phrase = ""
    for i in range(0,26):
        matched_words = 0
        test_str = Caesar_decrypt(x,i).split()
        for n in test_str:
            for word in word_list:
                if n+'\n' == word:
                    matched_words += 1
                    break
        if matched_words > max_matched:
            max_matched = matched_words
            saved_phrase = Caesar_decrypt(x,i)
    return saved_phrase
assert Caesar_break("nkrru lxoktj") == "hello friend"
assert Caesar_break("ifmmp") == "hello"
print('running the Caesar break on "nkrru lxoktj" is: ',Caesar_break("nkrru lxoktj"))
            
print()
print()
print("----part e----")


def copy_files(s:str):
    """Copies a file from the same directory as this file with a designated"""
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')
    page_num = 1
    if s == 'line numbers':
        for line in infile:
            outfile.write("{:6}: {}".format(page_num,line))
            page_num+=1
    elif s == 'Gutenberg trim':
        in_body = False
        for line in infile:
            if "*** END" in line:
                in_body = False
            if in_body:
                outfile.write(line)
            if "*** START" in line:
                in_body = True
    else:
        num_lines = 0
        e_lines = 0
        characters = 0
        for line in infile:
            if len(line.strip()) < 1:
                e_lines += 1
            else:
                characters += len(line)
            num_lines += 1
            outfile.write(line)
        if s == 'statistics':
            outfile.write("{:6} lines in the list".format(num_lines) + '\n' +
            "{:6} empty lines".format(e_lines)+ '\n' +
            "{:6.1f} average characters per line".format(characters/num_lines) + '\n' +
            "{:6.1f} average characters per non-empty line".format(characters/(num_lines-e_lines)))
    infile.close()
    outfile.close()
print("copying files with line numbers:")
copy_files("line numbers")
print("copying files with Gutenberg trim")
copy_files("Gutenberg trim")
print("copying files with statistics")
copy_files("statistics")
