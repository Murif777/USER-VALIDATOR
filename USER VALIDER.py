from tkinter import filedialog
from tkinter import messagebox, ttk
from tkinter import *
#from functools import partial
import re   
import tkinter as tk
from tkinter.messagebox import showinfo
from tkcalendar import Calendar
from datetime import datetime
from tkinter.ttk import Treeview
import datetime
import os
selected_line = ""
sw=0
carga_arch=False
print("By Farid Muriel, 2023-1")
def abrir():
    global sw
    global carga_arch
    sw = 0
    global filename
    filename = filedialog.askopenfilename(
        title=("Abrir archivo de usuarios"),
        filetypes=(("Archivos de texto", "*.txt"),)
    )
    if filename:
        messagebox.showinfo(message="Archivo cargado, \nRuta: " + filename, title="Abrir Archivo")
        sw = 1
        carga_arch=True
    else:
        messagebox.showinfo(message="Archivo no cargado", title="Abrir Archivo")
        sw = 0

def ventana_salida():
    ventana_temporal = Toplevel(root)
    ventana_temporal.geometry("500x400")
    ventana_temporal.title("Salida")
    tex=tk.Label(ventana_temporal,text="Has salido con exito", bg="brown2")
    tex.pack(fill=X)
    tex.configure(font=("Berlin Sans FB", 16, "italic"))
    autor=tk.Label(ventana_temporal,text="By_Farid_Muriel_2023",bg="brown2")
    autor.pack(fill=X,side=tk.BOTTOM)
    autor.configure(font=("Berlin Sans FB", 16, "italic"))
    ventana_temporal.after(1500, ventana_temporal.destroy)
    global imagen
    imagen = PhotoImage(file="")
    label_imagen = Label(ventana_temporal, image=imagen)
    label_imagen.pack()

def ventana_proc():
    ventana_temporal = Toplevel(root)
    ventana_temporal.geometry("400x150")
    ventana_temporal.title("Cargando")
    autor=tk.Label(ventana_temporal,text="Procesando Archivo...",fg="brown2")
    autor.pack(expand=True, anchor=tk.CENTER)
    autor.configure(font=("Berlin Sans FB", 16, "italic"))
    ventana_temporal.after(500,ventana_temporal.destroy)

def fun_unidas():
    result=messagebox.askquestion("Pregunta","¿Desea salir?")
    if result=="yes":
        root.after(1500, root.quit)
        ventana_salida()

def fun_unidas2():
    global sw
    global carga_arch
    if carga_arch:
        ventana_proc()
        root.after(1500, archivos)
        sw=1
        carga_arch=True
    else:
        messagebox.showinfo(message="Es necesario cargar un archivo", title="Error")

def fun_unidas3():
    global sw
    global carga_arch
    if carga_arch:
        ventana_proc()
        root.after(1500, mostrar)
        sw=1
        carga_arch=True
    else:
        messagebox.showinfo(message="Es necesario cargar un archivo", title="Error")

def fun_unidas4():
    global sw
    global carga_arch
    if carga_arch:
        ventana_proc()
        root.after(1500, Ventana3)
        sw=1
        carga_arch=True
    else:
        messagebox.showinfo(message="Es necesario cargar un archivo", title="Error")

def fun_unidas5():
    global sw
    global carga_arch
    if carga_arch:
        ventana_proc()
        root.after(1500, Ventana4)
        sw=1
        carga_arch=True
    else:
        messagebox.showinfo(message="Es necesario cargar un archivo", title="Error")

def fun_unidas6():
    global sw
    global carga_arch
    if carga_arch:
        ventana_proc()
        root.after(1500, Ventana2)
        sw=1
        carga_arch=True
    else:
        messagebox.showinfo(message="Es necesario cargar un archivo", title="Error")

def eliminar_fechas_incorrectas(fecha):
    try:
        datetime.datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def calcular_edad(fecha_nacimiento):
    try:
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
        hoy = datetime.date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad
    except ValueError:
        return None

def mostrar_tabla_errores(tabla, registros_erroneos):
    tabla.delete(*tabla.get_children())  # Limpiar la tabla antes de agregar registros
    for error in registros_erroneos:
        nl,tipo,documento,apellido,sec_apellido,nombre1,nombre2,fecha_nacimiento,genero,Sisben,Error= error
        tabla.insert("", "end", text=str(nl), values=(tipo,documento,apellido,sec_apellido,nombre1,nombre2,fecha_nacimiento,genero,Sisben,Error))

