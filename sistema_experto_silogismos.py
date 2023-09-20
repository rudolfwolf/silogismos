import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# parametros de configuracion de la ventana hecha con tkinter
ventana = tk.Tk()
ventana.resizable(width=0, height=0)
ventana.geometry("630x550")
ventana.title(" Sistema Experto Silogismos")
# aqui va la  ruta donde tengas el icono guardado
ventana.iconbitmap('D:/tareas/tareas_python_Arturo/icono.ico')
#aqui va la ruta donde tengas la imagen guardada
imagen = Image.open("D:/tareas/tareas_python_Arturo/1.jpg")
imagen_tk = ImageTk.PhotoImage(imagen)
fondo = Label(ventana, image=imagen_tk)
fondo.place(x=0, y=0, relwidth=1, relheight=1)
ventana.geometry("%dx%d" % (imagen.size[0], imagen.size[1]))

# Etiqueta 1 y campo de entrada 1
etiqueta1 = tk.Label(ventana, text="P. Mayor:")
etiqueta1.grid(row=0, column=0, padx=20, pady=20)
campo_texto1 = tk.Entry(ventana)
campo_texto1.grid(row=0, column=1, padx=50, pady=50)


# Etiqueta 2 y campo de entrada 2
etiqueta2 = tk.Label(ventana, text="P. Menor:")
etiqueta2.grid(row=1, column=0, padx=30, pady=30)
campo_texto2 = tk.Entry(ventana)
campo_texto2.grid(row=1, column=1, padx=50, pady=50)


# Etiqueta 3 y campo de entrada 3
etiqueta3 = tk.Label(ventana, text="Conclusión:")
etiqueta3.grid(row=2, column=0, padx=20, pady=20)
campo_texto3 = tk.Entry(ventana)
campo_texto3.grid(row=2, column=1, padx=50, pady=50)
campo_texto3.config(state='disabled')


# Etiqueta 4 y campo de entrada 4
etiqueta4 = tk.Label(ventana, text="T. Mayor:")
etiqueta4.grid(row=3, column=0, padx=20, pady=20)
campo_texto4 = tk.Entry(ventana)
campo_texto4.grid(row=3, column=1, padx=20, pady=20)
campo_texto4.config(state='disabled')


# Etiqueta 5 y campo de entrada 5 a la derecha de etiqueta1 y campo_texto1
etiqueta5 = tk.Label(ventana, text="letra:")
etiqueta5.grid(row=0, column=2, padx=20, pady=20)
campo_texto5 = tk.Entry(ventana)
campo_texto5.grid(row=0, column=3, padx=20, pady=20)
campo_texto5.config(state='disabled')


# Etiqueta 6 y campo de entrada 6 a la derecha de etiqueta2 y campo_texto2
etiqueta6 = tk.Label(ventana, text="letra:")
etiqueta6.grid(row=1, column=2, padx=20, pady=20)
campo_texto6 = tk.Entry(ventana)
campo_texto6.grid(row=1, column=3, padx=20, pady=20)
campo_texto6.config(state='disabled')



# Etiqueta 7 y campo de entrada 6 a la derecha de etiqueta3 y campo_texto3
etiqueta7 = tk.Label(ventana, text="letra:")
etiqueta7.grid(row=2, column=2, padx=20, pady=20)
campo_texto7 = tk.Entry(ventana)
campo_texto7.grid(row=2, column=3, padx=20, pady=20)
campo_texto7.config(state='disabled')


# Etiqueta 8 y campo de entrada 4
etiqueta8 = tk.Label(ventana, text="T. Menor:")
etiqueta8.grid(row=4, column=0, padx=20, pady=20)
campo_texto8 = tk.Entry(ventana)
campo_texto8.grid(row=4, column=1, padx=20, pady=20)
campo_texto8.config(state='disabled')



# Etiqueta 9 y campo de entrada 9
etiqueta9 = tk.Label(ventana, text="T. 1/2:")
etiqueta9.grid(row=5, column=0, padx=20, pady=20)
campo_texto9 = tk.Entry(ventana)
campo_texto9.grid(row=5, column=1, padx=20, pady=20)
campo_texto9.config(state='disabled')



