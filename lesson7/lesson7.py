# # Подвиг 3

# class Clock:
#     def __init__(self, time: int = 0):
#         self.__time = time

#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm

#     def get_time(self):
#         return self.__time

#     @classmethod
#     def __check_time(cls, tm):
#         return type(tm) is int and 0 <= tm <= 100_000


# clock = Clock(4530)


# # Подвиг 4

# class Money:
#     def __init__(self, money):
#         self.__money = money

#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money

#     def get_money(self):
#         return self.__money

#     def add_money(self, from_money):
#         self.__money += from_money.get_money()

#     @classmethod
#     def __check_money(cls, money):
#         return type(money) is int and money >= 0


# # Подвиг 6

# class Book:
#     def __init__(self, author, title, price):
#         self.set_author(author)
#         self.set_title(title)
#         self.set_price(price)

#     def set_title(self, title):
#         self.__title = title

#     def set_author(self, author):
#         self.__author = author

#     def set_price(self, price):
#         self.__price = price

#     def get_title(self):
#         return self.__title

#     def get_author(self):
#         return self.__author

#     def get_price(self):
#         return self.__price


# # Подвиг 7

# class Line:
#     def __init__(self, *args):
#         self.__x1, self.__y1, self.__x2, self.__y2 = args

#     def set_coords(self, *args):
#         self.__x1, self.__y1, self.__x2, self.__y2 = args

#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2

#     def draw(self):
#         print(self.__x1, self.__y1, self.__x2, self.__y2)


# # Подвиг 8

# class Point:
#     def __init__(self, *args):
#         self.__x, self.__y = args

#     def get_coords(self):
#         return self.__x, self.__y


# class Rectangle:
#     def __init__(self, *args):
#         if type(args[0]) is Point and type(args[1]) is Point:
#             self.__sp = args[0]
#             self.__ep = args[1]
#         else:
#             self.__sp = Point(args[0], args[1])
#             self.__ep = Point(args[2], args[3])

#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep

#     def get_coords(self):
#         return self.__sp, self.__ep

#     def draw(self):
#         print(f"Прямоугольник с координатами: ({self.__sp.get_coords()}) ({self.__ep.get_coords()})")


# rect = Rectangle(0, 0, 20, 34)


# Подвиг 9

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = self.tail = obj
            self.head.set_prev(None)
            self.tail.set_next(None)
        else:
            self.tail.set_next(obj)
            prev = self.tail
            self.tail = self.tail.get_next()
            self.tail.set_prev(prev)
            self.tail.set_next(None)

    def remove_obj(self):
        if self.tail is None:
            pass
        elif self.tail.get_prev() is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        result = []
        head = self.head

        if head is None:
            return []

        while head:
            result.append(head.get_data())
            head = head.get_next()
        return result


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_data(self, data):
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']


# Подвиг 10
import random


class EmailValidator:
    CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls) -> str:
        return ''.join(random.sample(cls.CHARS, 30)) + '@gmail.com'

    @classmethod
    def check_email(cls, email) -> bool:
        if cls.__is_email_str(email) and all([ch in cls.CHARS for ch in email]):
            dog = email.find('@')
            if len(email[:dog]) <= 100 and len(email[dog + 1:]) <= 50:
                if '.' in email[dog + 1:] and '..' not in email:
                    return True
        return False

    @staticmethod
    def __is_email_str(email):
        return type(email) is str