def mostrar():
    global sw
    archivo = filename
    with open(archivo, "r") as archivo_lectura:
        nl = 0
        sw = 0
        tabla1 = ttk.Treeview(root)
        tabla1['columns'] = ('Tipo', 'Documento', 'Apellido', 'Segundo Apellido', 'Nombre1', 'Segundo nombre',
                            'Fecha Nacimiento', 'Genero', 'Sisben')
        tabla1.column('#0', width=0, stretch=NO)
        #tabla1.column('Codigo', anchor=CENTER, width=100)
        tabla1.column('Tipo', anchor=CENTER, width=100)
        tabla1.column('Documento', anchor=CENTER, width=150)
        tabla1.column('Apellido', anchor=CENTER, width=100)
        tabla1.column('Segundo Apellido', anchor=CENTER, width=100)
        tabla1.column('Nombre1', anchor=CENTER, width=100)
        tabla1.column('Segundo nombre', anchor=CENTER, width=100)
        tabla1.column('Fecha Nacimiento', anchor=CENTER, width=150)
        tabla1.column('Genero', anchor=CENTER, width=100)
        tabla1.column('Sisben', anchor=CENTER, width=150)
        #agregar colunmas
        tabla1.heading('#0', text='', anchor=CENTER)
        #tabla1.heading('Codigo', text='Codigo', anchor=CENTER)
        tabla1.heading('Tipo', text='Tipo', anchor=CENTER)
        tabla1.heading('Documento', text='Documento', anchor=CENTER)
        tabla1.heading('Apellido', text='Apellido', anchor=CENTER)
        tabla1.heading('Segundo Apellido', text='Segundo Apellido', anchor=CENTER)
        tabla1.heading('Nombre1', text='Nombre1', anchor=CENTER)
        tabla1.heading('Segundo nombre', text='Segundo nombre', anchor=CENTER)
        tabla1.heading('Fecha Nacimiento', text='Fecha Nacimiento', anchor=CENTER)
        tabla1.heading('Genero', text='Genero', anchor=CENTER)
        tabla1.heading('Sisben', text='Sisben', anchor=CENTER)     
        #ciclo que organiza
        for linea in archivo_lectura:
            nl += 1
            linea = linea.rstrip()
            registro = linea.split(sep=',')
            #codigo = registro[0]
            tipo = registro[0]
            documento = registro[1]
            apellido = registro[2]
            sec_apellido = registro[3]
            nombre1 = registro[4]
            nombre2 = registro[5]
            fecha_nacimiento = registro[6]
            genero = registro[7]
            Sisben = registro[8]
            tabla1.insert(parent='', index='end', iid=nl, text='', values=(
                tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero, Sisben
            ))
        tabla1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

def archivos():
    global registros_correctos
    global sw
    archivo = filename
    with open(archivo, "r") as archivo_lectura:
        registros = []
        registros_correctos = []
        registros_erroneos = []
        nl = 0
        sw = 0
        tabla = ttk.Treeview(root)
        tabla['columns'] = ('Tipo', 'Documento', 'Apellido', 'Segundo Apellido', 'Primer nombre', 'Segundo nombre',
                            'Fecha Nacimiento', 'Genero', 'Sisben', 'Error')
        tabla.column('#0', width=0, stretch=NO)
        tabla.column('Tipo', anchor=CENTER, width=100)
        tabla.column('Documento', anchor=CENTER, width=150)
        tabla.column('Apellido', anchor=CENTER, width=100)
        tabla.column('Segundo Apellido', anchor=CENTER, width=100)
        tabla.column('Primer nombre', anchor=CENTER, width=100)
        tabla.column('Segundo nombre', anchor=CENTER, width=100)
        tabla.column('Fecha Nacimiento', anchor=CENTER, width=150)
        tabla.column('Genero', anchor=CENTER, width=100)
        tabla.column('Sisben', anchor=CENTER, width=150)
        tabla.column('Error', anchor=CENTER, width=200)  # Nueva columna para mostrar el error
        
        tabla.heading('#0', text='', anchor=CENTER)
        tabla.heading('Tipo', text='Tipo', anchor=CENTER)
        tabla.heading('Documento', text='Documento', anchor=CENTER)
        tabla.heading('Apellido', text='Apellido', anchor=CENTER)
        tabla.heading('Segundo Apellido', text='Segundo Apellido', anchor=CENTER)
        tabla.heading('Primer nombre', text='Primer nombre', anchor=CENTER)
        tabla.heading('Segundo nombre', text='Segundo nombre', anchor=CENTER)
        tabla.heading('Fecha Nacimiento', text='Fecha Nacimiento', anchor=CENTER)
        tabla.heading('Genero', text='Genero', anchor=CENTER)
        tabla.heading('Sisben', text='Sisben', anchor=CENTER)
        tabla.heading('Error', text='Error', anchor=CENTER)  # Encabezado de la nueva columna
        
        for linea in archivo_lectura:
            nl += 1
            linea = linea.rstrip()
            campo = linea.split(sep=',')
            registros.append(campo)
            tipo = campo[0]
            documento = campo[1]
            apellido = campo[2]
            sec_apellido = campo[3]
            nombre1 = campo[4]
            nombre2 = campo[5]
            fechas_validas = [fecha for fecha in campo[6].split(',') if eliminar_fechas_incorrectas(fecha)]
            fecha_nacimiento = ', '.join(fechas_validas)
            genero = campo[7]
            Sisben = campo[8]
            
            error = ""  # Variable para almacenar el mensaje de error
            
            if (
                documento == "" or
                not documento.isdigit() or
                (apellido == "" or not apellido.isalpha()) or
                (tipo not in ['CC', 'TI', 'RC', 'PT','SC','PA','PE','CE','CN']) or
                (sec_apellido != "" and not sec_apellido.isalpha()) or
                not nombre1.isalpha() or
                (nombre2 != "" and not nombre2.isalpha()) or
                not eliminar_fechas_incorrectas(fecha_nacimiento) or
                genero not in ["M", "F"]
            ):  
                registros_erroneos.append((nl, tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero, Sisben, error))
            else:
                registros_correctos.append((tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero, Sisben))

        tabla.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")
    mostrar_tabla_errores(tabla, registros_erroneos)

