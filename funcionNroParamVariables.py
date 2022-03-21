
// Funciones con numero de parametros variable



def imprimo(*args):// simple
  for valor in args:
    print(f"{valor} es de tipo {type(valor)}")
imprimo(1,2,3,4)

def imprimo_otros_valores(**kwargs): // diccionario
  for clave, valor in kwargs.items():
    print(f"{clave} es {valor}")

imprimo_otros_valores(banda1= 'Nirvana', banda2="Foo Fighters", banda3="AC/DC")

def imprimo_datos(par1, par2, par3): // simples o lista de 3 elementos
  print(par2)
lista = [1, 2, 3]
imprimo_datos(*lista)

def imprimo_agenda(nombre, celu):
  print(nombre, celu)
contacto = {"nombre": "frankkaster", "celu": 12345}
imprimo_agenda(contacto, contacto)// {"nombre": "frankkaster", "celu": 12345} {"nombre": "frankkaster", "celu": 12345}
imprimo_agenda(*contacto) // {"nombre","celu"}
imprimo_agenda(**contacto)// {"frankkaster", 12345}


def imprimo_elementos1(uno, dos, tres, cuatro): // valores
  print( f"{uno}, {dos}")
  
def imprimo_elementos2(*argumentos): //lista simple
  for valor in argumentos:
    print( valor)
    
def imprimo_elementos3(**argumentos): // clave, valor
  for nombre, valor in argumentos.items():
    print( f"{nombre} = {valor}")


tabla_numeros = { "uno": 1, "dos": 2, "tres":3, "cuatro": 4}
print("Invoco a imprimo_elementos3 con tabla_numeros como parámetro")
imprimo_elementos3(**tabla_numeros)


print("-" * 20)
print("Invoco a imprimo_elementos3 con los parámetros nombrados")
imprimo_elementos3(uno =1, dos = 2, tres = 3, cuatro = 4)
print("-" * 20)
print("Invoco a imprimo_elementos1 con parámetros nombrados")
imprimo_elementos1(uno ="I", dos = "II", tres = "III", cuatro = "IV")

print("-" * 20)
print("Invoco a imprimo_elementos1 con parámetros simples")
imprimo_elementos1("I", "II", "III", "IV")

print("-" * 20)
print("Invoco a imprimo_elementos2 con parámetros simples")
imprimo_elementos2(1,2,3,4)
