# Test pierwszości Fermata pozwala z pewnym prawdopodobieństwem zależnym od k określić czy liczba p,
# niebędąca liczbą Carmichaela, jest liczbą pierwszą

import random

def are_coprime(a, b):
    def euklides(a, b):
        while b != 0:
            c = a % b
            a, b = b, c
        return a

    if euklides(a, b) == 1: return True
    else: return False

def test_Fermata(p, k):
    if p < 2: return False
    if p == 2: return True

    for _ in range(k):
        a = random.randint(2, p-2)
        if not are_coprime(a, p): return False

        # potęgowanie modularne: r^(p-1) % p
        if pow(a, p-1, p) != 1: return False

    return True

# False - liczba zlozona
# True - liczba pierwsza
print(test_Fermata(37, 30))
print(test_Fermata(22, 22))
print(test_Fermata(19, 19))