def nada():
    messagebox.showinfo(message="Opcion Vacia", title="En construcción")

def acercade():
    messagebox.showinfo(message="By Farid Muriel", title="Acerca de...")

def Ventana1():
    global root
    global filename
    root = Tk()
    root.iconbitmap('punpun1.ico')
    root.geometry("1500x400") 
    root.title("Menu principal") 
    ventana = Menu(root)

    filemenu = Menu(ventana, tearoff=0)
    filemenu.add_command(label="Cargar", command=abrir)
    filemenu.add_command(label="Validar", command=fun_unidas2)
    filemenu.add_command(label="Mostrar", command=fun_unidas3)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=fun_unidas)
    ventana.add_cascade(label="Archivo", menu=filemenu) 

    gestionmenu = Menu(ventana, tearoff=0)
    gestionmenu.add_command(label="Agregar Registro", command=fun_unidas6)
    gestionmenu.add_command(label="Eliminar Registro", command=fun_unidas5)
    gestionmenu.add_command(label="Buscar", command=fun_unidas4)
    ventana.add_cascade(label="Gestion", menu=gestionmenu)

    helpmenu = Menu(ventana, tearoff=0)
    helpmenu.add_command(label="Ayuda", command=nada)
    helpmenu.add_separator()
    helpmenu.add_command(label="About...", command=acercade)
    ventana.add_cascade(label="Ayuda", menu=helpmenu)
    root.config(menu=ventana)

    root.mainloop()

def ventana_salida2():
    ventana_temporal = Toplevel(root)
    ventana_temporal.geometry("500x400")
    ventana_temporal.title("Salida")
    tex=tk.Label(ventana_temporal,text="Has salido con exito", bg="brown2")
    tex.pack(fill=X)
    tex.configure(font=("Berlin Sans FB", 16, "italic"))
    autor=tk.Label(ventana_temporal,text="By_Farid_Muriel_2023",bg="brown2")
    autor.pack(fill=X,side=tk.BOTTOM)
    autor.configure(font=("Berlin Sans FB", 16, "italic"))
    ventana_temporal.after(1500, ventana_temporal.destroy)
    global imagen
    imagen = PhotoImage(file="")
    label_imagen = Label(ventana_temporal, image=imagen)
    label_imagen.pack()

def salir_ventana_secundaria(ventana2):
    result = messagebox.askquestion("Confirmar", "¿Estás seguro de que deseas salir?")
    if result == "yes":
        ventana2.destroy()

def salir_ventana_secundaria(Ventana3):
    result = messagebox.askquestion("Confirmar", "¿Estás seguro de que deseas salir?")
    if result == "yes":
        Ventana3.destroy()