# Etiqueta 10 y campo de entrada 10 a la derecha de etiqueta3 y campo_texto3
etiqueta10 = tk.Label(ventana, text="Modo:")
etiqueta10.grid(row=3, column=2, padx=20, pady=20)
campo_texto10 = tk.Entry(ventana)
campo_texto10.grid(row=3, column=3, padx=20, pady=20)
campo_texto10.config(state='disabled')



# Etiqueta 11 y campo de entrada 11 a la derecha de etiqueta3 y campo_texto3
etiqueta11 = tk.Label(ventana, text="Figura:")
etiqueta11.grid(row=4, column=2, padx=20, pady=20)
campo_texto11 = tk.Entry(ventana)
campo_texto11.grid(row=4, column=3, padx=20, pady=20)
campo_texto11.config(state='disabled')


def determinar_termino_medio(p_mayor, p_menor):
    
    conectores = ["Tienen", "son", "es", "no son", "Son", "Es", "No Son", "Todos", "Todas", "Toda", "Todo", "Las", "Los", "Ningun", "Ninguna", "Algun", "Algunos", "Algunas", "Alguna"]

    """ esta funcion determina el termino medio separando  las cadenas  recorriendo y validando si se repiten palabras
    excluye las de la lista llamada conectores y concatena las encontradas"""
    
    # Separa las palabras en listas
    p_mayor = p_mayor.split(" ")
    p_menor = p_menor.split(" ")

    # Inicializa una lista para almacenar las palabras repetidas
    palabras_repetidas = []

    # Recorre las dos listas para encontrar palabras repetidas
    for i in range(len(p_mayor)):
        for j in range(len(p_menor)):
            # Compara las palabras sin la "s" al final (si es que la tienen)
            if (p_menor[j] == p_mayor[i] or (p_menor[j].endswith('s') and p_menor[j][:-1] == p_mayor[i]) or (p_mayor[i].endswith('s') and p_mayor[i][:-1] == p_menor[j]) or (p_menor[j].endswith('es') and p_menor[j][:-2] == p_mayor[i]) or (p_mayor[i].endswith('es') and p_mayor[i][:-2] == p_menor[j])):
                # Verifica que la palabra no esté en la lista de conectores
                if p_menor[j] not in conectores:
                    # Comprueba si la palabra en p_mayor tiene una "s" al final y la palabra en p_menor no tiene "s", y viceversa
                    if (p_mayor[i].endswith('s') and not p_menor[j].endswith('s')) or (p_menor[j].endswith('s') and not p_mayor[i].endswith('s')):
                        continue
                    palabras_repetidas.append(p_menor[j] if len(p_menor[j]) > len(p_mayor[i]) else p_mayor[i])

    # Concatena las palabras repetidas en la variable t_menor
    t_medio = ""
    for palabra in palabras_repetidas:
        t_medio += palabra + " "
        
    # Retorna t_medio
    return t_medio


def determinar_terminos(p_mayor, t_medio):
    
    eliminar = ["Todos", "todos", "los", "las", "Algunas", "algunas", "Algunos", "algunos", "alguno", "alguna", "toda","Ningún", "no", "No", "Todo", "todas", "todos", "todo", "ningun", "ninguna", "ningunos", "ningunas", "algun", "alguna", "algunos", "algunas", "son", "es", "era", "el", "los", "las"]
    
    # Separa las palabras de p_mayor en una lista
    palabras_p_mayor = p_mayor.split()

    # Crea una lista para almacenar las palabras limpias
    palabras_limpias = []

    # Recorre cada palabra de palabras_p_mayor
    for palabra in palabras_p_mayor:
        # Descarta las palabras que se encuentran en eliminar o t_medio
        if palabra not in eliminar and palabra not in t_medio.split():
            # Agrega las palabras restantes a la lista de palabras limpias
            palabras_limpias.append(palabra)

    # Concatena las palabras limpias en una cadena
    termino = " ".join(palabras_limpias)

    # Retorna la cadena limpia
    return termino


