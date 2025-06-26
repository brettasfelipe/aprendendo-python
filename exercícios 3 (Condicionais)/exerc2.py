a, b, c = map(int, input().split())
if a == 0 or b == 0  or c == 0 and a + b < c or b + c < a or b + a < c:
    print("Triângulo inválido")
elif a == b == c:
    print("Equilátero")
elif a == b or b == c or a == c:
    print("Isósceles")
else:
    print("Escaleno")