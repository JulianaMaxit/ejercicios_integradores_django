def get_int():
    valor_correcto = False
    while not valor_correcto:
        try:
            valor = int(input("Ingrese un número entero"))
            valor_correcto = True
        except ValueError:
            print("Debe ingresar un número entero")
    return valor

numero_entero = get_int()
print("El número ingresado es:", numero_entero)


def get_int():
    try:
        valor = int(input("Ingrese un número entero"))
        return valor
    except ValueError:
        print("Ingrese un número entero")
        return get_int()


numero_entero = get_int()
print("El número ingresado es:", numero_entero)
