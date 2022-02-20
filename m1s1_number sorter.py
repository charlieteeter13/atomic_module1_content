#!/usr/bin/env python


#NUMBER OF INTEGERS
def get_input3():
    I = input('How many random numbers? Type: ')
    return I
inputted_text3 = get_input3()
number = inputted_text3
z = int(number)

#LOWER BOUND
def get_input():
    I = input('Lower bound? Type: ')
    return I
inputted_text = get_input()
low1 = inputted_text
x = int(low1)

#UPPER BOUND
def get_input2():
    I = input('Upper bound? Type: ')
    return I
inputted_text2 = get_input2()
up1 = inputted_text2
y = int(up1)

#GENERATE RANDOM LIST
import random
randomlist = []
for i in range (0, z):
    n = random.randint(x,y)
    randomlist.append(n)
print('Below is your list of random numbers.')
print(randomlist)

print('Now, here is your list of random numbers sorted in accending order.')

#SORT NUMBERS
sortedlist = []
while randomlist:
    minimum = randomlist[0]
    for x in randomlist: 
        if x < minimum:
            minimum = x
    sortedlist.append(minimum)
    randomlist.remove(minimum)
print(sortedlist)

#Completely forgot to do two separate script.
#for script one, save the list as a file
#for script two, just add in the step of inserting that file to be sorted.
