from finite_automata import NFA, DFA

filename = input('Enter the name of the NFA file\nFor example "./tests/test2.txt".\nYou might need to format your input,\ndepending on the location of your file.\n\nFilename:')
try:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    dfa = DFA()
    dfa.convert_from_nfa(NFA(lines))
    dfa.print()
except Exception as e:
    print(e)