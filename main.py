from decorators import suma_fake, consulta_continente
from factory import Factory


@suma_fake
def suma(num):
    return 2 + num


@suma_fake
def suma2(num):
    return 2 + num


@consulta_continente
def alerta_continente(continente=None):
    return "Continente no soportado :("


print(alerta_continente("europa"))
print("=========================")

print(suma(3))
print(suma2(5))

print("=========================")

object_factory = Factory("Bills").get_instance()
print(object_factory().get_factura())




