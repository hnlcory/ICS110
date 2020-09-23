# Cory Parker

# 7/10/2020

# Assignment 1
#1
##################
#INSTRUCTOR COMMENTS
#You went above and beyond in #8 and made it interesting and interactive. Nice touch.You answered everything correctly. 
##################

print("Twinkle, twinkle, little star,\n\n   How I wonder what you are! \n\n  Up above the world so high, \n\n  Like a diamond in the sky. \n\n                Twinkle, twinkle, little star, \n\nHow I wonder what you are\n")

#2
a= input('Input Raduis \n')
print("Your radius =", a)
float(a)
b=3.14*float(a)**2
print('Area =', b)

#3
first=('cory') 
middle=('lyle')
last=('parker')
firstI=first[::-1]
middleI=middle[::-1]
lastI=last[::-1]
endI=firstI+' '+middleI+' '+lastI
print(endI)

#4
middle1=endI[5:9]
middle2=middle1[::-1]
print(middle2)

#5
a=96706,96701,96703,96815,96816
ziplist=list(a)
print('List Example:', ziplist)
ziptuple=(a)
print('Tuple Example:', ziptuple)

#6
ziplist.pop(1)
print('List Pop:', ziplist)
ziplist.append('Added Text')
print('List Append:', ziplist)
ziplist.reverse()
print('List Reverse:', ziplist)
ziplist.pop(0)
ziplist.sort()
print('List Sort:', ziplist)

#7
island_dict={'Maui':'Lahaina','Oahu':'Ewa','Kauai':'Lihue','Big Island':'Keauhou','Molokai':'Kalaupapa','Lanai':'Lanai City'}
print(island_dict['Oahu'])

#8
pdict={'Dad':'Eric','Mom':'May','Grandma':'Grace','Grandpa':'Ed','Dog':'Oreo'}
pinput=input('Select Family Member \nMom, Dad, Grandma, Grandpa, Dog\n')
print('You selected',pinput)
presult= pdict[pinput]   
print('Their name is:',presult)

#9
fname_inp=input('Enter your first name:')
lname_inp=input('Enter your last name:')
month_inp=input('Enter your date of birth:Month?')
day_inp=input('Enter your date of birth:Day?')
year_inp=input('Enter your date of birth:Year?')
print('%s %s was born on %s %s %s' %(fname_inp,lname_inp,month_inp,day_inp,year_inp))
