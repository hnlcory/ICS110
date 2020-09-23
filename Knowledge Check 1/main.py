#COPY AND PASTE EVERYTHING BELOW INTO REPL.IT FOR YOUR KNOWLEDGE CHECK.

#SHARE YOUR REPL.IT WITH YOUR INSTRUCTOR AND SUBMIT THE LINK IN AT THE END/LAST QUESTION

#Statements Knowledge Check Repl.it Templat
#StatementsKnowledge Check
#Use for, .split(), and if to create a Statement that will print out words that start with 's':
# 1. st = 'Print only the words that start with s in this sentence'
#Code here
st = 'Print only the words that start with s in this sentence'
st =st.split(' ')

for letter in st:
    if letter[0][0] == 's':
        print(letter)


# 2. Use range() to print all the even numbers from 0 to 10.
#Code Here
for num in range(11):
    if num % 2 == 0:
        print(num)


# 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#Code here
lst= [x for x in range(51) if x % 2 != 0]
print(lst)

# 4. Go through the string below and if the length of a word is even print "even!"
#st = 'Print every word in this sentence that has an even number of letters'
#Code here
st = 'Print every word in this sentence that has an even number of letters'
words= list(st.split(' '))
for x in words:
    if len(x)%2==0:
        print(x)

# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#Code in this cell
for num in range(101):
    if num % 5 == 0 and num % 3 ==0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')


# 6. Use List Comprehension to create a list of the first letters of every word in the string below:
# st = 'Create a list of the first letters of every word in this string'
#Code here
st = 'Create a list of the first letters of every word in this string'
words = st.split()
for c in words:
    firstcharlst = c[0]
    print(firstcharlst)
