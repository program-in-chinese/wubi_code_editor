import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        图片1 = tk.PhotoImage(file="images/test1.png")
        self.图片显示1 = tk.Label(self, image=图片1) #side="top"
        self.图片显示1.image = 图片1
        self.图片显示1.pack()

        图片2 = tk.PhotoImage(file="images/test2.png")
        self.图片显示2 = tk.Label(self, image=图片2) #side="top"
        self.图片显示2.image = 图片2
        self.图片显示2.pack()

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

