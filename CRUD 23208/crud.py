from tkinter import *
from tkinter import messagebox
import sqlite3 as sq3
import matplotlib.pyplot as plt

# Entorno virtual
''' primera vez deben instalar con
    pip install virtualenv

CREAR ENTORNO VIRTUAL
virtualenv {nombre}
ej: virtualenv venv

ACTIVAR el entorno virtual
{Nombre del entorno virtual}\Scirpt\activate

INSTALAR LIBRERÍAS
pip install {nombreLibrería} (En este caso es "matplotlib")

VER QUE HAY INSTALADO EN EL ENTORNO VIRTUAL

DESCTIVAR el entorno virtual
deactivate

GRABAR en un archivo los requerimientos del entorno
PIP freeze > requirements.txt

Al distribuir el proyecto, solo llevo los archivos py, gráficos, etc y requirements.txt. en la máquina de
destino, creo un entorno virtual e instalo los requerimientos pip install -r requeriments.txt

DOCUMENTACIÓN: https://virtualenv.pypa.io/en/stable/index.html

'''

'''
******************************
Parte funcional
******************************
'''
# *****MENÚ*****
# BBDD-Conectar
def conectar():
    global con
    global cur
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    messagebox.showinfo("STATUS","¡Conectado a la BBDD!")

# BBDD - Salir
def salir():
    resp = messagebox.askquestion("CONFIRME", "¿Desea salir de la aplicación?")
    if resp == 'yes':
        con.close()
        raiz.destroy()
    

'''
******************************
Interfaz gráfica
******************************
'''
#Framecampos
color_fondo = 'cyan'
color_letra = 'black'

#Framebotones
fondo_framebotones = 'plum'
color_fondo_boton = 'black'
color_texto_boton = fondo_framebotones

# RAÍZ
raiz = Tk()
raiz.title('GUI - Comisión 23208')

# BARRAMENÚ
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

#Menú de BBDD
bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label = 'Conectar a la base de datos', command=conectar)
bbddmenu.add_command(label = 'Listado de alumnos')
bbddmenu.add_command(label = 'Salir', command=salir)

# Menú estadísticas
estadmenu = Menu(barramenu, tearoff=0)
estadmenu.add_command(label = 'Alumnos por escuelas')
estadmenu.add_command(label = 'Calificaciones')
estadmenu.add_command(label = 'Calificaciones')

# Menú limpiar
limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label= 'Limpiar')

# Menú acerca de..
ayudamenu = Menu(barramenu,tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de...')

barramenu.add_cascade(label ='BBDD', menu=bbddmenu)
barramenu.add_cascade(label = 'Gráficas', menu=estadmenu)
barramenu.add_cascade(label = 'Limpiar', menu=limpiarmenu)
barramenu.add_cascade(label = 'Acerca de...', menu=ayudamenu)

# ----- FRAME CAMPOS -----
framecampos = Frame(raiz)
framecampos.config(bg=color_fondo)
framecampos.pack(fill='both')

#Labels
def config_label(mi_label, fila):
    espaciado_labels = {'column':0, 'sticky':'e', 'padx':10, 'pady':10}
    color_labels = {'bg':color_fondo, 'fg':color_letra}
    mi_label.grid(row=fila, **espaciado_labels)
    mi_label.config(**color_labels)

legajo_label = Label(framecampos, text='N° de legajo')
config_label(legajo_label,0)

apellido_label = Label(framecampos, text='Apellido')
config_label(apellido_label,1)

nombre_label = Label(framecampos, text='Nombre')
config_label(nombre_label,2)

email_label = Label(framecampos, text='E-mail')
config_label(email_label,3)

promedio_label = Label(framecampos, text='Promedio')
config_label(promedio_label,4)

escuela_label = Label(framecampos, text='Escuela')
config_label(escuela_label,5)

localidad_label = Label(framecampos, text='Localidad')
config_label(localidad_label,6)

provincia_label = Label(framecampos, text='Provincia')
config_label(provincia_label,7)

# ENTRY
# Crear variables de control de los campos de entrada
legajo = StringVar()
apellido = StringVar()
nombre = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

def config_input(mi_input, fila):
    espaciado_inputs = {'column':1, 'padx':10, 'pady':10, 'ipadx':50}
    mi_input.grid(row=fila, **espaciado_inputs)

legajo_input = Entry(framecampos, textvariable=legajo)
config_input(legajo_input, 0)

apellido_input = Entry(framecampos, textvariable=apellido)
config_input(apellido_input, 1)

nombre_input = Entry(framecampos, textvariable=nombre)
config_input(nombre_input, 2)

email_input = Entry(framecampos, textvariable=email)
config_input(email_input, 3)

calificacion_input = Entry(framecampos, textvariable=calificacion)
config_input(calificacion_input, 4)

#NO OLVIDARSE DE SACAR PARA PONER CAMPOS DESPLEGABLES
escuela_input = Entry(framecampos, textvariable=escuela)
config_input(escuela_input, 5)

localidad_input = Entry(framecampos, textvariable=localidad)
config_input(localidad_input, 6)

provincia_input = Entry(framecampos, textvariable=provincia)
config_input(provincia_input, 7)

#------FRAMEBOTONES ----------
#FUNCIONES CRUD (CREATE, READ, UPDATE, DELETE)
framebotones = Frame(raiz)
framebotones.config(bg=fondo_framebotones)
framebotones.pack(fill='both')

def config_buttons(mi_button, columna):
    espaciado_buttons = {'row':0, 'padx':5, 'pady':10, 'ipadx':12}
    mi_button.config(bg=color_fondo_boton, fg=color_texto_boton)
    mi_button.grid(column=columna, **espaciado_buttons)

boton_crear = Button(framebotones, text='Crear')
config_buttons(boton_crear, 0)

boton_buscar = Button(framebotones, text='Buscar')
config_buttons(boton_buscar, 1)

boton_actualizar = Button(framebotones, text='Actualizar')
config_buttons(boton_actualizar, 2)

boton_eliminar = Button(framebotones, text='Eliminar')
config_buttons(boton_eliminar, 3)

#------ FRAMECOPY ------

framecopy = Frame(raiz)
framecopy.config(bg='black')
framecopy.pack(fill='both')

copylabel = Label(framecopy, text='(2023) por Leonel Juiz para CaC 4.0 - Big Data (Idea original de Prof. Regina N. Molares)')
copylabel.config(bg='darkred', fg='white')
copylabel.grid(row=0, column=0, padx=10, pady=10)




raiz.mainloop()
