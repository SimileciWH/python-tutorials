#!usr/bin/env python3
#-*- coding : utf-8 -*-
# 9-1,9-2test
class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        '''随便创建一个餐厅的信息'''
        self.name = restaurant_name
        self.type = restaurant_type

    def describle_restaurant(self):
        print('This restaurant is called '+self.name.title()+', and it\'s a '+self.type.title()+' kind restaurant.')

    def open_restaurant(self):
        print('The restaurant is now openning all day!')

restaurant = Restaurant('jinlin','chinese')
restaurant.describle_restaurant()
restaurant.open_restaurant()

# 9-3test
class User():
    def __init__(self,first_name,last_name,telephone,home):
        self.firstName = first_name
        self.lastName = last_name
        self.tel = telephone
        self.home = home

    def describe_user(self):
        fullname = self.firstName.title() +' '+self.lastName.upper()
        prompt = fullname+' is live in '+self.home.title()+', phone number is: '+str(self.tel)
        print(prompt)

    def greet_user(self):
        prompt = 'Hello, '+self.firstName+' '+self.lastName+' have a nice day!'
        print(prompt)

person = User('simileci','wh',17626026632,'changzhou')
person.describe_user()
person.greet_user()

# 9-4test
class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        '''随便创建一个餐厅的信息'''
        self.name = restaurant_name
        self.type = restaurant_type
        self.number_served = 0

    def describle_restaurant(self):
        print('This restaurant is called '+self.name.title()+', and it\'s a '+self.type.title()+' kind restaurant.')

    def open_restaurant(self):
        print('The restaurant is now openning all day!')

    def set_number_served(self,number_served):
        prompt = 'There have '+str(number_served)+' people eated!'
        print(prompt)
restaurant2 = Restaurant('jinlin','chinese')
restaurant2.open_restaurant()
restaurant2.describle_restaurant()
restaurant2.set_number_served(20)

# 9-6test
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,restaurant_type,flavors):
        super().__init__(restaurant_name,restaurant_type)
        self.flavors = flavors

    def display_icecream(self):
        # 子类无法访问父类的参数，失败的尝试如下：
        # prompt = 'The'+self.restaurant_name.title()+' restaurant is a '+self.restaurant_type.title()
        # prompt += ' kind of restaurant.\n'+'The ice-cream with following adds:\n\t'
        # print(prompt)
        print('The ice-cream with following adds:\n\t')
        for flavor in self.flavors:
            print(flavor)

ice = IceCreamStand('jinlin','chinese',['123','456','chese','lalala'])
ice.open_restaurant()
ice.describle_restaurant()
ice.display_icecream()
