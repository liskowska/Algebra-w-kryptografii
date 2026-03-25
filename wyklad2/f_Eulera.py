# Dla niezerowej liczby naturalnej n definiujemy funkjcę Eulera jako liczbę liczb całkowitych dodatnich nie większych
# od n, które są względnie pierwsze z n.

# E(1) = 1
# E(n) <= n-1, dla n > 1

from math import sqrt

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True

def prime_factorization(a):
    primes = []
    for i in range(a):
        if isPrime(i):
            while True:
                if a % i == 0:
                    primes.append(i)
                    a = a / i
                else: break
    return primes

def f_Eulera(a):
    primes_a = prime_factorization(a)
    prev_prime = -1
    E = a
    for p in primes_a:
        if prev_prime == p: continue
        E *= (1 - 1/p)
        prev_prime = p
    return int(E)

# print(prime_factorization(2646))
# print(f_Eulera(2646))