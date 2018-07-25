# 8-1test
def display_message():
    # 显示以下我想显示的内容
    print('I love this world!')

display_message()


# 8-2test
def favourite_book(title):
    print('one of my favourite books is '+title+'.')

favourite_book('Alice in Wonderland')


# 8-3,8-4test
def make_shirt(size,contents = 'I love Python'):
    prompt = 'The shirt size is '+str(size)+', and content is '+contents
    print(prompt)
make_shirt(42)
make_shirt(10)
make_shirt(42,'classic')


# 8-5test
def describe_city(cityName,country = 'anhui'):
    prompt = '\n'+cityName.title() +' is in '+country.title()
    print(prompt)
describe_city(cityName = 'wuhu')
describe_city('hefei')
describe_city('nanjing','jiangsu')

# 8-6test
def describe_city(cityName,country = 'anhui'):
    prompt = '\n'+cityName.title() +' is in '+country.title()
    return prompt
dis0 = describe_city('wuhu')
dis1 = describe_city('hefei')
dis2 = describe_city('nanjing','jiangsu')
print('\n'+dis0+'\n'+dis1+'\n'+dis2)

# 8-7.8-8test
def make_album(singerName,albumName,num = ''):
    album = {
    'Name':singerName,
    'albumName':albumName,
    }
    if num:
        album['num'] = num
    return album

# list0 = make_album('tolar swift','famous')
# list1 = make_album('jj','world')
# list2 = make_album('zhm','flowers','7')
# print(list0)
# print(list1)
# print(list2)

while True:
    singerName = input('\t\t\tPlease input \'q\' to exit!!!'+'\nPlease input a singer\'s name:')
    if singerName == 'q':
        break
    albumName = input('Please inputer this singer\'s album name:')
    if albumName == 'q':
        break
    num = input('If u know how many songs in that album, please input. Otherwise input "enter"!')
    if num == 'q':
        break
    album = make_album(singerName,albumName)
    if num:
        album['naum'] = num
    print(album)
