# # Подвиг 4

# class Car:
#     def __init__(self):
#         self.__model = None

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self, model):
#         if type(model) is str and 2 <= len(model) <= 100:
#             self.__model = model


# # Подвиг 5

# class WindowDlg:
#     def __init__(self, title: str, width: int, height: int):
#         self.__title = title
#         self.__width = width
#         self.__height = height

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, num: int):
#         if type(num) is int and 0 <= num <= 10_000:
#             self.__width = num
#             self.show()

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self, num: int):
#         if type(num) is int and 0 <= num <= 10_000:
#             self.__height = num
#             self.show()

#     def show(self):
#         print(f"{self.__title}: {self.width}, {self.height}")


# Подвиг 6
# from typing import Optional


# class StackObj:
#     def __init__(self, data: str) -> None:
#         self.__data = data
#         self.__next: Optional['StackObj'] = None

#     @property
#     def data(self) -> Optional['StackObj']:
#         return self.__data

#     @data.setter
#     def data(self, data: str) -> None:
#         self.__data = data

#     @property
#     def next(self) -> Optional['StackObj']:
#         return self.__next

#     @next.setter
#     def next(self, next_obj) -> None:
#         if next_obj is None or isinstance(next_obj, StackObj):
#             self.__next = next_obj


# class Stack:
#     def __init__(self, top: Optional['StackObj'] = None) -> None:
#         self.top = top

#     def push(self, obj: 'StackObj') -> None:
#         if self.top is None:
#             self.top = obj
#             self.top.next = None
#         else:
#             head = self.top
#             while head.data is not None:
#                 if head.next is None:
#                     head.next = obj
#                     break
#                 head = head.next

#     def pop(self) -> None:
#         head = self.top
#         while head.next is not None:
#             try:
#                 if head.next.next is None:
#                     result = head.next
#                     head.next = None
#                     return result
#             except Exception:
#                 pass

#             head = head.next

#         result = head
#         self.top = None
#         return result

#     def get_data(self) -> list:
#         result = []
#         head = self.top
#         while head is not None:
#             result.append(head.data)
#             head = head.next
#         return result


# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# st.pop()
# st.pop()
# res = st.get_data()    # ['obj1']


# # Подвиг 7

# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024

#     def __init__(self, x: int = 0, y: int = 0):
#         self.__x = x if self.__check_value(x) else 0
#         self.__y = y if self.__check_value(y) else 0

#     def __check_value(self, num):
#         if type(num) in (int, float):
#             if self.MIN_COORD <= num <= self.MAX_COORD:
#                 return True

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, num: int | float):
#         if self.__check_value(num):
#             self.__x = num

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, num: int | float):
#         if self.__check_value(num):
#             self.__y = num

#     @staticmethod
#     def norm2(vector: 'RadiusVector2D') -> float:
#         return vector.x ** 2 + vector.y ** 2


# Подвиг 8

class TreeObj:
    def __init__(self, indx, value=None, left=None, right=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    ROOT = None

    @classmethod
    def predict(cls, root, x):
        while root.value is None:
            if x[root.indx]:
                root = root.left
            else:
                root = root.right

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if left and node is not None:
            node.left = obj
            return obj
        elif not left and node is not None:
            node.right = obj
            return obj
        else:
            cls.ROOT = obj
            return cls.ROOT


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
v_111 = DecisionTree.add_obj(TreeObj(3), v_11)
v_112 = DecisionTree.add_obj(TreeObj(4), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "1"), v_111)
DecisionTree.add_obj(TreeObj(-1, "2"), v_111, False)
DecisionTree.add_obj(TreeObj(-1, "5"), v_12)
DecisionTree.add_obj(TreeObj(-1, "6"), v_12, False)
DecisionTree.add_obj(TreeObj(-1, "3"), v_112)
DecisionTree.add_obj(TreeObj(-1, "4"), v_112, False)

x = [1, 0, 1, 1, 0]
res = DecisionTree.predict(root, x)
print(res)


# Подвиг 9

class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.__all_path = [LineTo(0, 0)] + [item for item in args]

    def get_path(self):
        return self.__all_path[1:]

    def get_length(self):
        sum_length = 0
        for i in range(len(self.__all_path) - 1):
            last = self.__all_path[i]
            now = self.__all_path[i + 1]

            sum_length += ((now.x - last.x) ** 2 + (now.y - last.y) ** 2) ** 0.5
        return sum_length

    def add_line(self, line):
        self.__all_path.append(line)


# Подвиг 10

class PhoneNumber:
    def __init__(self, number: int, fio: str):
        self.number = number
        self.fio = fio


class PhoneBook:
    def __init__(self):
        self.all_phone_numbers = []

    def add_phone(self, phone):
        self.all_phone_numbers.append(phone)

    def remove_phone(self, indx):
        del self.all_phone_numbers[indx]

    def get_phone_list(self):
        return self.all_phone_numbers


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
