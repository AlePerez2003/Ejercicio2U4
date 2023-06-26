from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana: None
    __ingresado: None
    __iva: None
    __total: None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x250')
        self.__ventana.title('Calculadora IPC')
        mainframe = ttk.Frame(self.__ventana, padding = "3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__ingresado = StringVar()
        self.__iva = StringVar()
        self.__total = StringVar()
        self.valor=IntVar()

        ttk.Label (mainframe, text="Cálculo de IVA", bg='ligth sky blue').grid(column=0,row=0,columnspan=4,sticky=(W, E))
        #tkinter.Label(self,text="Calculo de IVA",bg='light sky blue').grid(column=0,row=0,columnspan=4,sticky=('nsew'))

        ttk.Label(mainframe, text="Precio sin IVA").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="IVA 21%").grid(column=2, row=2, sticky=W)
        ttk.Label(mainframe, text="IVA 10.5%").grid(column=2, row=3, sticky=W)
        ttk.Label(mainframe, text = "IVA").grid(column=1, row=4, sticky=W)
        ttk.Label(mainframe, text="Precio con IVA").grid(column=1, row=5, sticky=W)
        self.ingresadoEntry = ttk.Entry(mainframe, width=7, textvariable=self.__vCant)
        self.ingresadoEntry.grid(column=2, row=2, sticky=(W, E))


        '''ttk.Label(mainframe, textvariable=str(self.__porcentaje)).grid(column=2, row=6, sticky=(W, E))
        ttk.Button(mainframe, text="Calcular IPC", command=self.calcular).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=4, row=5, sticky=W)
        ttk.Label(mainframe, text="IPC %").grid(column=1, row=6, sticky=W)
        ttk.Label(mainframe, text="%").grid(column=3, row=6, sticky=W)
'''

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.vCantEntry.focus()
        self.__ventana.mainloop()
    
    def calcular(self):
        try:
            cantV = int(self.vCantEntry.get())
            cantA = int(self.aCantEntry.get())
            cantE = int(self.eCantEntry.get())
            baseV = int(self.vPABEntry.get())
            baseA = int(self.aPABEntry.get())
            baseE = int(self.ePABEntry.get())
            actualV = int(self.vPAAEntry.get())
            actualA = int(self.aPAAEntry.get())
            actualE = int(self.ePAAEntry.get())
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        
        costo_base = (cantA * baseA) + (cantV * baseV) + (cantE * baseE)
        costo_actual = (cantA * actualA) + (cantV * actualV) + (cantE * actualE)

        ipc = (costo_actual / costo_base)
        ipc = ipc - int(ipc)
        ipc = ipc * 100
        self.__porcentaje.set(round(ipc, 2))

def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()