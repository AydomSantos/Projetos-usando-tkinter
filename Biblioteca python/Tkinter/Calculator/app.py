from tkinter import Tk , Entry , Button , StringVar

class Calculator:
    def __init__(self, main):
        main.title('Calculator')
        main.geometry('350x427+0+0')
        main.config(bg='gray')
        main.resizable(False, False)
        

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable= self.equation).place(x=0, y=0)

        # Botões da calculadora
        Button(width=8, bg="#fff", text="1", font=('flat'), height=4, command=lambda: self.show("1"),).place(x=0, y=50)
        Button(width=8, bg="#fff", text="2", font=('flat'), height=4, command=lambda: self.show("2")).place(x=90, y=50)
        Button(width=8, bg="#fff", text="3", font=('flat'), height=4, command=lambda: self.show("3")).place(x=180, y=50)
        Button(width=8, bg="#fff", text="+", font=('flat'), height=4, command=lambda: self.show("+")).place(x=270, y=50)
        Button(width=8, bg="#fff", text="4", font=('flat'), height=4, command=lambda: self.show("4")).place(x=0, y=150)
        Button(width=8, bg="#fff", text="5", font=('flat'), height=4, command=lambda: self.show("5")).place(x=90, y=150)
        Button(width=8, bg="#fff", text="6", font=('flat'), height=4, command=lambda: self.show("6")).place(x=180, y=150)
        Button(width=8, bg="#fff", text="-", font=('flat'), height=4, command=lambda: self.show("-")).place(x=270, y=150)
        Button(width=8, bg="#fff", text="7", font=('flat'), height=4, command=lambda: self.show("7")).place(x=0, y=250)
        Button(width=8, bg="#fff", text="8", font=('flat'), height=4, command=lambda: self.show("8")).place(x=90, y=250)
        Button(width=8, bg="#fff", text="9", font=('flat'), height=4, command=lambda: self.show("9")).place(x=180, y=250)
        Button(width=8, bg="#fff", text="*", font=('flat'), height=4, command=lambda: self.show("*")).place(x=270, y=250)
        Button(width=8, bg="#fff", text="C", font=('flat'), height=4, command=self.clean).place(x=0, y=350)
        Button(width=8, bg="#fff", text="0", font=('flat'), height=4, command=lambda: self.show("0")).place(x=90, y=350)
        Button(width=8, bg="#fff", text="=", font=('flat'), height=4, command=self.salve).place(x=180, y=350)
        Button(width=8, bg="#fff", text="/", font=('flat'), height=4, command=lambda: self.show("/")).place(x=270, y=350)

        
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clean(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def salve(self):
        result = eval(self.entry_value)
        self.equation.set(result) 

app = Tk()
calculator =  Calculator(app)
app.mainloop()

