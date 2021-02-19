class Singleton:
    instance = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = object.__new__(cls)
        return Singleton.instance

    def __str__(self):
        return "Hola"


object_singleton1 = Singleton()
object_singleton2 = Singleton()
object_singleton3 = Singleton()
print(id(object_singleton1))
print(id(object_singleton2))
print(id(object_singleton3))


class SinSingleton:
    def __init__(self):
        pass


object_singleton_a = SinSingleton()
object_singleton_b = SinSingleton()
object_singleton_c = SinSingleton()
print("========================================")
print(id(object_singleton_a))
print(id(object_singleton_b))
print(id(object_singleton_c))
