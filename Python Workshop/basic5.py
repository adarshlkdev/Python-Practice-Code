#list =>  It supports heteogenius items

my_list = ['Adarsh'  , 23 , 2.45 ]

my_list[1] = 'Aman'

print(my_list[0])

my_list.append(29)

print(my_list)

print(len(my_list))

del my_list[-1]

print(my_list)

for x in my_list:
    print(x)

del my_list

# List Comprehension is an elegant way to create a new list from an existing list

a = [x for x in range(100) if x%2==0]
print(a)

b = [3**i for i in range(10)]
print(b)