def Ventana2():
    root2= Toplevel(root)
    root2.iconbitmap('punpun1.ico')
    root2.geometry("600x250")
    root2.title("Agregar registro")
    root2.focus()
    variable_identificacion= StringVar()
    variable_prapeliido=StringVar()
    variable_seapellido=StringVar()
    variable_prnombre=StringVar()
    variable_senombre=StringVar()
    variable_nivel=StringVar()
    variable_fecha=tk.StringVar()
    variable_tipo=tk.StringVar()
    variable_sexo=tk.StringVar()
    
    titulo1= Label(root2,text="Tipo")
    titulo1.pack()
    titulo1.place(x=50, y=20,anchor="center")
    opciones = ['CC', 'TI', 'RC', 'PT','SC','PA','PE','CE','CN']
    def obtener_seleccion(event):
        seleccion = entrada1.get()
        variable_tipo.set(seleccion)
        print( variable_tipo.get())
    entrada1 = ttk.Combobox(root2, values=opciones, textvariable=variable_tipo,width=5)
    entrada1.pack()
    entrada1.bind("<<ComboboxSelected>>", obtener_seleccion)
    entrada1.place(x=170, y=20,anchor="center")
    
    titulo2= Label(root2,text="Identificacion")
    titulo2.pack()
    titulo2.place(x=50, y=50,anchor="center")
    entrada2= Entry(root2,textvariable=variable_identificacion)
    entrada2.pack()
    entrada2.place(x=170, y=50,anchor="center")

    titulo3= Label(root2,text="Primer apellido")
    titulo3.pack()
    titulo3.place(x=50, y=75,anchor="center")
    entrada3= Entry(root2,textvariable=variable_prapeliido)
    entrada3.pack()
    entrada3.place(x=170, y=75,anchor="center")

    titulo4= Label(root2,text="Segundo apellido")
    titulo4.pack()
    titulo4.place(x=50, y=100,anchor="center")
    entrada4= Entry(root2,textvariable=variable_seapellido)
    entrada4.pack()
    entrada4.place(x=170, y=100,anchor="center")
    #otra columna
    titulo5= Label(root2,text="Primer nombre")
    titulo5.pack()
    titulo5.place(x=300, y=20,anchor="center")
    entrada5= Entry(root2,textvariable=variable_prnombre)
    entrada5.pack()
    entrada5.place(x=420, y=20,anchor="center")

    titulo6= Label(root2,text="Segundo nombre")
    titulo6.pack()
    titulo6.place(x=300, y=50,anchor="center")
    entrada6= Entry(root2,textvariable=variable_senombre)
    entrada6.pack()
    entrada6.place(x=420, y=50,anchor="center")

    titulo7= Label(root2,text="Fechas de nacimiento")
    titulo7.pack()
    titulo7.place(x=300, y=75,anchor="center")
    """
    def mostrar_calendario(event):
        def seleccionar_fecha():
            fecha_seleccionada = calendario.selection_get().strftime("%d/%m/%Y")
            print("Fecha seleccionada:", fecha_seleccionada)
            variable_fecha.set(fecha_seleccionada)
            ventana_calendario.destroy()

        ventana_calendario = tk.Toplevel(root2)
        calendario = Calendar(ventana_calendario, selectmode="day", date_pattern="dd/mm/yy")
        calendario.pack(pady=10)
        boton_seleccionar = ttk.Button(ventana_calendario, text="Seleccionar", command=seleccionar_fecha)
        boton_seleccionar.pack()
    entrada7= ttk.Combobox(root2, textvariable=variable_fecha, values=["Seleccionar fecha"],width=15)
    entrada7.bind("<<ComboboxSelected>>", mostrar_calendario)
    """
    entrada7=Entry(root2,textvariable=variable_fecha)
    entrada7.pack()
    entrada7.place(x=420, y=75,anchor="center")

    titulo8= Label(root2,text="Sexo")
    titulo8.pack()
    titulo8.place(x=300, y=100,anchor="center")
    sexo = ['M', 'F']
    def obtener_seleccion_s(event):
        seleccion = entrada8.get()
        variable_sexo.set(seleccion)
        print( variable_sexo.get())
    entrada8 = ttk.Combobox(root2, values=sexo, textvariable=variable_sexo,width=10)
    entrada8.pack()
    entrada8.bind("<<ComboboxSelected>>", obtener_seleccion_s)
    entrada8.place(x=420, y=100,anchor="center")

    titulo9=Label(root2,text="Nivel")
    titulo9.pack()
    titulo9.place(x=250, y=150,anchor="center")
    sisben = [
        "A01", "A02", "A03", "A04", "A05",
        "B01", "B02", "B03", "B04", "B05", "B06", "B07",
        "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12",
        "C13", "C14", "C15", "C16", "C17", "C18",
        "D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D12",
        "D13", "D14", "D15", "D16", "D17", "D18", "D19", "D20", "D21"
    ]
    def obtener_seleccion_n(event):
        seleccion = entrada9.get()
        variable_nivel.set(seleccion)
        print( variable_nivel.get())
    entrada9 = ttk.Combobox(root2, values=sisben, textvariable=variable_nivel,width=5)
    entrada9.pack()
    entrada9.bind("<<ComboboxSelected>>", obtener_seleccion_n)
    entrada9.place(x=300, y=150,anchor="center")
    global xx
    xx="linea",variable_tipo.get(),variable_identificacion.get(),variable_prapeliido.get(),variable_seapellido.get(),variable_prnombre.get(),variable_senombre.get(),variable_fecha.get(),variable_nivel.get()
    def validacion():
        campos = {
            "variable_1": variable_tipo.get(),
            "variable_2": variable_identificacion.get(),
            "variable_3": variable_prapeliido.get(),
            "variable_4": variable_seapellido.get(),
            "variable_5": variable_prnombre.get(),
            "variable_6": variable_senombre.get(),
            "variable_7": variable_fecha.get(),
            "variable_8": variable_sexo.get(),
            "variable_9": variable_nivel.get()
        }
        global campo
        global cp
        cp=0
        obligatorio=["variable_1","variable_2","variable_3","variable_5","variable_7","variable_8"]
        for campo in obligatorio:
            if not campo:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return False

        if not re.match(r'^[0-9]+$', campos["variable_2"]):
            messagebox.showerror("Error", "La identificación debe contener solo números.")
            cp=1
            return False
 
        if not re.match(r'^[a-zA-Z]+$', campos["variable_3"]):
            messagebox.showerror("Error", "Error en el primer apellido ingresado")
            cp=1
            return False

        if not re.match(r'^[a-zA-Z]*$', campos["variable_4"]):
            messagebox.showerror("Error", "Error en el segundo apellido ingresado")
            cp=1
            return False

        if not re.match(r'^[a-zA-Z]+$', campos["variable_5"]):
            messagebox.showerror("Error", "Error en el primer nombre ingresado")
            cp=1
            return False
        
        fecha=variable_fecha.get()
        patron = r"^(0[1-9]|1[0-9]|2[0-9]|3[01])/(0[1-9]|1[012])/\d{4}$"
        if re.match(patron, fecha):
            dia=int(fecha[0:2])
            mes=int(fecha[3:5])
            año = int(fecha[6:10])
            if mes in [1, 3, 5, 7, 8, 10, 12]: 
                    if dia <= 31:
                        print("Fecha valida")
                    else:
                        messagebox.showerror("Error", "dia invalido")
                        cp=1
            elif mes in [4, 6, 9, 11]:
                if dia<=30:
                    print("valida")
                else:
                    messagebox.showerror("Error", "dia invalido")
                    cp=1
            elif mes == 2:
                if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
                    if dia <= 29:
                        print("Fecha válida")
                    else:
                        messagebox.showerror("Error", "dia invalido")
                        cp=1
                else:
                    if dia<=28:
                        print("valido")
                    else:
                        messagebox.showerror("Error", "dia invalido")
                        cp=1
            else:
                messagebox.showerror("Error", "Error en la fecha ingresada")
                cp=1
        else:
            messagebox.showerror("Error", "Error en la fecha ingresada, recuerde el formato dd/mm/aaaa")
            cp=1

        if not re.match(r'^[a-zA-Z]*$', campos["variable_6"]):
            messagebox.showerror("Error", "Error en el segundo nombre ingresado")
            cp=1
            return False

        return campos

    def guardar():
        campos = validacion()
        global cp
        global arch
        if cp == 1:
            return False
        else:
            if campos:
                messagebox.showinfo(message="linea:"+(str(variable_tipo.get()))+","+(str(variable_identificacion.get()))+","+(str(variable_prapeliido.get()))+","+(str(variable_seapellido.get()))+","+(str(variable_prnombre.get()))+","+(str(variable_senombre.get()))+","+(str(variable_fecha.get()))+","+(str(variable_nivel.get())),title="guardado")
                linea=(str(variable_tipo.get()))+","+(str(variable_identificacion.get()))+","+(str(variable_prapeliido.get()))+","+(str(variable_seapellido.get()))+","+(str(variable_prnombre.get()))+","+(str(variable_senombre.get()))+","+(str(variable_fecha.get()))+","+(str(variable_nivel.get()))
                proceso(linea)

                confirmacion_otro = messagebox.askyesno("Agregar otro registro", "¿Deseas agregar otro registro?")
                if confirmacion_otro:
                    reiniciar_ventana(root2)
                else:
                    salir_ventana_secundaria(root2)

    def reiniciar_ventana(ventana):
        ventana.destroy()
        Ventana2()

    def proceso(linea):
        try:
            archivo=filename
            linea = linea.rstrip()
            print("::> ",linea)
            with open(archivo, 'a') as temp_file:
                #cad=cad[:-n]
                temp_file.write(linea+"\n")
                temp_file.close()
            with open(archivo, "r") as archivo_lectura:
                total_lines = sum(1 for line in archivo_lectura)
            print("Archivo procesado.",total_lines)
        except FileNotFoundError:
            messagebox.showinfo("Archivo no encontrado", "No se encontró el archivo 'usuarios_lite.txt'.")

    #boton1
    botonguar=Button(root2, text="Guardar", command=guardar,bg="gray63",fg="white")
    botonguar.pack()
    botonguar.place(x=420, y=150,anchor="center")
    #boton2
    botonsalir=Button(root2, text="Salir", command=lambda: salir_ventana_secundaria(root2),bg="gray63",fg="white")
    botonsalir.place(x=500, y=150,anchor="center")

    root2.mainloop()

