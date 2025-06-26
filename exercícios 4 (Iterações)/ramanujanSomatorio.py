import math as mt
def fatorial(a):
    if a == 0 or a == 1:
        return 1
    else:
       m = 1
       for n in range(1, a+1):
        m = m * n
        return m

def estimate_pi():
    somatorio = 0
    i = 0
    k = 0
    while True:
        num = (fatorial(4*k)*(1103+26390*k))
        dem = ((fatorial(k))**4)*(396**(4*k))
        i = num/dem
        if i < 10**-15:
            break
        k += 1
        somatorio += i

    sobrePI = ((2*mt.sqrt(2))/9801) * somatorio
    sobrePI = sobrePI**(-1)
    return sobrePI

print(estimate_pi())
print(mt.pi)