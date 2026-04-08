# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    return list(range(1, n + 1))


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    return [n * i for i in range(1, 11)]


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    suma = 0
    n = abs(n)
    while n > 0:
        suma += n % 10
        n //= 10
    return suma


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    res = [0, 1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res