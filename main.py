from finite_automata import NFA, DFA


filename = input('Enter the name of the NFA file: ')

file = open(filename, 'r')
lines = file.readlines()
file.close()


nfa = NFA(lines)

dfa = DFA()
dfa.convert_from_nfa(nfa)

dfa.print()