def determinar_figura_silogismo(p_mayor, p_menor, t_medio, termino_mayor, termino_menor):
    
    # Determinar la figura del silogismo a partir del orden de los términos
    if termino_mayor in p_mayor and t_medio in p_menor:
        figura_silogismo = "Figura 1"
    elif termino_mayor in p_menor and t_medio in p_mayor:
        figura_silogismo = "Figura 2"
    elif termino_menor in p_mayor and t_medio in p_menor:
        figura_silogismo = "Figura 3"
    elif termino_menor in p_menor and t_medio in p_mayor:
        figura_silogismo = "Figura 4"
    else:
        figura_silogismo = "No se puede determinar la figura del silogismo"
    
    # Retornar la figura del silogismo
    return figura_silogismo


def validar_modo(Modo, Figura):
    
    #esta funcion saca la figura correspondiente de cada modo
    
    if Figura == "1":
        
        if Modo == "AAA":
            return "BARBARA"
        
        elif Modo == "EAE":
            return "CELARENT"
        
        elif Modo == "AII":
            return "DARII"
        
        elif Modo == "EIO":
            return "FERIO"
        
    elif Figura == "2":
        
        if Modo == "EAE":
            return "CESARE"
        
        elif Modo == "AEE":
            return "CAMESTRES"
        
        elif Modo == "EIO":
            return "FESTINO"
        
        elif Modo == "AOO":
            return "BAROCO"
        
    elif Figura == "3":
        
        if Modo == "AAA":
            return "DARAPTI"
        
        elif Modo == "AII":
            return "DATISI"
        
        elif Modo == "IAI":
            return "DISAMIS"
        
        elif Modo == "EAE":
            return "FELAPTON"
        
        elif Modo == "EIO":
            return "FERISON"
        
        elif Modo == "OAO":
            return "BOCARDO"
    return "N/A"


def Conclusion(premisa1, letra_premisa1, premisa2, letra_premisa2):
    
    #esta función saca la conclusion de las dos premisas
    
    if letra_premisa1 == 'A' and letra_premisa2 == 'A':
        modo = validar_modo("AAA", "1")
        print(modo)
        conclusion = f"Tod@s {premisa1} son {premisa2}"
        letra_conclusion = 'A'
        
    elif letra_premisa1 == 'E' and letra_premisa2 == 'A':
        modo = validar_modo("EAE", "1")
        print(modo)
        conclusion = f"Ningún {premisa1} es {premisa2}"
        letra_conclusion = 'E'

    elif letra_premisa1 == 'A' and letra_premisa2 == 'I':
        modo = validar_modo("AII", "1")
        print(modo)
        conclusion = f"Algun@s {premisa1} son {premisa2}"
        letra_conclusion = 'I'
        
    elif letra_premisa1 == 'E' and letra_premisa2 == 'I':
        modo = validar_modo("EIO", "1")
        print(modo)
        conclusion = f"Algun@s {premisa1} no son {premisa2}"
        letra_conclusion = 'O'
    
    elif letra_premisa1 == 'E' and letra_premisa2 == 'A':
        modo = validar_modo("EAE", "2")
        print(modo)
        conclusion = f"Ningún {premisa1} es {premisa2}"
        letra_conclusion = 'E'
        
    elif letra_premisa1 == 'A' and letra_premisa2 == 'E':
        modo = validar_modo("AEE", "2")
        print(modo)
        conclusion = f"Ningún {premisa1} es {premisa2}"
        letra_conclusion = 'E'
        
    elif letra_premisa1 == 'E' and letra_premisa2 == 'I':
        modo = validar_modo("EIO", "2")
        print(modo)
        conclusion = f"Algún@s {premisa1} son {premisa2}"
        letra_conclusion = 'O'
        
    elif letra_premisa1 == 'A' and letra_premisa2 == 'O':
        modo = validar_modo("AOO", "2")
        print(modo)
        conclusion = f"Algun@s {premisa1} no son {premisa2}"
        letra_conclusion = 'O'
    
    elif letra_premisa1 == 'A' and letra_premisa2 == 'A':
        modo = validar_modo("AAA", "3")
        print(modo)
        conclusion = f"Algun@s {premisa1} son {premisa2}"
        letra_conclusion = 'O'
        
    elif letra_premisa1 == 'A' and letra_premisa2 == 'I':
        modo = validar_modo("AII", "3")
        print(modo)
        conclusion = f"Algun@s {premisa1} son {premisa2}"
        letra_conclusion = 'I'
        
    elif letra_premisa1 == 'I' and letra_premisa2 == 'A':
        modo = validar_modo("IAI", "3")
        print(modo)
        conclusion = f"Algun@s {premisa1} son {premisa2}"
        letra_conclusion = 'I'
        
    elif letra_premisa1 == 'E' and letra_premisa2 == 'A':
        modo = validar_modo("EAE", "3")
        print(modo)
        conclusion = f"Algun@s {premisa1} son {premisa2}"
        letra_conclusion = 'O'
        
    elif letra_premisa1 == 'E' and letra_premisa2 == 'I':
        modo = validar_modo("EIO", "3")
        print(modo)
        conclusion = f"Algun@s {premisa1} no son {premisa2}"
        letra_conclusion = 'O'
        
    elif letra_premisa1 == 'O' and letra_premisa2 == 'A':
        modo = validar_modo("OAO", "3")
        print(modo)
        conclusion = f"Algun@s {premisa1} no son {premisa2}"
        letra_conclusion = 'O'
        
    else :
        modo = 'N/A'
        print(modo)
        conclusion = f" "
        letra_conclusion = 'N/A'
        
    
    return conclusion, modo, letra_conclusion


