# Подвиг 3

# class Book:
#     def __init__(self, title: str = '', author: str = '', pages: int = 0, year: int = 0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year

#     def __setattr__(self, key, value):
#         if (key == 'title' or key == 'author') and type(value) is str:
#             object.__setattr__(self, key, value)
#         elif (key == 'pages' or key == 'year') and type(value) is int:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваемых данных.")


# book = Book(title='Python ООП', author='Сергей Балакирев', pages=123, year=2022)


# Подвиг 4

# class Product:
#     NEW_ID = 0

#     def __init__(self, name: str, weight, price):
#         self.id = self.NEW_ID + 1
#         self.NEW_ID += 1
#         self.name = name
#         self.weight = weight
#         self.price = price

#     def __setattr__(self, key, value):
#         condition = (key == "id" and type(value) is int) or \
#                     (key == "name" and type(value) is str) or \
#                     ((key == "weight" or key == "price") and (type(value) is int or type(value) is float) and value > 0)
#         if condition:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваемых данных.")

#     def __delattr__(self, name):
#         if name == "id":
#             raise AttributeError("Атрибут id удалять запрещено.")
#         object.__delattr__(self, name)


# class Shop:
#     def __init__(self, name: str):
#         self.name = name
#         self.goods = []

#     def add_product(self, product: Product):
#         self.goods.append(product)

#     def remove_product(self, product: Product):
#         self.goods.remove(product)


# # Подвиг 5

# class LessonItem:
#     def __init__(self, title: str, practices: int, duration: int):
#         self.title = title
#         self.practices = practices
#         self.duration = duration

#     def __setattr__(self, key, value):
#         condition = (key == "title" and type(value) is str) or \
#                     (key == "practices" and type(value) is int and value > 0) or \
#                     (key == "duration" and type(value) is int and value > 0)

#         if condition:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваемых данных.")

#     def __getattr__(self, name):
#         return False

#     def __delattr__(self, name):
#         if name == "title" or name == "practices" or name == "duration":
#             pass
#         else:
#             object.__delattr__(self, name)


# class Module:
#     def __init__(self, name: str):
#         self.name = name
#         self.lessons: list[LessonItem] = []

#     def add_lesson(self, lesson: LessonItem):
#         self.lessons.append(lesson)

#     def remove_lesson(self, indx: int):
#         del self.lessons[indx]


# class Course:
#     def __init__(self, name: str):
#         self.name = name
#         self.modules: list[Module] = []

#     def add_module(self, module: Module):
#         self.modules.append(module)

#     def remove_module(self, indx: int):
#         del self.modules[indx]


# # Подвиг 6

# class Picture:
#     def __init__(self, name: str, author: str, descr: str):
#         self.name = name
#         self.author = author
#         self.descr = descr


# class Mummies:
#     def __init__(self, name: str, location: str, descr: str):
#         self.name = name
#         self.location = location
#         self.descr = descr


# class Papyri:
#     def __init__(self, name: str, date: str, descr: str):
#         self.name = name
#         self.date = date
#         self.descr = descr


# class Museum:
#     def __init__(self, name: str):
#         self.name: str = name
#         self.exhibits: list = []

#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)

#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)

#     def get_info_exhibit(self, indx: int) -> str:
#         return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"


# Подвиг 7

class AppVK:
    def __init__(self):
        self.name = "Вконтакте"


class AppYouTube:
    def __init__(self, memory_max: int):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list: dict):
        self.name = "Phone"
        self.phone_list = phone_list


class SmartPhone:
    def __init__(self, model: str):
        self.model: str = model
        self.apps: list = []

    def add_app(self, app):
        if any([app.__class__ == my_app.__class__ for my_app in self.apps]):
            return
        self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


# Подвиг 8

# class Circle:
#     def __init__(self, x, y, radius):
#         self.__x, self.__y = x, y
#         self.__radius = radius

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, value):
#         self.__x = value

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, value):
#         self.__y = value

#     @property
#     def radius(self):
#         return self.__radius

#     @radius.setter
#     def radius(self, value):
#         if value > 0:
#             self.__radius = value

#     def __setattr__(self, name, value):
#         if type(value) is int or type(value) is float:
#             object.__setattr__(self, name, value)
#         else:
#             raise TypeError('Неверный тип присваиваемых данных.')

#     def __getattr__(self, name):
#         return False


# Подвиг 9

# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000

#     def __init__(self, a: int | float, b: int | float, c: int | float):
#         self.__a = a
#         self.__b = b
#         self.__c = c

#     @property
#     def a(self):
#         return self.__a

#     @a.setter
#     def a(self, value):
#         self.__a = value

#     @property
#     def b(self):
#         return self.__b

#     @b.setter
#     def b(self, value):
#         self.__b = value

#     @property
#     def c(self):
#         return self.__c

#     @c.setter
#     def c(self, value):
#         self.__c = value

#     def __setattr__(self, name, value):
#         if name == "_Dimensions__a" or name == "_Dimensions__b" or name == "_Dimensions__c":
#             if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
#                 object.__setattr__(self, name, value)
#         elif name == "MAX_DIMENSION" or name == "MIN_DIMENSION":
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")


# Подвиг 10

import time


class Mechanical:
    def __init__(self, date: int | float):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return None
        return object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date: int | float):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return None
        return object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date: int | float):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return None
        return object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = [0, 0, 0]

    def add_filter(self, slot_num: int, filter):
        if slot_num == 1 and isinstance(filter, Mechanical):
            if self.filters[slot_num - 1] == 0:
                self.filters[slot_num - 1] = filter
        elif slot_num == 2 and isinstance(filter, Aragon):
            if self.filters[slot_num - 1] == 0:
                self.filters[slot_num - 1] = filter
        elif slot_num == 3 and isinstance(filter, Calcium):
            if self.filters[slot_num - 1] == 0:
                self.filters[slot_num - 1] = filter

    def remove_filter(self, slot_num: int):
        if self.filters[slot_num - 1] != 0:
            self.filters[slot_num - 1] = 0

    def get_filters(self):
        return tuple(fil for fil in self.filters if fil != 0)

    def water_on(self):
        for fil in self.filters:
            if not (fil != 0 and 0 <= time.time() - fil.date <= self.MAX_DATE_FILTER):
                return False
        return True
