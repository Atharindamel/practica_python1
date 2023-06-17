from tkinter import *

#Framecampos
color_fondo = 'cyan'
color_letra = 'black'

# RAÍZ
raiz = Tk()
raiz.title('GUI - Comisión 23208')

# BARRAMENÚ
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

#Menú de BBDD
bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label = 'Conectar a la base de datos')
bbddmenu.add_command(label = 'Listado de alumnos')
bbddmenu.add_command(label = 'Salir')

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



legajo_input

raiz.mainloop()
