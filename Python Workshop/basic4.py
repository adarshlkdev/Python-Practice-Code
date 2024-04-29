#String

print('''This is a
      multiline string if
         you are trying this with double
quote then you will get a error ''') 

#String concat 

city = 'Jaipur'
state = 'Rajasthan'

print(city + state)

city = "Jaipur"

print(city[-1])

my_char = city[3]

print(my_char)


#======Slicing in Strings==========

string = "Hello"

print(string[1:5])

print(string[:5])

print(string[2:])

print(string[0:5:2])

print(string , 'I am immutable')

#Reverse a string

print('Reverse string is',string[::-1])


#===loop in strings====

a = 'abc'

for my_char in a:
    print(my_char*2)


#some string pre defined methods

password = " absc%12 "

print(password.isalpha())
print(password.isdigit())
print(password.islower())
print(password.isupper())
print(password.upper())

print(password.lstrip())
print(password.rstrip())
