//Necesitamos procesar las notas de los estudiantes de este curso
//Queremos saber
  // cuál es el promedio de las notas
  // qué estudiantes están por debajo del promedio
  
  
 // len(); 
// keys();
// values();
// items();
// del(): permite borrar un par clave:valor
 //clear(): permite borrar todo
nombre= input("Ingrese nombre <o FIN>: ")
dicc= {}
while nombre!= "FIN":
  nota= int(input(f"Ingrese nota del estudiante {nombre}: "))
  dicc[nombre]= nota
  nombre= input("Ingrese nombre <o FIN>: ")
  
dicci = dict([("enero", 31), ("febrero", 28), ("marzo", 31)]) //usando dict Se denomia “constructor” 
                                                            //y crea un diccionario directamente desde listas de pares clave-valor
print(dicci)                                                            //  guardados como tuplas
    
//En esta sección, usaremos la compresión de diccionario para crear un diccionario en Python a partir de un elemento iterable, es decir, una lista o tupla.

dicComp= dict ([(x, x**2) for x in (2, 4, 6)])
caracteres = dict([(n, ord(n)) for n in ("a","b","c")])
print(dicComp)
print(caracteres)

cant= len(dicc)
total= 0
for d in dicc:  // POR CADA NOMBRE DEL DICCIONARIO- ACCEDO POR LA CLAVE
  total= total + dicc[d]  // SUMO SU NOTA AL TOTAL

promedio= total/cant
for d in dicc:
  if dicc[d] < promedio: // SI NOTA < PROMEDIO
    print(f"Alumno {d} tiene un nota {dicc[d]} menor al promedio {promedio}")

claves= dicc.keys()
valores= dicc.values()
items= dicc.items()
for k in claves:
  print(f"Claves {k}") // ana, oscar
for k in valores:
  print(f"Valores {k}") // 5,6
for k in items:
  print(f"Claves {k}") // (ana,5), (oscar,6)
