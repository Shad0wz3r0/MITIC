# 1. Imprime "Hola, mundo"
print( "Hola, mundo" );
# 2. Imprime "Hola, Carlos" con el nombre en una variable
nombre = "Carlos";
print( "Hola," ,nombre) # con una coma
print( "Hola, " + nombre) # con un +
# 3. Imprimir "Hola 156!" con el número en una variable
numero = 117
print( "Hola" ,numero, "!" ) # con una coma
print( "Hola " + str(numero) + " !" ) # con un + -- este debería arrojar un error!, corrígelo con conversión
# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "pizza"
comida2 = "Vori Vori"
print( "Me encanta comer {} y {} !".format(comida1, comida2)) # con .format()
print( f"Me encanta comer {comida1} y {comida2} !" ) # con una cadena f
print( "Me encanta comer %s y %s !" % (comida1, comida2)) # con %
