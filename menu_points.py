suma = 0
print("\tQuiz")
print("De los animales abajo:")
print("1) Perro")
print("2) Crocodilo")
print("3) Conejo")
print("4) Tiburon")
res = input("Cuales destos son maritimos? ")
if res == '2':
    suma = suma + 0.5
    print("Sumaste medio punto")
if res == '4':
    suma = suma + 1
    print("Sumaste uno punto")
if res == '2 4' or res == '2, 4':
    suma = suma + 1.5
    print("Sumaste un punto y medio")
elif res == '1':
    print("No sumaste ningun punto")
elif res == '3':
    print("No sumaste ningun punto")