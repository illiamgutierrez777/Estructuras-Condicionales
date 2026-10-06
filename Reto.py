nombre = input("Ingresa tu nombre:")
edad = int(input("Ingresa tu edad:"))
cal1 = float(input("Ingresa nota1:"))
cal2 = float(input("Ingresa nota2:"))
cal3 = float(input("Ingresa nota3:"))

prom = (cal1+cal2+cal3) / 3

if prom >= 71:
    print("Aprobado")
else:
    print("No aprobado")