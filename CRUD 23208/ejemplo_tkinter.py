from tkinter import *

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



raiz.mainloop() 