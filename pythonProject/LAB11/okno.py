# -*- coding: utf-8 -*-

from tkinter import BOTH, Tk, W, E, N, S, Canvas, NW, messagebox
from tkinter.ttk import Frame, Style, Label, Entry, Button, Combobox

class Okno(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.inicializuj()

    def inicializuj(self):
        self.parent.title("PiSoft")
        self.style = Style()
        self.style.theme_use("winnative")
        self.pack(fill = BOTH, expand = 1)


def main():
    gui = Tk()
    gui.geometry("1000x700")
    app = Okno(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()