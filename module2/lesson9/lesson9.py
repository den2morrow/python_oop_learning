# Подвиг 6

class FloatValue:
    @classmethod
    def __check_value(cls, value):
        if type(value) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value: float = 0.0):
        self.value = value


class TableSheet:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.cells = [[Cell() for j in range(self.m)] for i in range(self.n)]


table = TableSheet(n=5, m=3)
cnt = 1.0

for line in table.cells:
    for cell in line:
        cell.value = cnt
        cnt += 1.0


# Подвиг 7

class ValidateString:
    def __init__(self, min_length: int = 3, max_length: int = 100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string) -> bool:
        if type(string) is str:
            if self.min_length <= len(string) <= self.max_length:
                return True
        return False


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, name):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'''<form>
                  Логин: {self.login}
                  Пароль: {self.password}
                  Email: {self.email}
                  </form>''')


# Подвиг 8

class SuperShop:
    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:
    def __init__(self, min_length: int = 2, max_length: int = 50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, name):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) is str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_price=10_000):
        self.max_price = max_price

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, name):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_price:
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name: str, price):
        self.name = name
        self.price = price


# Подвиг 9

class Bag:
    def __init__(self, max_weight: int):
        self.use_weight = 0
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.use_weight + thing.weight <= self.max_weight:
            self.use_weight += thing.weight
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.use_weight -= self.__things[indx]
        del self.__things[indx]

    def get_total_weight(self):
        total = 0
        for thing in self.__things:
            total += thing.weight

        return total


class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


# Подвиг 10

class TVProgram:
    def __init__(self, channel_name: str):
        self.channel_name = channel_name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for tl in self.items:
            if tl.uid == indx:
                self.items.remove(tl)
                break


class Telecast:
    def __init__(self, id: int, name: str, duration: int):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, new_value: int):
        self.__id = new_value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_time: int):
        self.__duration = new_time