def Ventana3():
    root3 = Tk()
    root3.iconbitmap('punpun1.ico')
    root3.geometry("900x600")
    root3.title("Buscar registro")
    root3.grab_set()
    root3.focus()

    titulo2 = Label(root3, text="Identificacion")
    titulo2.place(x=50, y=20, anchor="center")
    entrada2 = Entry(root3)
    entrada2.place(x=170, y=20, anchor="center")

    titulo5 = Label(root3, text="Primer nombre")
    titulo5.place(x=50, y=48, anchor="center")
    entrada5 = Entry(root3)
    entrada5.place(x=170, y=48, anchor="center")

    titulo3 = Label(root3, text="Primer apellido")
    titulo3.place(x=50, y=75, anchor="center")
    entrada3 = Entry(root3)
    entrada3.place(x=170, y=75, anchor="center")

    def buscar():
        identificacion = entrada2.get();prnombre = entrada5.get(); prapellido = entrada3.get()
        print(prnombre);print(identificacion);print(prapellido)
        tabla2.delete(*tabla2.get_children())  # Vaciar la tabla
        archivo = filename
        encontrado = False  # Variable para controlar si se encontró algún archivo

        with open(archivo, "r") as archivo_lectura:
            for linea in archivo_lectura:
                linea = linea.rstrip()
                campo = linea.split(sep=',')
                if (identificacion == campo[1]):
                    encontrado = True
                    #codigo = campo[0]
                    tipo = campo[0]
                    documento = campo[1]
                    apellido = campo[2]
                    sec_apellido = campo[3]
                    nombre1 = campo[4]
                    nombre2 = campo[5]
                    fecha_nacimiento = campo[6]
                    genero = campo[7]
                    Sisben = campo[8]
                    tabla2.insert(parent='', index='end', text='', values=(
                        tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero,
                        Sisben
                    ))
                elif (prapellido == campo[2]):
                    encontrado = True
                    tipo = campo[0]
                    documento = campo[1]
                    apellido = campo[2]
                    sec_apellido = campo[3]
                    nombre1 = campo[4]
                    nombre2 = campo[5]
                    fecha_nacimiento = campo[6]
                    genero = campo[7]
                    Sisben = campo[8]
                    tabla2.insert(parent='', index='end', text='', values=(
                        tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero,
                        Sisben
                    ))
                elif (prnombre == campo[4]):
                    encontrado = True
                    #codigo = campo[0]
                    tipo = campo[0]
                    documento = campo[1]
                    apellido = campo[2]
                    sec_apellido = campo[3]
                    nombre1 = campo[4]
                    nombre2 = campo[5]
                    fecha_nacimiento = campo[6]
                    genero = campo[7]
                    Sisben = campo[8]
                    tabla2.insert(parent='', index='end', text='', values=(
                        tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero,
                        Sisben
                    ))
        if not encontrado:
            messagebox.showinfo("Información", "No se encontró ningún archivo congruente a los datos ingresados.")

    botonbus = Button(root3, text="Buscar", command=buscar, bg="gray63", fg="white")
    botonbus.pack()
    botonbus.place(x=300, y=60, anchor="center")
    botonsalir=Button(root3, text="Salir", command=lambda: salir_ventana_secundaria(root3),bg="gray63",fg="white")
    botonsalir.place(x=500, y=60,anchor="center")

    # Agregar Treeview
    tabla2 = ttk.Treeview(root3)
    tabla2['columns'] = ('Tipo', 'Documento', 'Apellido', 'Segundo Apellido', 'Nombre1', 'Segundo nombre',
                         'Fecha Nacimiento', 'Genero', 'Sisben')
    tabla2.column('#0', width=0, stretch=NO)
    #tabla2.column('codigo', anchor=CENTER, width=150)
    tabla2.column('Tipo', anchor=CENTER, width=100)
    tabla2.column('Documento', anchor=CENTER, width=150)
    tabla2.column('Apellido', anchor=CENTER, width=100)
    tabla2.column('Segundo Apellido', anchor=CENTER, width=100)
    tabla2.column('Nombre1', anchor=CENTER, width=100)
    tabla2.column('Segundo nombre', anchor=CENTER, width=100)
    tabla2.column('Fecha Nacimiento', anchor=CENTER, width=150)
    tabla2.column('Genero', anchor=CENTER, width=100)
    tabla2.column('Sisben', anchor=CENTER, width=150)

    tabla2.heading('#0', text='', anchor=CENTER)
    #tabla2.heading('codigo', text='codigo', anchor=CENTER)
    tabla2.heading('Tipo', text='Tipo', anchor=CENTER)
    tabla2.heading('Documento', text='Documento', anchor=CENTER)
    tabla2.heading('Apellido', text='Apellido', anchor=CENTER)
    tabla2.heading('Segundo Apellido', text='Segundo Apellido', anchor=CENTER)
    tabla2.heading('Nombre1', text='Primer nombre', anchor=CENTER)
    tabla2.heading('Segundo nombre', text='Segundo nombre', anchor=CENTER)
    tabla2.heading('Fecha Nacimiento', text='Fecha Nacimiento', anchor=CENTER)
    tabla2.heading('Genero', text='Genero', anchor=CENTER)
    tabla2.heading('Sisben', text='Sisben', anchor=CENTER)

    tabla2.place(x=450, y=300, anchor="center", width=800, height=300)
    root3.mainloop()

