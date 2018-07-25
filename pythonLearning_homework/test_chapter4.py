# 4-1,4-2test
favourite_pizzas = ['biske','sanwige','bubber']
for pizza in favourite_pizzas:
    print("I like "+pizza+' pizza.')
print("I really like pizza!")


print('hello\n')

# 4-3test
for num in range(1,21):
    print(num)

# 4-4,4-5test
num = []
for i in range(1,1000001):
    num.append(i)
print(num)
num_min = min(num)
num_max = max(num)
num_sum = sum(num)
print(num_min)
print(num_max)
print(num_sum)

# 4-6test
odd_num = []
for i in range(1,21,2):
    odd_num.append(i)
print(odd_num)

# 4-7test
num_3baishu = []
for i in range(3,30,3):
    num_3baishu.append(i)
    print(num_3baishu)


# 4-8test
for i in range(1,11):
    print(i**3)

# 4-9test
num_3 = [i**3 for i in range(1,11)]
print(num_3)



# 4-10test
a = []
for i in range(1,10):
    a.append(i)
print("The first three items in the list are: "+str(a[:3]))
print("Three items from the moddle of the list are: "+str(a[3:-3]))
print("The last three items in the list are: "+str(a[-3:]))

# 4-11test
friends_pizzas = favourite_pizzas[:]
favourite_pizzas.append('hot parries')
friends_pizzas.append('cold barrier')
print('My favourite pizzas are:\n')
print(favourite_pizzas)
print('My friend\'s favourite pizzas are:\n')
print(friends_pizzas)

# 4-12test
print('My favourite pizzas are:\n')
for i in range(0,len(favourite_pizzas)):
    print(favourite_pizzas[i])
print('===============================================')
print('My friend\'s favourite pizzas are:\n')
for j in range(0,len(friends_pizzas)):
    print(friends_pizzas[j])
