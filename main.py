# Створіть метаклас, що перевіряє наявність певних
# атрибутів у всіх класах, які використовують цей
# метаклас.


class MetaClass(type):
    attributes = ["name"]
    def __new__(cls, name, bases, dct):

        for attribute in cls.attributes:
            if attribute not in dct:
                raise AttributeError(f'There is no atribute {attribute} in class {name}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MetaClass):
    name = "John"
    age = 23
    def greet(self):
        print(f"Hello world, its {self.name}. I'm {self.age} years old.")

object = MyClass()
object.greet()
