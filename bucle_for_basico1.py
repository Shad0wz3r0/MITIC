
#1-Básico: imprime todos los números enteros del 0 al 100.

print(" 1- Básico, presione una tecla para continuar");
input()

for num in range(0,101):
    print (num);

#2-Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500

print("\n 2 - Múltiples de 2, presione una tecla para continuar");
input()

for num in range(2,501,2):
    print (num);

#3-Contando Vanilla Ice: imprime los números enteros del 1 al 100.
#  Si es divisible por 5 imprime “ice ice” en vez del número.
#  Si es divisible por 10, imprime “baby”

print("\n 3 - Contando Vanilla Ice, presione una tecla para continuar");
input()

for num in range(1,101):
    if divmod (num,10)[1]==0:
     print ("baby");
    elif divmod (num,5)[1]==0:
      print ("ice ice");
    else:
     print (num);

#4-Wow. Número gigante a la vista:
#  suma los números pares del 0 al 500,000 
# e imprime la suma total. (Sorpresa, será un número gigante).

print("\n 4 - Wow. Número gigante a la vista, presione una tecla para continuar");
input()

suma = sum(range(0,500001))
print (suma)

#Regrésame al 3: imprime los números positivos comenzando desde 2024,
#  en cuenta regresiva de 3 en 3.

print("\n 5 - Regrésame al 3:, presione una tecla para continuar");
input()

for num in range(2024,0,-3):
    print(num);

#Contador dinámico: establece tres variables: numInicial, numFinal y multiplo.
#Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo.
#Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

print("\n 6 - Contador Dinamico, presione una tecla para continuar");
input()

numInicial = 6;
numFinal = 50;
multiplo = 5;

for i in range(numInicial,numFinal):
    if divmod (i,multiplo)[1]==0:
      print (i);
