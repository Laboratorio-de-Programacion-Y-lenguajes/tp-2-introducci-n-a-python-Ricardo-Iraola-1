# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cero" según corresponda.
    """
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Retorna el mayor de tres números.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota:
    - nota >= 9: "Sobresaliente"
    - nota >= 7: "Bueno"
    - nota >= 6: "Aprobado"
    - nota < 6:  "Desaprobado"
    """
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    """
    Retorna True si el año es bisiesto.
    Un año es bisiesto si es divisible por 4,
    excepto los divisibles por 100, salvo que también lo sean por 400.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False