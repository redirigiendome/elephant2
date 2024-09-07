
#Funciones y usos de todo el codigo

#Crear menu para herramientas = Menu
#Menu desplegable = Add_cascade

#Fuentes = font=(fuente, tamaño)
#Posicionar = Grid("Matriz" Fila y columna )
#Margen de pixeles=  Padx=0 - Pady=0

#sticky="n": El widget se alinea a la parte superior.
#sticky="e": El widget se alinea a la derecha.
#sticky="s": El widget se alinea a la parte inferior.
#sticky="w": El widget se alinea a la izquierda.
#sticky="ns": El widget se expande verticalmente para llenar toda la altura de la celda.
#sticky="ew": El widget se expande horizontalmente para llenar toda la anchura de la celda.
#sticky="nsew": El widget se expande para llenar toda la celda, en todas las direcciones.


#Crear otra ventana = Toplevel
#Ocultar widget de la ventana = grid_forget()

#Almacena booleanos (True o False) =BooleanVar

#Indicar cuantas columnas ocupara la funcion = grid (Columnspan())
#Sincroniza valores de texto = Facilita la sincronizacion automatica del texto entre diferentes widgets = Stringvar 


#Modificar Resolucion = Geometry
#Modificar Color = Configure

#Lambda argumento: expresion // Funcion sin poner todo un texto largo

#No doy mas wacho



import tkinter as tkin
from tkinter import messagebox
from tkinter import ttk


