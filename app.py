import tkinter as tk
from tkinter import filedialog as fd
import os
from finite_automata import NFA, DFA


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button0 = tk.Button(
            self.frame, text='Import', width=25, command=self.ask_directory_for_conversion)
        self.button0.pack()
        self.button1 = tk.Button(
            self.frame, text='Convert', width=25, command=self.conversion)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def ask_directory_for_conversion(self):
        self.file_path = fd.askopenfilename()

    def conversion(self):
        file = open(self.file_path, 'r')
        self.lines = file.readlines()
        file.close()
        self.nfa = NFA(self.lines)
        self.dfa = DFA()
        self.dfa.convert_from_nfa(self.nfa)
        self.dfa.print()


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(
            self.frame, text='Back', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