def determinar_letra(premisa):
    
    '''
    esta función determina la letra del silogismo
    '''
    universal_positivo = ["todos", "todo", "toda", "todas", "Todos", "Todo", "Toda", "Todas"]
    universal_negativo = ["Ningún", "ningun", "ningun", "ningún", "ninguna", "ninguna", "ningunas", "ningunas", "ninguno", "ninguno", "ningunos", "ningunos"]
    negativo = [" no es", "no son"]
    particular = ["alguno", "algunos", "algunas", "alguna","Alguno", "Algunos", "Algunas", "Alguna", "Algún", "algun", "algún", "Algun" ]
    positivo = [ "es", "son"]

    if any(word in premisa for word in universal_positivo) and any(word in premisa for word in positivo):
        return 'A'
    elif any(word in premisa for word in universal_negativo) and any(word in premisa for word in positivo):
        return 'E'
    elif any(word in premisa for word in particular) and any(word in premisa for word in negativo):
        return 'O'
    elif any(word in premisa for word in particular) and any(word in premisa for word in positivo):
        return 'I'
    
'''  
premisas de prueba  
p_mayor = 'Todos los parásitos son insectos'
p_menor = 'Algunos parásitos son animales      '

t_medio = determinar_termino_medio(p_mayor, p_menor)
termino_mayor = determinar_terminos(p_mayor, t_medio)
termino_menor = determinar_terminos(p_menor, t_medio)
figura_silogismo = determinar_figura_silogismo(p_mayor, p_menor, t_medio, termino_mayor, termino_menor)
letra_pmayor = (determinar_letra(p_mayor)) 
letra_pmenor = (determinar_letra(p_menor)) 
conclusion, modo, letra_conclusion = Conclusion(termino_menor, letra_pmayor, termino_mayor, letra_pmenor)


impresion variables desde consola
print ('premisa mayor: ',p_mayor)
print('termino mayor: ',termino_mayor)
print('letra:',letra_pmayor)
print('\n')
print ('premisa menor: ',p_menor)
print('termino menor: ',termino_menor)
print('letra:',letra_pmenor)
print('\n')
print('término medio: ',t_medio)
print('\n')
print('conclusion: ',conclusion)
print('letra: ',letra_conclusion)
print('modo: ',modo)
print('figura: ',figura_silogismo)
'''

