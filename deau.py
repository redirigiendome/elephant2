  import tkinter as tkin  # Se usará el ".tkin" en vez de usar el "tk" en todo el código
from tkinter import messagebox  # Importa la ventana emergente para mostrar mensajes

class app:
    def __init__(self, dea):
        self.dea = dea  # dea = formulario 
        self.dea.title("ya sature >:v")

        # Imprime texto nombre
        self.label_nombre = tkin.Label(dea, text="Nombre")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        # Abre la posibilidad de poner el nombre en Texto abierto
        self.entry_nombre = tkin.Entry(dea)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Imprime texto edad
        self.label_edad = tkin.Label(dea, text="¿Cuál es tu edad?")
        self.label_edad.grid(row=1, column=0, padx=10, pady=10)

        # Se abre la entrada para poner edad
        self.entry_edad = tkin.Entry(dea)
        self.entry_edad.grid(row=1, column=1, padx=10, pady=10)

        self.label_preguntita = tkin.Label(dea, text="¿Qué género eres?")
        self.label_preguntita.grid(row=2, column=0, padx=10, pady=10)

        # StringVar gestiona y sincroniza valores de texto en Tkinter
        self.genero = tkin.StringVar(value="No especificado")

        # Opciones de los géneros a elegir
        self.radio_masculino = tkin.Radiobutton(dea, text="Masculino", variable=self.genero, value="Masculino")
        self.radio_masculino.grid(row=3, column=0, padx=10, pady=5)

        self.radio_femenino = tkin.Radiobutton(dea, text="Femenino", variable=self.genero, value="Femenino")
        self.radio_femenino.grid(row=3, column=1, padx=10, pady=5)

        # Botón para enviar el formulario 
        self.boton_env = tkin.Button(dea, text="Enviar", command=self.enviar_datos)
        self.boton_env.grid(row=6, column=0, columnspan=2, pady=10)

        self.listbox1 = tkin.Listbox(dea)
        self.listbox1.grid(column=0, row=4, columnspan=2)
        self.listbox1.insert(0, "Hola")
        self.listbox1.insert(1, "¿Qué")
        self.listbox1.insert(2, "haces?")

        self.label1 = tkin.Label(self.dea, text="Recuperar")
        self.label1.grid(row=5, column=0, columnspan=2, pady=5)
        
        self.boton_recuperar = tkin.Button(self.dea, text=":v", command=self.recuperar)
        self.boton_recuperar.grid(row=5, column=1, pady=5)



        self.listbox2 = tkin.Listbox(dea, selectmode=tkin.MULTIPLE)
        self.listbox2.grid(column=2, row=4, columnspan=2)
        self.listbox2.insert(0, "Hola")
        self.listbox2.insert(1, "¿Qué")
        self.listbox2.insert(2, "haces?")

        self.label2 = tkin.Label(self.dea, text="Recuperar")
        self.label2.grid(row=5, column=3, columnspan=2, pady=5)
        
        self.boton2_recuperar = tkin.Button(self.dea, text=":v 2", command=self.recuperar2)
        self.boton2_recuperar.grid(row=5, column=2, pady=5)
    def recuperar2(self):
        if len(self.listbox2.curselection()) != 0:
            lista=""
            for posicion in self.listbox2.curselection():
                lista=lista+self.listbox2.get(posicion)+"\n"
                self.label2.configure(text=lista)
        


    def recuperar(self):
        if len(self.listbox1.curselection()) != 0:
            self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))
        

    def enviar_datos(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        genero = self.genero.get()

        # Y acá llega la ventana que va a salir cuando envías los datos  
        messagebox.showinfo("Info", f"Nombre: {nombre}\nEdad: {edad}\nGénero: {genero}")

# Ejecutor
dea = tkin.Tk()
Apa = app(dea)
dea.mainloop()
