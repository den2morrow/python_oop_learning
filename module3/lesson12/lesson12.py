# Подвиг 2

# import sys


# class Book:
#     def __init__(self, *args) -> None:
#         print(args)
#         self.title, self.author, self.pages = args[0], args[1], args[2]

#     def __str__(self) -> str:
#         return f"Книга: {self.title}; {self.author}; {self.pages}"


# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка из входного потока (эту строчку не менять)
# print(Book(*lst_in))


# Подвиг 3

# class Model:
#     def __init__(self) -> None:
#         self.dct_query = dict()

#     def query(self, **kwargs):
#         for key, val in kwargs.items():
#             self.dct_query[key] = val

#     def __str__(self) -> str:
#         result = "Model:"

#         if len(self.dct_query) > 1:
#             for key, val in self.dct_query.items():
#                 result += f" {key} = {val},"
#             return result[:-1]
#         else:
#             return result[:-1]


# Подвиг 4

# class WordString:
#     def __init__(self, string="") -> None:
#         self.__string = string
#         self.all_words = [word for word in self.string.split() if word != ' ']

#     @property
#     def string(self) -> str:
#         return self.__string

#     @string.setter
#     def string(self, value) -> None:
#         self.__string = value

#     def __len__(self) -> int:
#         return len(self.all_words)

#     def __call__(self, indx):
#         if 0 <= abs(indx) <= len(self):
#             return self.all_words[indx]


# Подвиг 5

# class ObjList:
#     def __init__(self, data, next=None, prev=None) -> None:
#         self.__data = data
#         self.__next = next
#         self.__prev = prev

#     @property
#     def data(self):
#         return self.__data

#     @data.setter
#     def data(self, value):
#         self.__data = value

#     @property
#     def next(self):
#         return self.__next

#     @next.setter
#     def next(self, value):
#         self.__next = value

#     @property
#     def prev(self):
#         return self.__prev

#     @prev.setter
#     def prev(self, value):
#         self.__prev = value


# class LinkedList:
#     def __init__(self, head=None, tail=None) -> None:
#         self.head = head
#         self.tail = tail

#     def add_obj(self, obj) -> None:
#         if self.head is None:
#             self.head = obj
#             self.tail = obj
#         else:
#             h = self.head
#             while h.next:
#                 h = h.next
#             h.next = obj
#             self.tail = h.next
#             self.tail.prev = h

#     def remove_obj(self, indx) -> None:
#         cnt = 0
#         h = self.head
#         while indx != cnt:
#             cnt += 1
#             h = h.next
#         if len(self) == 2 and indx == 1:
#             self.tail = self.head
#             self.head.next = None
#         elif len(self) == 2 and indx == 0:
#             self.head = self.tail
#             self.tail.prev = None
#         elif len(self) == 1:
#             self.head = None
#             self.tail = None
#         else:
#             h.prev.next = h.next

#     def __len__(self) -> int:
#         cnt = 0
#         h = self.head
#         while h:
#             cnt += 1
#             h = h.next
#         return cnt

#     def __call__(self, indx):
#         cnt = 0
#         h = self.head
#         while indx != cnt:
#             cnt += 1
#             h = h.next
#         return h.data


# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1)  # s = Balakirev


# Подвиг 6

# class Complex:
#     def __init__(self, real: int | float, img: int | float) -> None:
#         self.__real = real
#         self.__img = img

#     @property
#     def real(self) -> int | float:
#         return self.__real

#     @real.setter
#     def real(self, value) -> None:
#         if type(value) in (int, float):
#             self.__real = value
#         else:
#             raise ValueError("Неверный тип данных.")

#     @property
#     def img(self) -> int | float:
#         return self.__img

#     @img.setter
#     def img(self, value) -> None:
#         if type(value) in (int, float):
#             self.__img = value
#         else:
#             raise ValueError("Неверный тип данных.")

#     def __abs__(self):
#         return (self.real * self.real + self.img * self.img) ** 0.5


# cmp = Complex(real=7, img=8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)


# Подвиг 7

# class RadiusVector:
#     def __init__(self, *args) -> None:
#         if len(set(args)) < 2:
#             self.coords = [0 for _ in range(args[0])]
#         else:
#             self.coords = [arg for arg in args]

#     def set_coords(self, *coords) -> None:
#         length = len(coords) if len(coords) <= len(self.coords) else len(self.coords)
#         for i in range(length):
#             self.coords[i] = coords[i]

#     def get_coords(self) -> tuple[int, ...]:
#         return tuple(self.coords)

#     def __len__(self) -> int:
#         return len(self.coords)

#     def __abs__(self):
#         result = 0
#         for coord in self.coords:
#             result += coord * coord
#         return result ** 0.5


# vector3D = RadiusVector(3)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
# vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
# res_len = len(vector3D)  # res_len = 3
# res_abs = abs(vector3D)


# Подвиг 8

# class Clock:
#     def __init__(self, hours: int, minutes: int, seconds: int) -> None:
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def get_time(self) -> int:
#         return self.hours * 3600 + self.minutes * 60 + self.seconds


# class DeltaClock:
#     def __init__(self, clock1: Clock, clock2: Clock) -> None:
#         self.clock1 = clock1
#         self.clock2 = clock2

#     def __str__(self):
#         # delta_time = ... -> if delta_time < 0 then ...
#         hours = self.clock1.hours - self.clock2.hours if self.clock1.hours - self.clock2.hours > 0 else 0
#         minutes = self.clock1.minutes - self.clock2.minutes if self.clock1.minutes - self.clock2.minutes > 0 else 0
#         seconds = self.clock1.seconds - self.clock2.seconds if self.clock1.seconds - self.clock2.seconds > 0 else 0
#         return f"{self.change_len_number(hours)}: {self.change_len_number(minutes)}: {self.change_len_number(seconds)}"

#     def change_len_number(self, number: int) -> str:
#         if number < 10:
#             return f"0{number}"
#         else:
#             return str(number)

#     def __len__(self) -> int:
#         delta_time = self.clock1.get_time() - self.clock2.get_time()
#         if delta_time < 0:
#             return 0
#         return delta_time


# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt)  # 01: 30: 00
# len_dt = len(dt)  # 5400


# Подвиг 8

# class Ingredient:
#     def __init__(self, name: str, volume: float, measure: str) -> None:
#         self.name = name
#         self.volume = volume
#         self.measure = measure

#     def __str__(self) -> str:
#         return f"{self.name}: {self.volume}, {self.measure}"


# class Recipe:
#     def __init__(self, *ings) -> None:
#         self.ingredients = list(ings)

#     def add_ingredient(self, ing: Ingredient) -> None:
#         self.ingredients.append(ing)

#     def remove_ingredient(self, ing: Ingredient) -> None:
#         self.ingredients.remove(ing)

#     def get_ingredient(self) -> tuple[Ingredient, ...]:
#         return tuple(self.ingredients)

#     def __len__(self) -> int:
#         return len(self.ingredients)


# Подвиг 9

class PolyLine:
    def __init__(self, *coords) -> None:
        self.coords = list(coords)

    def add_coord(self, x: int | float, y: int | float) -> None:
        self.coords.append((x, y))

    def remove_coord(self, indx: int) -> None:
        del self.coords[indx]

    def get_coords(self) -> tuple:
        return tuple(self.coords)
