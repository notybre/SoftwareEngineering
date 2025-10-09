from pprint import pprint
my_dict = {'first':'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4= 13)
dict_maker(name='Роман', age=19, weight=55, eyes_color='brown')
pprint(my_dict)