from tkinter import *
from tkinter.filedialog import askopenfilename

from driver import import_file


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.init_ui()

    @staticmethod
    def display_data(email):
        root = Tk()
        root.geometry("1366x768+700+700")
        text = Text(root)
        text.config(width=240, height=72)
        text.insert(END, str(email))
        text.pack()
        root.mainloop()

    def open_file(self):
        filename = askopenfilename()
        self.display_data(import_file(filename))

    def init_ui(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        browse_btn = Button(self, text="Browse Files", command=self.open_file)
        browse_btn.place(x=45, y=10)