class app:
    def __init__(self, dea):
        self.dea = dea
        self.dea.title("Form pr")

        # Menu de la aplicacion
        menubar1 = tkin.Menu(self.dea)
        self.dea.config(menu=menubar1)

        opciones1 = tkin.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="Colores", menu=opciones1)
        opciones1.add_command(label="Fondo Negro", command=self.fijarrojo)
        opciones1.add_command(label="Fondo Verde", command=self.fijarverde)
        opciones1.add_command(label="Fondo Azul", command=self.fijarazul)

        opciones2 = tkin.Menu(menubar1)
        menubar1.add_cascade(label="Tamanos", menu=opciones2)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)

        # Nuevo apartado de menu "Sugerencias"
        sugerencias_menu = tkin.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="Sugerencias", menu=sugerencias_menu)
        sugerencias_menu.add_command(label="Abrir ventana de sugerencias", command=self.abrir_sugerencias)

        # Crear notebook
        self.notebook = ttk.Notebook(self.dea)
        self.notebook.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Pestaña 1: Nombre de usuario y contrasena
        self.tab1 = tkin.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Login")
                                    
        self.label_usuario = tkin.Label(self.tab1, text="Nombre de usuario:", font=("Verdana", 10))
        self.label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_usuario = tkin.Entry(self.tab1, font=("Verdana", 10))
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_contrasena = tkin.Label(self.tab1, text="Contrasena:", font=("Verdana", 10))
        self.label_contrasena.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_contrasena = tkin.Entry(self.tab1, show="*", font=("Verdana", 10))
        self.entry_contrasena.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.boton_login = tkin.Button(self.tab1, text="Login", command=self.convertir_login, font=("Verdana", 10))
        self.boton_login.grid(row=2, column=0, columnspan=2, pady=10)

        # Pestaña 2: Formulario
        self.tab2 = tkin.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Formulario")

        # Etiqueta y entrada para nombre
        self.label_nombre = tkin.Label(self.tab2, text="Nombre", font=("Verdana", 10))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_nombre = tkin.Entry(self.tab2, font=("Verdana", 10))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Etiqueta y entrada para edad
        self.label_edad = tkin.Label(self.tab2, text="Que edad tienes", font=("Verdana", 10))
        self.label_edad.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_edad = tkin.Entry(self.tab2, font=("Verdana", 10))
        self.entry_edad.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_pregunta = tkin.Label(self.tab2, text="Te sientes apto para participar?", font=("Verdana", 10))
        self.label_pregunta.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        # Opciones de los generos a elegir
        self.genero = tkin.StringVar(value="No especificado")

        self.radio_masculino = tkin.Radiobutton(self.tab2, text="Masculino", variable=self.genero, value="Masculino", font=("Verdana", 10))
        self.radio_masculino.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.radio_femenino = tkin.Radiobutton(self.tab2, text="Femenino", variable=self.genero, value="Femenino", font=("Verdana", 10))
        self.radio_femenino.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Listbox con seleccion multiple
        self.listbox = tkin.Listbox(self.tab2, selectmode=tkin.MULTIPLE, font=("Verdana", 10))
        self.listbox.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")
        self.listbox.insert(0, "Opcion 1")
        self.listbox.insert(1, "Opcion 2")
        self.listbox.insert(2, "Opcion 3")

        self.label_listbox = tkin.Label(self.tab2, text="Recuperar seleccion", font=("Verdana", 10))
        self.label_listbox.grid(row=6, column=0, columnspan=2, pady=5, sticky="n")

        self.boton_recuperar = tkin.Button(self.tab2, text="Recuperar", command=self.recuperar, font=("Verdana", 10))
        self.boton_recuperar.grid(row=7, column=0, columnspan=2, pady=5)

        # Combobox
        self.label_combobox = tkin.Label(self.tab2, text="Selecciona una opcion", font=("Verdana", 10))
        self.label_combobox.grid(row=8, column=0, padx=10, pady=10, sticky="e")

        self.combobox = ttk.Combobox(self.tab2, values=["Opcion 1", "Opcion 2", "Opcion 3"], font=("Verdana", 10))
        self.combobox.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        # Checkbuttons
        self.label_checkbuttons = tkin.Label(self.tab2, text="Selecciona opciones", font=("Verdana", 10))
        self.label_checkbuttons.grid(row=9, column=0, padx=10, pady=10, sticky="e")

        self.check1_var = tkin.BooleanVar()
        self.check2_var = tkin.BooleanVar()
        self.check3_var = tkin.BooleanVar()

        self.check1 = tkin.Checkbutton(self.tab2, text="Opcion 1", variable=self.check1_var, font=("Verdana", 10))
        self.check1.grid(row=10, column=0, padx=10, pady=5)

        self.check2 = tkin.Checkbutton(self.tab2, text="Opcion 2", variable=self.check2_var, font=("Verdana", 10))
        self.check2.grid(row=10, column=1, padx=10, pady=5)

        self.check3 = tkin.Checkbutton(self.tab2, text="Opcion 3", variable=self.check3_var, font=("Verdana", 10))
        self.check3.grid(row=10, column=2, padx=10, pady=5)

        self.boton_env = tkin.Button(self.tab2, text="Enviar", command=self.enviar_datos, font=("Verdana", 10))
        self.boton_env.grid(row=11, column=0, columnspan=3, pady=10)

    def recuperar(self):
        seleccion = ""
        for i in self.listbox.curselection():
            seleccion += self.listbox.get(i) + "\n"
        self.label_listbox.configure(text=seleccion if seleccion else "No hay seleccion")

    def enviar_datos(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        genero = self.genero.get()

        seleccion_listbox = ""
        if len(self.listbox.curselection()) > 0:
            for posicion in self.listbox.curselection():
                seleccion_listbox += self.listbox.get(posicion) + "\n"
        else:
            seleccion_listbox = "No seleccionado"

        seleccion_combobox = self.combobox.get() if self.combobox.get() else "No seleccionado"

        check1 = "Seleccionado" if self.check1_var.get() else "No seleccionado"
        check2 = "Seleccionado" if self.check2_var.get() else "No seleccionado"
        check3 = "Seleccionado" if self.check3_var.get() else "No seleccionado"

        messagebox.showinfo("Info", f"Nombre: {nombre}\nEdad: {edad}\nGenero: {genero}\n\nSeleccion Listbox:\n{seleccion_listbox}\n\nSeleccion Combobox:\n{seleccion_combobox}\n\nCheckbuttons:\nOpcion 1: {check1}\nOpcion 2: {check2}\nOpcion 3: {check3}")

    def abrir_sugerencias(self):
        nueva_ventana = tkin.Toplevel(self.dea)
        nueva_ventana.title("Sugerencias")

        label_sugerencias = tkin.Label(nueva_ventana, text="Escribe tu sugerencia:", font=("Verdana", 10))
        label_sugerencias.grid(row=0, column=0, padx=10, pady=10)

        entry_sugerencias = tkin.Entry(nueva_ventana, font=("Verdana", 10))
        entry_sugerencias.grid(row=1, column=0, padx=10, pady=10)

        boton_enviar_sugerencia = tkin.Button(nueva_ventana, text="Enviar", font=("Verdana", 10), command=lambda: messagebox.showinfo("Sugerencia", "Sugerencia enviada!"))
        boton_enviar_sugerencia.grid(row=2, column=0, padx=10, pady=10)



    def convertir_login(self):
        nombre_usuario = self.entry_usuario.get()
        self.label_usuario.configure(text=f"Usuario: {nombre_usuario}")
        self.entry_usuario.grid_forget()
        self.label_contrasena.configure(text="Contrasena ingresada")
        self.entry_contrasena.grid_forget()
        self.boton_login.grid_forget()

    def fijarrojo(self):
        self.dea.configure(background="black")

    def fijarverde(self):
        self.dea.configure(background="green")

    def fijarazul(self):
        self.dea.configure(background="blue")

    def ventanachica(self):
        self.dea.geometry("640x480")

    def ventanagrande(self):
        self.dea.geometry("1024x800")

# Ejecutor
dea = tkin.Tk()
Apa = app(dea)
dea.mainloop()
