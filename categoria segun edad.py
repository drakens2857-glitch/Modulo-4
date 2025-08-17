edad = int(input("Introduce la edad del estudiante: "))
if edad < 12:
    print("Niño")
elif 12 <= edad <= 17:
    print("Adolescente")
else:
    print("Adulto")
    