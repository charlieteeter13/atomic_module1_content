#!/usr/bin/env python

print('hello world')

# ints
a = 1
b = 2
c = a + b
print ('c = ' + str(c))

# floats
d = 3. 
e = 2.
f = d/e

print('f = ' + str(f))

# strings
string = 'I am a string of characters'
print(string)

# booleans
a = True
b = False
c = None
print( a == b ) # False
print (d > e) # True
print ( a is b ) # False

# lists
l = [1, 2, 3]

print(l)
print(l[0]) # prints only 1
print(l[-1]) # negative indices, prints last element (3)

# dictionaries
d = {
    'school' : 'Hopkins',
    'class':'ATOMIC',
}

# files (explicit open/close)
f = open('HEMI M1S1.py', 'r') #w, a
text = f.read()
print(text)
f.close()

# files (more foolproof) (closes everything for you)
with open('HEMI M1S1.py','r') as f:
    counter = 0
    for line in f:
        print('%d: %s' % (counter, line))
        counter += 1
    print('eof')

# loops (for)
print(l)
for element in l:
    print(element)
print(d)
for key in d:
    print(key, d[key])

for i in range(10, 20):
    print(i) #creates a list that goes over that range

# loops (while)
a = 10
while a < 20:
    print(a)
    a+=2

# functions
def get_input():
    I = input('Type something: ')
    return I

inputted_text = get_input()
print(inputted_text)

def check_length(string):
    if len(string) < 1:
        print('Empty')
    elif len(string) <2:
        print('Character')
    else:
        orint('String')

check_length(get_input())


            





