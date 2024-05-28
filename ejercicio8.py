class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            print("El nombre debe ser una cadena de texto.")

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número")

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8:
            self.dni = dni
        else:
            print("El DNI debe tener 8 números.")

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print("Nombre:" + self.nombre)
        print("Edad:" + str(self.edad))
        print("DNI:" + self.dni)
        if self.es_mayor_de_edad():
            print(self.nombre + " es mayor de edad.")
        else:
            print(self.nombre + " no es mayor de edad.")

    def es_mayor_de_edad(self):
        return self.edad >= 18

class Cuenta:     
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print("Titular:", self.titular.get_nombre())
        print("Cantidad:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad ingresada debe ser mayor a 0.")

    def retirar(self, cantidad):
        self.cantidad -= cantidad


persona_titular = Persona("Juliana", 28,"39846546")
cuenta = Cuenta(persona_titular, 100.0)


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular de la cuenta debe tener más de 18 y menos de 25 años para poder retirar dinero.")

    def mostrar(self):
        print("Tipo de cuenta: Cuenta Joven")
        print("Bonificación:", self.bonificacion, "%")

#Puesto en práctica con ejemplos:

cuenta_joven = CuentaJoven(persona_titular, 100.0, 20)

cuenta_joven.mostrar()

cuenta_joven.retirar(100.0)


#con usuario válido

persona_titular.set_edad(22)

cuenta_joven.retirar(100.0)
cuenta_joven.mostrar()


