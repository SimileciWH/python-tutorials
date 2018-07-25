# 7-8,7-9test
sandwich_orders = ['san1','san2','san3','san1','san7','san1']
finish_sandwiches = []

while 'san1' in sandwich_orders:
    sandwich_orders.remove('san1')
    print('san1 is sale out')

while sandwich_orders :
    finish_sandwiche =  sandwich_orders.pop()
    print("I made your tun sandwich, "+finish_sandwiche)
    finish_sandwiches.append(finish_sandwiche)
print(sandwich_orders)
print(finish_sandwiches)


# 7-10test
prompt = 'If u could visit one place in the world, where would u go?'
name_place = {}
goon = ''
while True:
    name = input('你叫什么名字？')
    place = input('你最想去的地方是哪里？')
    name_place[name] = place
    print('Hi '+name+', 你最想去的地方是'+place)
    goon = input('是否继续输入（y/n）')
    if goon == 'n':
        break
