#Objects and Data Structures Assessment Test Repl.it Template

 

#1. Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

(100*2/2)+0.50-0.25

#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

 

#Answer these three questions without typing code. Then type code to check your answer.

#2. What is the value of the expression 4 * (6 + 5)

 44

#3. What is the value of the expression 4 * 6 + 5 

 25

#4. What is the value of the expression 4 + 6 * 5 

 34

#5. What is the type of the result of the expression 3 + 1.5 + 4?

 Floating Point Number

#What would you use to find a number’s square root, as well as its square?

#6. Square root:

 number**0.5

#7. Square:

number**2


#STRINGS

#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

#8. Print out 'e' using indexing

s = 'hello'
print (s[1])

 

#9. Reverse the string using slicing

s ='hello'
s[::-1]
 

#Given the string hello, give two methods of producing the letter 'o' using indexing.



#Print out the 'o'

#10. Method 1:

 s ='hello'
s[4]

#Print out the 'o'

#11. Method 2:

mystring=('hello')[4]  

#NUMBERS

#Build this list [0,0,0] two separate ways.

#12. Method 1:

 my_list= ['0','0']
 my_list.append('0')

#13. Method 2:

 my_list= ['0','0']
new_list= ['0']
final_list= my_list + new_list
 
#Reassign 'hello' in this nested list to say 'goodbye' instead:

#14. list3 = [1,2,[3,4,'hello']]

 list3[2][2]='goodbye'

#Sort the list below:

#15. list4 = [5,3,4,6,1]

 list4.sort()

#DICTIONARIES

#Using keys and indexing, grab the 'hello' from the following dictionaries:

 

# d = {'simple_key':'hello'}

# 16. Grab 'hello'

 d['simple_key']

# d = {'k1':{'k2':'hello'}}

# 17.  Grab 'hello'

 d['k1']['k2']

# Getting a little tricker

# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#18. Grab hello

 d['k1'][0]['nest_key'][1]

# This will be hard and annoying!

# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

#19. Grab hello

 d['k1'][2]['k2'][1]['tough'][2][0]

#SETS

# Use a set to find the unique values of the list below:

# list5 = [1,2,2,33,4,4,11,22,3,3,2]

 set(list5)

#BOOLEAN

# Answer before running cell  2 > 3

 False

# Answer before running cell 3 <= 2

 False

# Answer before running cell  3 == 2.0

 False

# Answer before running cell  3.0 == 3

 True

# Answer before running cell  4**0.5 != 2

 False

# Final Question: What is the boolean output of the cell block below?

# two nested lists

# l_one = [1,2,[3,4]]
# l_two = [1,2,{'k1':4}]

# True or False?

# l_one[2][0] >= l_two[2]['k1']

False
