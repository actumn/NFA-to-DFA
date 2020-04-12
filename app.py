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
        # DOES NOT WORK?
        # self.button2 = tk.Button(
        #     self.frame, text='Save', width=25, command=self.conversion)
        # self.button2.pack()
        self.frame.pack()

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

    # DOES NOT WORK?
    # def save_button(self):
    #     file = open(f"{self.file_path}", 'w')
    #     file.write(len(self.dfa.q))
    #     file.write(''.join(self.dfa.symbols))
    #     file.write(str(self.dfa.num_final_states) + ' ' + ' '.join(str(final_state) for final_state in self.dfa.final_states))
    #     file.write(self.dfa.start_state)
    #     file.close()

def main():
    root = tk.Tk()
    Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
