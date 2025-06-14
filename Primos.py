def es_primo(numero):
    """
    Verifica si un número es primo.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primeros_n_primos(n):
    """
    Encuentra los primeros 'n' números primos.
    """
    primos = []
    num_actual = 0
    while len(primos) < n:
        if es_primo(num_actual):
            primos.append(num_actual)
        num_actual += 1
    return primos

# Mostrar los primeros 20 números primos
cantidad_primos = 20
primeros_20_primos = encontrar_primeros_n_primos(cantidad_primos)
print(f"Los primeros {cantidad_primos} números primos son:")
print(primeros_20_primos)