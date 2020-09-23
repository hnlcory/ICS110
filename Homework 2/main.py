#A school has the following rules for grading system, using an if statement ask the user to enter marks and print the corresponding grade

score= int(input('Enter Score out of 100 \n'))
if score<=100 and score>=81:
    print('Your grade is an A')
elif score<=80 and score >=61:
    print('Your grade is a B')
elif score<=60 and score >=51:
    print('Your grade is a C')
elif score<=50 and score >=46:
    print('Your grade is a D')
elif score<=45 and score>=26:
    print('Your grade is a E')
elif score<=25 and score>=1:
    print('Your grade is a F')

#Count the total number of digits in a number using a while statement
Num= 75869
Count= 0
while Num > 0:
  Num = Num // 10
  Count = Count +1
print(Count)
    
#Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
for num in list1[::-1]:
    print(num)
 
