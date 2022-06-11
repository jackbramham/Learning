'''
Classes can be used to create your own datatype 

'''
class Cookie:
    def __init__(self, color):          # this is called the constructor
        self.color = color              # if it has self then it is a method which is part of a class

    def get_color(self):
        return self.color 

    def set_color(self, color):
        self.color = color 


cookie_1 = Cookie('green')
cookie_2 = Cookie('blue')

print('cookie 1 is colour', cookie_1.get_color())
print('cookie 2 is colour', cookie_2.get_color())

cookie_1.set_color('yellow')

print('cookie 1 is colour', cookie_1.get_color())
print('cookie 2 is colour', cookie_2.get_color())

