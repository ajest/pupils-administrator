import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("Pupils Administrator")

        self.initialButton = []

        self.pack()
        self.set_initial_button()

    def set_initial_button(self):
        self.initialButton = tk.Button(self, text='Iniciar', command=self.start_app)
        self.initialButton.pack(side="top")

    def start_app(self):
        print("Application started")


root = tk.Tk()
app = Application(master=root)
app.mainloop()