import tkinter as tkin  #Se usara el ".tkin" en vez de usar el "tk" en todo el codigo

from tkinter import messagebox #-> Se importa la ventana al momento de enviar el form 
class app:
    def __init__(self, dea):
        self.dea=dea                #dea = formulario 
        self.dea.title("ya sature >:v")

        #Imprime texto nombre
        self.label_nombre= tkin.Label(dea, text="Nombre")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        #Abre la posibilidad de poner el nombre en Texto abierto
        self.entry_nombre=tkin.Entry(dea)
        self.entry_nombre.grid(row=0, column=1, padx=10,pady=10)

        #Imprime texto edad
        self.label_edad=tkin.Label(dea, text="Cual es tu edad?")
        self.label_edad.grid(row=1,column=0, padx=10, pady=10)

        #Se abre la entrada para poner edad
        self.entry_edad=tkin.Entry(dea)
        self.entry_edad.grid(row=1, column=1, padx=10, pady=10)

        self.label_preguntita=tkin.Label(dea,text="Que genero sos?")
        self.label_preguntita.grid(row=2,column=0,padx=10, pady=10)

        #StringVar gestiona y sincroniza valores de texto en Tkinter
        self.genero=tkin.StringVar(value="Non specificied:vvvvv")
        
        #Opciones de los generos a elegir
        self.radio_masculino = tkin.Radiobutton(dea, text="Masculino", variable=self.genero, value="Masculino")
        self.radio_masculino.grid(row=4, column=0, padx=10, pady=5)

        self.radio_femenino=tkin.Radiobutton (dea, text="Femenino", variable=self.genero, value="Femenino")
        self.radio_femenino.grid(row=4, column=2, padx=10, pady=5)
        

        #Boron para enviar el formulario 
        self.boton_env=tkin.Button(dea, text="Enviar", command=self.enviar_datos)
        self.boton_env.grid(row=6, column=0, columnspan=3, pady=10)


    #Al momento de enviar rellenar el formulario y enviar, este obtiene los datos
    def enviar_datos(self):
            nombre= self.entry_nombre.get()
            edad= self.entry_nombre.get()
            genero=self.genero.get()
    
    #Y acá llega la ventana que va a salir cuando envias los datos  
            messagebox.showinfo("Info", f"Nombre: {nombre}\nEdad: {edad}\nGenero: {genero}")


#Ejecutor :v
dea=tkin.Tk() 
Apa=app(dea)
dea.mainloop()