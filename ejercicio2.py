def maximo_comun_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def minimo_comun_multiplo(a ,b):
    return abs( a * b) // maximo_comun_divisor(a, b)

numero1 = 25
numero2 = 10
resultado = minimo_comun_multiplo(numero1,numero2)

print("El mínim común múltiplo de", numero1, "y", numero2,"es", resultado)