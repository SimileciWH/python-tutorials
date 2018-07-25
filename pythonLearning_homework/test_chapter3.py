# 3-1test
names = ['david','jone','smith','herry','johon']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())


# 3-2test
message = ' have a nice day.'
print(names[0].title()+message)
print(names[1].title()+message)
print(names[2].title()+message)
print(names[3].title()+message)
print(names[4].title()+message)

# 3-4,3-5,3-6,3-9test
invite_gust = ['davad','brown','zanmus','ketty','smith']
print(invite_gust)
# absent_invite_gust = invite_gust.pop(3)
absent_invite_gust = 'ketty'
invite_gust.remove(absent_invite_gust)
print(absent_invite_gust.title()+" can't appear!\n")

invite_gust.append('nancy')
print(invite_gust)
print('==================================================================\n')
print('I have found a bigger table, we need to invite three more friends.\n')
print('==================================================================\n')
add_gust = ['peter','garry','wallim']
invite_gust.insert(0,add_gust[0])
invite_gust.insert(3,add_gust[1])
invite_gust.append(add_gust[2])
print(invite_gust)
num = len(invite_gust)
# print('\t\t'+str(num)+'\n')
print(num)


# 3-8test
beautiful_place = ['parries','newyork','lasvegos','russia','germany']
print("It is original list:\n")
print(beautiful_place)
print("It is sorted list:\n")
print(sorted(beautiful_place))
print("It is sorted reverse list:\n")
print(sorted(beautiful_place,reverse = True))

beautiful_place.reverse()
print(beautiful_place)

beautiful_place.reverse()
print(beautiful_place)

beautiful_place.sort()
print(beautiful_place)

beautiful_place.sort(reverse = True)
print(beautiful_place)
