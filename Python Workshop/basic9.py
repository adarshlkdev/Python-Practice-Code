def sum(a , b):
    print(a+b)

sum(2 ,6) 

def greet(name , dish="Pasta"):
    print('Good Morning', name)
    print('Please eat',dish)

greet(input('Enter your name : ') , input('What do you want to eat : '))

def greetings(names):
    for name in names:
        print('Hello' , name)

names = ['Anuj' , 'Shivam' , 'Rohit']  

greetings(names)
    
