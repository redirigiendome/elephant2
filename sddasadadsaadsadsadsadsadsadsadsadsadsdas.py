import tkinter as tkin  # Se usará el ".tkin" en vez de usar el "tk" en todo el código
from tkinter import messagebox  # Importa la ventana emergente para mostrar mensajes
from tkinter import ttk  # Importa el módulo ttk para usar el Combobox

class app:
    def __init__(self, dea):
        self.dea = dea  # dea = formulario 
        self.dea.title("Form pr")

        # Menú de la aplicación
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

        # Imprime texto nombre
        self.label_nombre = tkin.Label(dea, text="Nombre")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        # Abre la posibilidad de poner el nombre en Texto abierto
        self.entry_nombre = tkin.Entry(dea)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Imprime texto edad
        self.label_edad = tkin.Label(dea, text="Que edad tienes")
        self.label_edad.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Se abre la entrada para poner edad
        self.entry_edad = tkin.Entry(dea)
        self.entry_edad.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_preguntita = tkin.Label(dea, text="Te sientes apto para participar?")
        self.label_preguntita.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        # StringVar gestiona y sincroniza valores de texto en Tkinter
        self.genero = tkin.StringVar(value="No especificado")

        # Opciones de los géneros a elegir
        self.radio_masculino = tkin.Radiobutton(dea, text="Masculino", variable=self.genero, value="Masculino")
        self.radio_masculino.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.radio_femenino = tkin.Radiobutton(dea, text="Femenino", variable=self.genero, value="Femenino")
        self.radio_femenino.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Listbox con selección múltiple
        self.listbox = tkin.Listbox(dea, selectmode=tkin.MULTIPLE)
        self.listbox.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")
        self.listbox.insert(0, "Opcion 1")
        self.listbox.insert(1, "Opcion 2")
        self.listbox.insert(2, "Opcion 3")

        self.label_listbox = tkin.Label(dea, text="Recuperar seleccion")
        self.label_listbox.grid(row=6, column=0, columnspan=2, pady=5, sticky="n")

        self.boton_recuperar = tkin.Button(dea, text="Recuperar", command=self.recuperar)
        self.boton_recuperar.grid(row=7, column=0, columnspan=2, pady=5)

        # Añadir un Combobox
        self.label_combobox = tkin.Label(dea, text="Selecciona una opción")
        self.label_combobox.grid(row=8, column=0, padx=10, pady=10, sticky="e")

        self.combobox = ttk.Combobox(dea, values=["Opción 1", "Opción 2", "Opción 3"])
        self.combobox.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        # Añadir Checkbuttons
        self.label_checkbuttons = tkin.Label(dea, text="Selecciona opciones")
        self.label_checkbuttons.grid(row=9, column=0, padx=10, pady=10, sticky="e")

        # Crear BooleanVars para los Checkbuttons
        self.check1_var = tkin.BooleanVar()
        self.check2_var = tkin.BooleanVar()
        self.check3_var = tkin.BooleanVar()

        self.check1 = tkin.Checkbutton(dea, text="Opción 1", variable=self.check1_var)
        self.check1.grid(row=10, column=0, padx=10, pady=5)

        self.check2 = tkin.Checkbutton(dea, text="Opción 2", variable=self.check2_var)
        self.check2.grid(row=10, column=1, padx=10, pady=5)

        self.check3 = tkin.Checkbutton(dea, text="Opción 3", variable=self.check3_var)
        self.check3.grid(row=10, column=2, padx=10, pady=5)

        # Botón para enviar el formulario en la parte inferior
        self.boton_env = tkin.Button(dea, text="Enviar", command=self.enviar_datos)
        self.boton_env.grid(row=11, column=0, columnspan=3, pady=10)

        # Ajustar el peso de las filas y columnas para que se expanda correctamente
        #dea.grid_rowconfigure(11, weight=1)
        #dea.grid_columnconfigure(0, weight=1)
        #dea.grid_columnconfigure(1, weight=1)
        #dea.grid_columnconfigure(2, weight=1)

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

        # Obtener el estado de los Checkbuttons
        check1 = "Seleccionado" if self.check1_var.get() else "No seleccionado"
        check2 = "Seleccionado" if self.check2_var.get() else "No seleccionado"
        check3 = "Seleccionado" if self.check3_var.get() else "No seleccionado"

        # Y aquí llega la ventana que va a salir cuando envías los datos  
        messagebox.showinfo("Info", f"Nombre: {nombre}\nEdad: {edad}\nGenero: {genero}\n\nSeleccion Listbox:\n{seleccion_listbox}\n\nSeleccion Combobox:\n{seleccion_combobox}\n\nCheckbuttons:\nOpción 1: {check1}\nOpción 2: {check2}\nOpción 3: {check3}")

    # Métodos para cambiar el color de fondo y tamaño de la ventana
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
