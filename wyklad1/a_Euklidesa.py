# Klasyczny algorytm Euklidesa znajduje NWD dwóch niezerowych liczb a,b należących do zbioru liczb całkowitych
# bez zera

# złożoność czasowa: O(log(m+n))

def Euklides(a, b):
    while b != 0:
        c = a % b
        a, b = b, c
    return a

a = 12
b = 90
print("NWD(", a, ",", b, ") = ", Euklides(a, b))