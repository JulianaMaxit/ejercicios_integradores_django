def maximo_comun_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

numero1 = 20
numero2 = 4

resultado = maximo_comun_divisor(numero1, numero2)

print("El máximo común divisor de", numero1, "y", numero2, "es", resultado)