# Sito Eratostenesa to algorytm wyznaczania wszystkich liczb pierwszych w skończonym zbiorze {2, ..., n} i polega
# na eliminacji liczb złożonych, wykorzystując twierdzenie o rozkładzie na liczby pierwsze

from math import sqrt
def sito_Eratostenesa(a):
    pierwsze = [i+2 for i in range(a-1)]

    k = 2
    i = 2
    while k <= sqrt(a):
        while i < len(pierwsze):
            pierwsze[i] = 0
            i += k

        for j in range(k-1, len(pierwsze)):
            if pierwsze[j] != 0:
                k = pierwsze[j]
                i = j + k
                break

    for pierwsza in pierwsze:
        if pierwsza != 0: print(pierwsza)
    return

print(sito_Eratostenesa(120))