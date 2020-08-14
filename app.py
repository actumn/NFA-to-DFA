import tkinter as tk
from tkinter import filedialog as fd
import os
from finite_automata import NFA, DFA


class Demo1:
    def __init__(self, master):
        self.master = master
        self.master.title("NFA to DFA Converter")
        self.frame = tk.Frame(self.master)
        self.button0 = tk.Button(self.frame, text='Import', width=25, padx=15, pady=10, command=self.ask_directory_for_conversion)
        self.button0.pack()
        self.button1 = tk.Button(self.frame, text='Convert', width=25, padx=15, pady=10, command=self.conversion)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text='Save', width=25, padx=15, pady=10, command=lambda: self.conversion(save=1))
        self.button2.pack()
        self.frame.pack()

    def ask_directory_for_conversion(self):
        self.file_path = fd.askopenfilename()

    def conversion(self, save=0):
        file = open(self.file_path, 'r')
        self.lines = file.readlines()
        file.close()
        self.nfa = NFA(self.lines)
        self.dfa = DFA()
        self.dfa.convert_from_nfa(self.nfa)
        if not save:
            self.dfa.print()
        else:
            try:
                with open(f"{self.file_path}_output.txt", 'w') as file:
                    file.write(f'{str(len(self.dfa.q))}\n')
                    file.write(f'{"".join(self.dfa.symbols)}\n')
                    file.write(f'{str(self.dfa.num_final_states)} {" ".join(str(final_state) for final_state in self.dfa.final_states)}\n')
                    file.write(f'{str(self.dfa.start_state)}\n')
                    for transition in sorted(self.dfa.transition_functions):
                        file.write(f"{' '.join(str(value) for value in transition)}\n")
            except Exception as e:
                print(e, "You need to select a file first, if you did, check the error output.")


def main():
    root = tk.Tk()
    Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
