# Rozszerzony algorytm Euklidesa znajduje NWD d dwóch liczb NATURALNYCH a,b w postaci d = sa + tb,
# gdzie s,t należą do zbioru licz całkowitych.

def Euklides_rozszerzony(a, b):
    r0 = a
    s0 = 1
    t0 = 0
    r1 = b
    s1 = 0
    t1 = 1
    while r1 != 0:
        q = r0 // r1
        r = r0 % r1

        s = s0 - q*s1
        t = t0 - q*t1

        r0, r1 = r1, r
        s0, s1 = s1, s
        t0, t1 = t1, t
    return r0, s0, t0

a = 90
b = 48
r,s,t = Euklides_rozszerzony(a, b)
print("NWD(", a, ",", b, ") =", s, "*", a, "+", t, "*", b, "=", r)