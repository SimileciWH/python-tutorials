
# 6-1test
friend_info = {
'first_name':'david',
'last_name':'geng',
'age':'25',
'city':'suzhou',
}

print(friend_info['first_name'].title())
print(friend_info['last_name'].title())
print(friend_info['age'])
print(friend_info['city'].upper())

# 6-2test
favourite_nums = {
'jams':'12',
'marry':'3',
'ketty':'45',
'sam':'32',
'simileci':'32',
}
print("jams's favourite number is: "+favourite_nums['jams'])
print("marry's favourite number is: "+favourite_nums['marry'])
print("ketty's favourite number is: "+favourite_nums['ketty'])
print("sam's favourite number is: "+favourite_nums['sam'])
print("simileci's favourite number is: "+favourite_nums['simileci'])


# 6-4test
favourite_nums = {
'jams':'12',
'marry':'3',
'ketty':'45',
'sam':'32',
'simileci':'32',
}
for key,value in favourite_nums.items():
    print('\t'+key+"'s favourite number is: "+value)


# 6-5test
country_rivers = {
'amazon':'america',
'huanghe':'china',
'youfaladi':'africa',
}
for river_name,through in country_rivers.items():
    print('The '+river_name.title()+' runs through '+through.title())
print('river_name:\n')

for river_name in country_rivers.keys():
    print(river_name.title())
print('through country:\n')

for through in country_rivers.values():
    print(through.title())

# 6-7test
friend_info_0 = {
'first_name':'david',
'last_name':'geng',
'age':'25',
'city':'suzhou',
}
friend_info_1 = {
'first_name':'curcy',
'last_name':'wu',
'age':'21',
'city':'hangzhou',
}
friend_info_2 = {
'first_name':'simileci',
'last_name':'wang',
'age':'18',
'city':'wuhu',
}

friends = [friend_info_0, friend_info_1, friend_info_2]

for friend in friends:
    friend_fullname = friend['first_name']+' '+friend['last_name']
    print('\n\t'+friend_fullname)
    print('\n\t'+friend['age'])
    print('\n\t'+friend['city']+'\n')

# 6-10test
favourite_nums = {
'jams':['12','13','14'],
'marry':['10','3','7','6'],
'ketty':['45','46','89'],
'sam':['32','23','2233'],
'simileci':['26','27'],
}
for name,num in favourite_nums.items():
    print('\n\t'+name+"'s favourite nums are:\n")
    for i in num:
        print(i)

# 6-11test
cities = {
'nanjing':{
        'country':'china',
        'population':'260000',
        'fact':'nice place',
        },
'shanghai':{
        'country':'china',
        'population':'360000',
        'fact':'modern city',
        },
'wuhu':{
    'country':'china',
    'population':'120000',
    'fact':'more rain && trees',
    },
}
for country,features in cities.items():
    print('\ncity name:\t'+country.title()+'\n')
    # print(features)
    for key,value in features.items():
        print(key.title()+'----'+value.title())
