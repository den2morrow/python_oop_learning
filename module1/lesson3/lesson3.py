'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/nT_sMhJsw1E

Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.

P.S. На экран в программе ничего выводить не нужно.
'''


class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)


'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DEyOq7Gpko4

Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), а третий необязательный аргумент - цвет точки (локальное свойство color). Если цвет не указывается, то он по умолчанию принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points укажите цвет 'yellow'.

P.S. На экран в программе ничего выводить не нужно.
'''


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


cnt = 1
points = [Point(1, 1), Point(3, 3, 'yellow')]
cnt = 5

for i in range(998):
    points.append(Point(cnt, cnt))
    cnt += 2


'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/bPH4It1_d0c

Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
'''

import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


classes = (Line, Rect, Ellipse)
elements = []
for _ in range(217):
    random_class = random.choice(classes)
    a, b, c, d = (random.random() for _ in range(4))

    obj = random_class(a, b, c, d)
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)

    elements.append(obj)


'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Vr4c1LgE91o

Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
'''


def check_numbers(nums):
    for num in nums:
        if not (type(num) in (int, float)):
            return False
    return True


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not check_numbers((self.a, self.b, self.c)) or self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        elif not (self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b):
            return 2
        else:
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/a3Har3Z_89Q

Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:

gr_1 = Graph(data)
где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса должны формироваться следующие локальные свойства:

data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);

В этом классе объявите следующие методы:

set_data(self, data) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.

Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение:

"Отображение данных закрыто"

Прочитайте из входного потока числовые данные с помощью команды:

data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show() со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться две соответствующие строки.

Sample Input:

8 11 10 -32 0 7 18
Sample Output:

Столбчатая диаграмма: 8 11 10 -32 0 7 18
Отображение данных закрыто
'''


class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {self.data}")
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {self.data}")
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))

qr = Graph(data_graph)
qr.show_bar()
qr.set_show(False)
qr.show_table()


'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZTCdEB_6h1I

Подвиг 7. Объявите в программе следующие несколько классов:

CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory, максимум N - по числу слотов памяти на материнской плате (N = 4).

Объекты классов должны иметь следующие локальные свойства:

для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).

P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.
'''


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots=None, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        memorys = 'Память: '
        for i in range(len(self.mem_slots)):
            memorys += f'{self.mem_slots[i].name}-{self.mem_slots[i].volume};'

        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name},{self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                memorys[:-1]]


cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])


'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI

Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
'''


class Cart:
    def __init__(self, goods=None):
        self.goods = goods if goods is not None else []

    def add(self, gd):  # - добавление в корзину товара, представленного объектом gd;
        self.goods.append(gd)

    def remove(self, indx):  # - удаление из корзины товара по индексу indx;
        del self.goods[indx]

    def get_list(self):  # - получение из корзины товаров в виде списка из строк:
        return [f'{good.name}: {good.price}' for good in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
tv1, tv2 = TV('Philips', 1000), TV('Samsung', 2500)
table = Table('Origon', 340)
notebook1, notebook2 = Notebook('MacBook', 2800), Notebook('MSI', 2500)
cup = Cup('Boss', 20)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(notebook1)
cart.add(notebook2)
cart.add(cup)


'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/3WfWCBKRKIM

Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ

Подвиг 9. Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не хранить, а формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:



Для этого объявите в программе класс ListObject, объекты которого создаются командой:

obj = ListObject(data)
Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся строки из списка lst_in (первая строка в первом объекте, вторая - во втором и  т.д.). На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.

P.S. В программе что-либо выводить на экран не нужно.

Sample Input:

1. Первые шаги в ООП
1.1 Как правильно проходить этот курс
1.2 Концепция ООП простыми словами
1.3 Классы и объекты. Атрибуты классов и объектов
1.4 Методы классов. Параметр self
1.5 Инициализатор init и финализатор del
1.6 Магический метод new. Пример паттерна Singleton
1.7 Методы класса (classmethod) и статические методы (staticmethod)
Sample Output:
'''


import sys


class ListObject:
    def __init__(self, data='', next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(data=lst_in[0])


def add_to_end(head, item):
    list_node = ListObject(item)
    while head.next_obj:
        head = head.next_obj
    head.link(list_node)


for lst in lst_in[1:]:
    add_to_end(head_obj, lst)


'''

'''


import random


def get_total_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for f in range(-1, 2):
            x = k + i
            y = f + j
            if x < 0 or y < 0 or x >= 10 or y >= 10:
                continue
            if pole[x][y].mine:
                n += 1
    return n


class GamePole:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.mines = [True] * m + (n * n - m) * [False]
        random.shuffle(self.mines)
        self.pole = [[Cell(0, self.mines.pop()) for _ in range(n)] for _ in range(n)]
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                self.pole[i][j].around_mines = get_total_mines(self.pole, i, j)

    def init(self):
        pass

    def show(self):
        for line in self.pole:
            for cell in line:
                if cell.fl_open:
                    if cell.mine:
                        print('0', end=' ')
                    else:
                        print(cell.around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False, fl_open: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


pole_game = GamePole(10, 12)
