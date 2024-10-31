print("Este proyecto tiene por objetivo generar operaciones matemáticas simples")

a = float(input("Dame un número: "))
b = float(input("Dame otro número: "))

print(a)
print(b)

def suma():
    return a + b
    
print("Esta es el resultado de sumar los números que colocaste: ", suma())

def multiplicacion():
    return a * b

print("Este es el resultado de multiplicar los números que colocaste: ", multiplicacion())
