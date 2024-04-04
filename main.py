# Реалізуйте метаклас, що забороняє спадкування від
# певних класів чи змінює порядок спадкування.


class MetaClass(type):
    forbidden_classes = ["Forbidden"]

    def __new__(cls, name, bases, dct):
        for base in bases:
            if base.__name__ in cls.forbidden_classes:
                raise TypeError(f"Inheritance from {base.__name__} is forbidden.")
        return super().__new__(cls, name, bases, dct)


# class Allowed(metaclass=ForbiddenInheritanceMeta):
    ...

class Forbidden(metaclass=MetaClass):
    ...

class NewClass(Forbidden):
    ...

# class NewClass(Allowed):
#     ...








