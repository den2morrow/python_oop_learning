'''
Подвиг 3.
Объявите класс с именем DataBase, который бы хранил в себе следующую информацию:

pk: 1
title: "Классы и объекты"
author: "Сергей Балакирев"
views: 14356
comments: 12
'''


class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


'''
Подвиг 4.
Объявите класс с именем Goods и пропишите в нем следующие атрибуты (переменные):

title: "Мороженое"
weight: 154
tp: "Еда"
price: 1024
Затем, после объявления класса, 
измените его атрибут price на значение 2048 и добавьте еще один атрибут:

inflation: 100
'''


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100


'''
Подвиг 5. Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:

model: "Тойота"
color: "Розовый"
number: "П111УУ77"
Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
'''


class Car:
    pass


setattr(Car, "model", "Тойота")
setattr(Car, "color", "Розовый")
setattr(Car, "number", "П111УУ77")

print(Car.__dict__['color'])


'''
Подвиг 6. Объявите класс с именем Notes и определите в нем следующие атрибуты:

uid: 1005435
title: "Шутка"
author: "И.С. Бах"
pages: 2
Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author.
'''


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, "author"))


'''
Подвиг 7. Объявите класс с именем Dictionary и определите в нем следующие атрибуты:

rus: "Питон"
eng: "Python"
Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута rus_word.
Если такого атрибута в классе нет, то функция getattr() должна возвращать булево значение False.
'''


class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, "rus_word", False))


'''
Подвиг 8. Объявите класс с именем TravelBlog и объявите в нем атрибут:

total_blogs: 0
Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:

name: 'Франция'
days: 6
Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.

Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два локальных свойства:

name: 'Италия'
days: 5
Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.

P.S. На экран ничего выводить не нужно.
'''


class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "Франция"
tb1.days = 6

TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = "Италия"
tb2.days = 5

TravelBlog.total_blogs += 1


'''
Подвиг 9. Объявите класс с именем Figure и двумя атрибутами:

type_fig: 'ellipse'
color: 'red'
Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:

start_pt: (10, 5)
end_pt: (100, 20)
color: 'blue'
Удалите из экземпляра класса свойство color
и выведите на экран список всех локальных свойств (без значений)
объекта fig1 в одну строчку через пробел в порядке, указанном в задании.
'''


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = "blue"

if 'color' in fig1.__dict__:
    del fig1.color

print(*fig1.__dict__)


'''
Подвиг 10. Объявите класс с именем Person и атрибутами:

name: 'Сергей Балакирев'
job: 'Программист'
city: 'Москва'
Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное свойство с именем job.
Выведите True, если оно присутствует в объекте p1 и False - если отсутствует.
'''


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print('job' in p1.__dict__)