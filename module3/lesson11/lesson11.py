# Подвиг 2

# import random


# class RandomPassword:
#     def __init__(self, psw_chars, min_length: int, max_length: int):
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length

#     def __call__(self, *args, **kwargs):
#         password_length = random.randint(self.min_length, self.max_length)
#         return ''.join(random.sample(self.psw_chars, password_length))


# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
# rnd = RandomPassword(psw_chars, min_length, max_length)

# lst_pass = [rnd() for _ in range(3)]


# Подвиг 3

# class ImageFileAcceptor:
#     def __init__(self, extensions: tuple):
#         self.extensions = extensions

#     def __call__(self, *args, **kwargs):
#         print(args)
#         return args[0].split('.')[-1] in self.extensions


# Подвиг 4

# from string import ascii_lowercase, digits


# class LoginForm:
#     def __init__(self, name, validators=None):
#         self.name = name
#         self.validators = validators
#         self.login = ""
#         self.password = ""

#     def post(self, request):
#         self.login = request.get('login', "")
#         self.password = request.get('password', "")

#     def is_validate(self):
#         if not self.validators:
#             return True

#         for v in self.validators:
#             if not v(self.login) or not v(self.password):
#                 return False

#         return True


# class LengthValidator:
#     def __init__(self, min_length: int, max_length: int):
#         self.min_length = min_length
#         self.max_length = max_length

#     def __call__(self, *args, **kwargs):
#         return self.min_length <= len(args[0])  <= self.max_length


# class CharsValidator:
#     def __init__(self, chars: str):
#         self.chars = chars

#     def __call__(self, *args, **kwargs):
#         for arg in args[0]:
#             if arg not in self.chars:
#                 return False
#         return True


# Подвиг 5

# class DigitRetrieve:
#     def __call__(self, *args, **kwargs):
#         try:
#             condition = args[0].isdigit() or int(args[0]) == float(args[0])
#         except Exception:
#             return None
#         if condition:
#             return int(args[0])
#         else:
#             return None


# Подвиг 6

class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        if self.type_list != 'ol':
            self.type_list = 'ul'

        html_string = f"""<{self.type_list}>\n"""

        for arg in args[0]:
            html_string += f"<li>{arg}</li>\n"

        return html_string + f"</{self.type_list}>"


# Подвиг 7

class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        method = request.get('method', 'GET')
        if method == 'GET':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"


# Подвиг 8

class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method in self.methods:
                return self.__getattribute__(method.lower())(func, request)
            return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


# Подвиг 9

class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        def wrapper():
            return list(map(int, self.func().split()))
        return wrapper()


input_dg = InputDigits(input)
res = input_dg()


# Подвиг 10

class RenderDigit:
    def __call__(self, value, *args, **kwargs):
        try:
            return int(value)
        except Exception:
            return None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))
        return wrapper


input_dg = InputValues(RenderDigit())(input)
res = input_dg()
print(res)
