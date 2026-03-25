from t_Fermata import *
from f_Eulera import *

from random import randint

def rand_prime(n, m):
    while True:
        potential_prime = randint(n, m)
        if test_Fermata(potential_prime, 1000): return potential_prime

def RSA():
    p = rand_prime(1024, 65535) # 16 bitow
    q = rand_prime(1024, 65535) # 16 bitow
    n = p * q

    E_n = (p-1) * (q-1) # wartosc funkcji eulera dla n
    while True:
        e = randint(2, E_n - 1)
        if are_coprime(e, E_n): break

    d = pow(e, -1, E_n)

    print("Klucz publiczny: (", n, ", ", e, ")" )
    print("Klucz prywatny: (", n, ", ", d, ")" )
    return p, q, n, e, d

print(RSA())