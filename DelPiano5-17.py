#Program Name: ASCII Characters
#Student Name: Sergio Del Piano
#''' My submission of this program indicates that I have neither received nor given substantial
#unauthorized assistance in writing this program. I worked [alone / with xxx, xxx, xxx] on this assignment.'''

#Assigning Count a Value
count = 0

#For statement presents order of ASCII values
for i in range(ord('!'),ord('~')+1):

#chr then returns the ASCII symbols
    print(chr(i),end=' ')
    count = count + 1

    #If Statement to make characters move to next line if 10 characters are printed
    if count == 10:
        count = 0
        print()
