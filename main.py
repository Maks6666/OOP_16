# Задайте метаклас, що автоматично додає
# додатковий функціонал до всіх класів, що його
# використовують.


class MetalClass(type):
    def __new__(cls, name, bases, dct):

        def greet(self):
            print(f"New method created!")

        dct['greet'] = greet
        print(f'{dct=}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MetalClass):
    def __init__(self, name):
        self.name = name

object = MyClass("Test")
object.greet()