def Ventana4():
    root4 = Tk()
    root4.iconbitmap('punpun1.ico')
    root4.geometry("1200x600")
    root4.title("Buscar registro")
    root4.grab_set()
    root4.focus()

    titulo2 = Label(root4, text="Identificacion")
    titulo2.place(x=50, y=48, anchor="center")
    entrada2 = Entry(root4)
    entrada2.place(x=170, y=48, anchor="center")

    titulo5 = Label(root4, text="Primer nombre")
    titulo5.place(x=300, y=48, anchor="center")
    entrada5 = Entry(root4)
    entrada5.place(x=459, y=48, anchor="center")

    titulo3 = Label(root4, text="Primer apellido")
    titulo3.place(x=600, y=48, anchor="center")
    entrada3 = Entry(root4)
    entrada3.place(x=800, y=48, anchor="center")

    def buscar():
        global selected_line
        identificacion = entrada2.get();prnombre = entrada5.get(); prapellido = entrada3.get()
        print(prnombre);print(identificacion);print(prapellido)
        tabla2.delete(*tabla2.get_children())  # Vaciar la tabla
        archivo = filename
        encontrado = False  # Variable para controlar si se encontró algún archivo

        with open(archivo, "r") as archivo_lectura:
            for linea in archivo_lectura:
                linea = linea.rstrip()
                campo = linea.split(sep=',')
                if (identificacion == campo[1]):
                    encontrado = True
                    #codigo = campo[0]
                    tipo = campo[0]
                    documento = campo[1]
                    apellido = campo[2]
                    sec_apellido = campo[3]
                    nombre1 = campo[4]
                    nombre2 = campo[5]
                    fecha_nacimiento = campo[6]
                    genero = campo[7]
                    Sisben = campo[8]
                    tabla2.insert(parent='', index='end', text='', values=(
                        tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero,
                        Sisben
                    ))
                elif (prapellido == campo[2]):
                    encontrado = True
                    #codigo = campo[0]
                    tipo = campo[0]
                    documento = campo[1]
                    apellido = campo[2]
                    sec_apellido = campo[3]
                    nombre1 = campo[4]
                    nombre2 = campo[5]
                    fecha_nacimiento = campo[6]
                    genero = campo[7]
                    Sisben = campo[8]
                    tabla2.insert(parent='', index='end', text='', values=(
                        tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero,
                        Sisben
                    ))
                elif (prnombre == campo[4]):
                    encontrado = True
                    #codigo = campo[0]
                    tipo = campo[0]
                    documento = campo[1]
                    apellido = campo[2]
                    sec_apellido = campo[3]
                    nombre1 = campo[4]
                    nombre2 = campo[5]
                    fecha_nacimiento = campo[6]
                    genero = campo[7]
                    Sisben = campo[8]
                    tabla2.insert(parent='', index='end', text='', values=(
                        tipo, documento, apellido, sec_apellido, nombre1, nombre2, fecha_nacimiento, genero,
                        Sisben
                    ))
                selected_line = linea
        if not encontrado:
            messagebox.showinfo("Información", "No se encontró ningún archivo congruente a los datos ingresados.")

    def eliminar_registro():
        archivo = filename
        seleccionados = tabla2.selection()
        if seleccionados:
            confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar el registro seleccionado?")
            if confirmacion:
                # Obtener el registro seleccionado
                seleccionado = seleccionados[0]  # Suponiendo que solo se puede seleccionar un registro a la vez
                # Obtener los valores del registro seleccionado
                valores = tabla2.item(seleccionado, 'values')
                codigo = valores[0]  # Suponiendo que el código del registro está en la primera columna

                # Mostrar la línea de registro que se eliminará
                registro = ','.join(valores)
                messagebox.showinfo("Registro a eliminar", f"Registro a eliminar:\n{registro}")

                # Abrir el archivo original y crear un nuevo archivo temporal
                archivo_temporal = "Usuarios_lite_temp.txt"
                with open(archivo, "r") as archivo_lectura, open(archivo_temporal, "w") as archivo_temp:
                    for linea in archivo_lectura:
                        registro = linea.rstrip().split(',')
                        if registro[0] != codigo:
                            # Si el código del registro no coincide con el código del registro seleccionado,
                            # escribir la línea en el archivo temporal
                            archivo_temp.write(linea)

                # Eliminar el archivo original
                os.remove(archivo)
                # Renombrar el archivo temporal como el archivo original
                os.rename(archivo_temporal, archivo)

                # Eliminar el registro de la tabla
                tabla2.delete(seleccionado)

                messagebox.showinfo("Eliminación exitosa", "El registro fue eliminado exitosamente.")
        else:
            messagebox.showinfo("No hay registros seleccionados", "No se ha seleccionado ningún registro para eliminar.")


    botoneli = Button(root4, text="buscar", command=buscar, bg="gray63", fg="white")
    botoneli.pack()
    botoneli.place(x=600, y=500, anchor="center")
    botondel = Button(root4, text="Eliminar", command=eliminar_registro, bg="gray63", fg="white")
    botondel.pack()
    botondel.place(x=700, y=500, anchor="center")
    botonsalir=Button(root4, text="Salir", command=lambda: salir_ventana_secundaria(root4),bg="gray63",fg="white")
    botonsalir.place(x=800, y=500,anchor="center")
    # Agregar Treeview
    tabla2 = ttk.Treeview(root4)
    tabla2['columns'] = ('Tipo', 'Documento', 'Apellido', 'Segundo Apellido', 'Primer nombre', 'Segundo nombre',
                         'Fecha Nacimiento', 'Genero', 'Sisben')
    tabla2.column('#0', width=0, stretch=NO)
    #tabla2.column('codigo', anchor=CENTER, width=150)
    tabla2.column('Tipo', anchor=CENTER, width=20)
    tabla2.column('Documento', anchor=CENTER, width=50)
    tabla2.column('Apellido', anchor=CENTER, width=50)
    tabla2.column('Segundo Apellido', anchor=CENTER, width=50)
    tabla2.column('Primer nombre', anchor=CENTER, width=50)
    tabla2.column('Segundo nombre', anchor=CENTER, width=50)
    tabla2.column('Fecha Nacimiento', anchor=CENTER, width=50)
    tabla2.column('Genero', anchor=CENTER, width=20)
    tabla2.column('Sisben', anchor=CENTER, width=30)

    tabla2.heading('#0', text='', anchor=CENTER)
    #tabla2.heading('codigo', text='codigo', anchor=CENTER)
    tabla2.heading('Tipo', text='Tipo', anchor=CENTER)
    tabla2.heading('Documento', text='Documento', anchor=CENTER)
    tabla2.heading('Apellido', text='Apellido', anchor=CENTER)
    tabla2.heading('Segundo Apellido', text='Segundo Apellido', anchor=CENTER)
    tabla2.heading('Primer nombre', text='Primer nombre', anchor=CENTER)
    tabla2.heading('Segundo nombre', text='Segundo nombre', anchor=CENTER)
    tabla2.heading('Fecha Nacimiento', text='Fecha Nacimiento', anchor=CENTER)
    tabla2.heading('Genero', text='Genero', anchor=CENTER)
    tabla2.heading('Sisben', text='Sisben', anchor=CENTER)

    tabla2.place(x=600, y=300, anchor="center", width=1100, height=350)
    root4.mainloop()

Ventana1()
#Ventana2()
#Ventana3()