def limpiar():
    #esta funciona habilita los campos limpia los campos y los inhabilita
    campo_texto1.config(state='normal')
    campo_texto2.config(state='normal')
    campo_texto3.config(state='normal')
    campo_texto4.config(state='normal')
    campo_texto5.config(state='normal')
    campo_texto6.config(state='normal')
    campo_texto7.config(state='normal')
    campo_texto8.config(state='normal')
    campo_texto9.config(state='normal')
    campo_texto10.config(state='normal')
    campo_texto11.config(state='normal')
    
    campo_texto1.delete(0, tk.END)
    campo_texto2.delete(0, tk.END)
    campo_texto3.delete(0, tk.END)
    campo_texto4.delete(0, tk.END)
    campo_texto5.delete(0, tk.END)
    campo_texto6.delete(0, tk.END)
    campo_texto7.delete(0, tk.END)
    campo_texto8.delete(0, tk.END)
    campo_texto9.delete(0, tk.END)
    campo_texto10.delete(0, tk.END)
    campo_texto11.delete(0, tk.END)
    
    campo_texto3.config(state='disabled')
    campo_texto4.config(state='disabled')
    campo_texto5.config(state='disabled')
    campo_texto6.config(state='disabled')
    campo_texto7.config(state='disabled')
    campo_texto8.config(state='disabled')
    campo_texto9.config(state='disabled')
    campo_texto10.config(state='disabled')
    campo_texto11.config(state='disabled') 
    #habilitamos el boton iniciar para que pueda validar el silogismo
    btnIniciar.config(state='normal')  


def validar():
    # función que ejecuta el boton de validar  para capturar datos y habilitar y deshabilitar los campos
    
    p_mayor = " "
    p_menor = ""  
    p_mayor = campo_texto1.get()
    p_menor = campo_texto2.get()
    t_medio = determinar_termino_medio(p_mayor, p_menor)
    termino_mayor = determinar_terminos(p_mayor, t_medio)
    termino_menor = determinar_terminos(p_menor, t_medio)
    figura_silogismo = determinar_figura_silogismo(p_mayor, p_menor, t_medio, termino_mayor, termino_menor)
    letra_pmayor = (determinar_letra(p_mayor)) 
    letra_pmenor = (determinar_letra(p_menor)) 
    conclusion, modo, letra_conclusion = Conclusion(termino_menor, letra_pmayor, termino_mayor, letra_pmenor)
    
    
    campo_texto1.config(state='normal')
    campo_texto2.config(state='normal')
    campo_texto3.config(state='normal')
    campo_texto4.config(state='normal')
    campo_texto5.config(state='normal')
    campo_texto6.config(state='normal')
    campo_texto7.config(state='normal')
    campo_texto8.config(state='normal')
    campo_texto9.config(state='normal')
    campo_texto10.config(state='normal')
    campo_texto11.config(state='normal')
    
    campo_texto3.insert(0, conclusion)
    campo_texto4.insert(0, termino_mayor)
    campo_texto5.insert(0, letra_pmayor)
    campo_texto6.insert(0, letra_pmenor)
    campo_texto7.insert(0, letra_conclusion)
    campo_texto8.insert(0, termino_menor)
    campo_texto9.insert(0, t_medio)
    campo_texto10.insert(0, modo)
    campo_texto11.insert(0, figura_silogismo)
    
    
    campo_texto3.config(state='disabled')
    campo_texto4.config(state='disabled')
    campo_texto5.config(state='disabled')
    campo_texto6.config(state='disabled')
    campo_texto7.config(state='disabled')
    campo_texto8.config(state='disabled')
    campo_texto9.config(state='disabled')
    campo_texto10.config(state='disabled')
    campo_texto11.config(state='disabled')
    btnIniciar.config(state='disabled')

#boton limpiar campos del formulario
btnLimpiar = tk.Button(ventana, text= 'Limpiar', command=limpiar)
btnLimpiar.grid(row=5, column=2, padx=20, pady=20)

#boton que llama a la función que realiza la validación del silogismo
btnIniciar = tk.Button(ventana, text= 'Validar', command=validar)
btnIniciar.grid(row=5, column=3, padx=20, pady=20)         

ventana.mainloop() 



