#input from user
'''
english_marks = int(input('Enter your marks in English :'))
hindi_marks = int(input('Enter your marks in Hindi :'))
maths_marks = int(input('Enter your marks in Maths :'))

avg_result = (english_marks + hindi_marks + maths_marks) / 3

print('Your avg marks are : ' ,avg_result)
'''

age = 5

if age > 18:
    print('You can vote')
else:
    print('Sorry you can not able to vote') 
print('This will always executed')  

num = 2.4

if num>0:
    print('Postitve number')
elif num==0:
    print('Zero')
else:
    print('Negative number')  

#Range function

a = list(range(10)) 
b = list(range(3 , 10))            #Here first number is inclusive & second one is exclusive
c = list(range(3 , 10 , 2))
print(a)
print(b)
print(c)
