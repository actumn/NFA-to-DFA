def final_states(line):
    final_states_line = list(map(int, line.split(' ')))
    return final_states_line[0], final_states_line[1:]


class NFA:
    def __init__(self, lines):
        self.num_states = int(lines[0])
        self.states = list(range(self.num_states))
        self.symbols = list(lines[1].strip())
        self.num_accepting_states, self.accepting_states = final_states(lines[2])
        self.start_state = int(lines[3])

        self.transition_functions = []
        for line in lines[4:]:
            transition_func_line = line.split(' ')

            starting_state = int(transition_func_line[0])
            transition_symbol = transition_func_line[1]
            ending_state = int(transition_func_line[2])

            self.transition_functions.append((starting_state, transition_symbol, ending_state))

    @property
    def transition_dict(self):
        result = {}
        for transition in self.transition_functions:
            starting_state = transition[0]
            transition_symbol = transition[1]
            ending_state = transition[2]

            if (starting_state, transition_symbol) in result:
                result[(starting_state, transition_symbol)].append(ending_state)
            else:
                result[(starting_state, transition_symbol)] = [ending_state]

        return result


class DFA:
    def __init__(self):
        self.num_states = 0
        self.symbols = []
        self.num_accepting_states = 0
        self.accepting_states = []
        self.start_state = 0
        self.transition_functions = []
        self.q = []

    def convert_from_nfa(self, nfa):
        self.symbols = nfa.symbols
        self.start_state = nfa.start_state

        # Combine NFA transitions
        nfa_transition_dict = nfa.transition_dict

        # Initial state q0
        self.q.append((self.start_state,))

        # Convert NFA transitions to DFA transitions
        dfa_transition_dict = {}
        for dfa_state in self.q:
            for symbol in nfa.symbols:
                if len(dfa_state) == 1 and (dfa_state[0], symbol) in nfa_transition_dict:
                    dfa_transition_dict[(dfa_state, symbol)] = nfa_transition_dict[(dfa_state[0], symbol)]

                    if tuple(dfa_transition_dict[(dfa_state, symbol)]) not in self.q:
                        self.q.append(tuple(dfa_transition_dict[(dfa_state, symbol)]))
                else:
                    destinations = []
                    final_destination = []

                    for nfa_state in dfa_state:
                        if (nfa_state, symbol) in nfa_transition_dict and \
                                nfa_transition_dict[(nfa_state, symbol)] not in destinations:
                            destinations.append(nfa_transition_dict[(nfa_state, symbol)])

                    if not destinations:
                        final_destination.append(None)
                    else:
                        for destination in destinations:
                            for value in destination:
                                if value not in final_destination:
                                    final_destination.append(value)

                    dfa_transition_dict[(dfa_state, symbol)] = final_destination

                    if tuple(final_destination) not in self.q:
                        self.q.append(tuple(final_destination))

        # Convert NFA states to DFA states            
        for key in dfa_transition_dict:
            self.transition_functions.append(
                (self.q.index(tuple(key[0])), key[1], self.q.index(tuple(dfa_transition_dict[key]))))

        for q_state in self.q:
            for nfa_accepting_state in nfa.accepting_states:
                if nfa_accepting_state in q_state:
                    self.accepting_states.append(self.q.index(q_state))
                    self.num_accepting_states += 1

    def print(self):
        print(len(self.q))
        print(''.join(self.symbols))
        print(str(self.num_accepting_states) + ' ' + 
              ' '.join(str(accepting_state) for accepting_state in self.accepting_states))
        print(self.start_state)

        for transition in sorted(self.transition_functions):
            print(' '.join(str(value) for value in transition))
