from tkinter import *
import parser

root = Tk()
root.title("Calculadora")
display = Entry (root)
display.grid(row=1, columnspan=6, sticky=W+E)


#obtener numeros en el display
indice = 0

def obtener_numeros_o_simbolos(n):

    global indice
    display.insert(indice, n)
    indice = indice + 1
    
def obtener_operacion(operacion):
    global indice
    longitud_operador = len(operacion)
    display.insert(indice, operador)
    indice = indice + longitud_operador

    #limpiar
def limpiar_pantalla():
    display.delete(0, END)

    #borrar 
def borrar_ultimo():
    display_state = display.get()
    if len(display_state)>1:
        display_new_state = display_state[:-1]
        limpiar_pantalla()
        display.insert(0, display_new_state)
    else:
        limpiar_pantalla()
        display.insert(0,'Error')

#evaluar 
def calcula():
    display_state = display.get()
   # try:
    expresion_matematica = parser.expr(display_state).compile()
    result = eval(expresion_matematica)
    limpiar_pantalla()
    display.insert(0,result)
   # except expresion_matematica as identifier:
 #       clear.display()
  #      display.inser(0, 'Error')
      



#botones numericos

Button(root, text="1", command=lambda:obtener_numeros_o_simbolos(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:obtener_numeros_o_simbolos(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:obtener_numeros_o_simbolos(3)).grid(row=2, column=2, sticky=W+E)
Button(root, text="4", command=lambda:obtener_numeros_o_simbolos(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:obtener_numeros_o_simbolos(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:obtener_numeros_o_simbolos(6)).grid(row=3, column=2, sticky=W+E)
Button(root, text="7", command=lambda:obtener_numeros_o_simbolos(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:obtener_numeros_o_simbolos(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:obtener_numeros_o_simbolos(9)).grid(row=4, column=2, sticky=W+E)

#mas botones

Button(root, text="AC", command=lambda:limpiar_pantalla()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:obtener_numeros_o_simbolos(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda:obtener_numeros_o_simbolos("%")).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", command=lambda:obtener_numeros_o_simbolos("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda:obtener_numeros_o_simbolos("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda:obtener_numeros_o_simbolos("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda:obtener_numeros_o_simbolos("/")).grid(row=5, column=3, sticky=W+E)

Button(root, text="←", command =lambda:borrar_ultimo()).grid(row=6, column=3, sticky=W+E)
Button(root, text="exp", command=lambda:obtener_numeros_o_simbolos("exp")).grid(row=6, column=2, sticky=W+E)
Button(root, text="*2", command=lambda:obtener_numeros_o_simbolos("**2")).grid(row=6, column=1, sticky=W+E)
Button(root, text="(", command=lambda:obtener_numeros_o_simbolos("(")).grid(row=6, column=0, sticky=W+E)
Button(root, text=")", command=lambda:obtener_numeros_o_simbolos(")")).grid(row=7, column=1, sticky=W+E)
Button(root, text="=", command =lambda:calcula()).grid(row=7, column=0, sticky=W+E)




root.mainloop()
