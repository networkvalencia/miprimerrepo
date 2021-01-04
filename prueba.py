# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#strings

mistring = "hello world"

print ("esto es " + mistring)
print (f"mi nombre es {mistring}")
print ("mi nombre es {0}" .format(mistring))

#numeros

print (type (9.99))


#edad = input ("introduce tu edad: ")

edad =4
print (edad)
nueva_edad = int(edad) + 5
print (nueva_edad)


#listas


demo_list = [1, 'lista', 4 , 'pepe']
lista_automatica_con_funcion_list = list ((1 ,'dos', 3, 'cuatro'))
print (lista_automatica_con_funcion_list)
lista_a_partir_de_rango = list(range(1,10))
print (type(lista_a_partir_de_rango))
# muestra los metodos de una funcion
print (dir(lista_a_partir_de_rango))
#muestra la longitud
print (len(lista_automatica_con_funcion_list))
print (lista_a_partir_de_rango[1])
#booleano a ver si la busqueda es correcta en una lista
print (4 in lista_a_partir_de_rango)
#utilizar metodo append para insertar un elemento en una lista
lista_a_partir_de_rango.append('otroelemento')
print (lista_a_partir_de_rango)
#utilizar metodo extend para insertar 1 elemento que son varios elemento a partir de otra lista
lista_a_partir_de_rango.extend((lista_automatica_con_funcion_list))
print (lista_a_partir_de_rango)
#insertar en un a lista en una posicion determinada
lista_a_partir_de_rango.insert(1, 'insertado')
print (lista_a_partir_de_rango)
#eliminar el ultimo, o cualquier indice indicandolo dentro del parentesis
lista_a_partir_de_rango.pop()
print (lista_a_partir_de_rango)
lista_a_partir_de_rango.remove('otroelemento')
print (lista_a_partir_de_rango)
#limpia toda una lista
lista_a_partir_de_rango.clear()

#tuplas
tupla = (1,2,3,4,5,6)
print (tupla)
#borra TODA la tupla ya que es inmutable elemento por elemento
del tupla


#SETS {} no se pueden recorer con un indice

colors = {'red', 'green'
    , 'blue'}
colors.add ('violea')
colors.remove('red')

#diccionarios sirven para definir objetos de la vida real

producto = { "nombre_producto" : "nombre del producto",
             "cantidad_del_producto" : 4 ,
             "observaciones_del_producto" : "observaciones"}

print(type(producto))
print(dir(producto))
print (producto.keys())
print (producto.items())

#control de flujo

x =input ("intriduce un valor numerico :")
valor = int(x)
if valor > 30 :
    print ("el valor que has introducido es > 30")
elif valor == 30:
    print ("el color es 30")
else:
    print ("el valor es < que 30")

# bucles o iteradores

for contador in lista_automatica_con_funcion_list: #esta definiendo contador
    if contador == "dos" :
        break
    print (contador)


for letras in "esto es una cadena":
    print (letras)


contador = 0
while contador < 10 :
    print (contador)
    contador = contador + 1

#FUNCIONES
#
        
def funcion (parametro1, parametro2):
    return (parametro1 + parametro2)

print (funcion (3, 10))

#modulos
#pip install "nombre del modulo

#tkinter para desarrolar aplicaciones de escritorio
