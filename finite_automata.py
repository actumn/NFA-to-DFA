class NFA:
    def __init__(self, lines):
        self.num_states = int(lines[0])
        self.states = list(range(self.num_states))
        self.symbols = list(lines[1].strip())
        final_states_line = list(map(int, lines[2].split(' ')))
        self.num_final_states, self.final_states = final_states_line[0], final_states_line[1:]
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


def lambda_closure(nfa_transition_dict, dfa_state):
    result = list(dfa_state)

    for nfa_state in result:
        if (nfa_state, '@') in nfa_transition_dict:
            value_list = nfa_transition_dict[(nfa_state, '@')]

            for value in value_list:
                if value not in result:
                    result.append(value)

    return tuple(result)


def extract_destination(nfa_transition_dict, dfa_state, symbol):
    destinations = []

    for nfa_state in dfa_state:
        if (nfa_state, symbol) in nfa_transition_dict and \
                nfa_transition_dict[(nfa_state, symbol)] not in destinations:
            destinations.append(nfa_transition_dict[(nfa_state, symbol)])

    return destinations


def destinations_to_final(destinations):
    if not destinations:
        return None

    final = []
    for destination in destinations:
        for value in destination:
            if value not in final:
                final.append(value)

    return final


class DFA:
    def __init__(self):
        self.symbols = []
        self.start_state = 0
        self.q = []
        self.transition_functions = []
        self.num_final_states = 0
        self.final_states = []

    def convert_from_nfa(self, nfa):
        self.symbols = nfa.symbols

        # Combine NFA transitions
        nfa_transition_dict = nfa.transition_dict

        # Initial state q0 = lambda_closure((0,))
        self.start_state = 0
        self.q.append(lambda_closure(nfa_transition_dict, (nfa.start_state, )))

        # Convert NFA transitions to DFA transitions
        dfa_transition_dict = {}
        for dfa_state in self.q:
            for symbol in nfa.symbols:
                destinations = extract_destination(nfa_transition_dict, dfa_state, symbol)
                final_destination = destinations_to_final(destinations)
                if final_destination is None:
                    continue

                final_destination = lambda_closure(nfa_transition_dict, final_destination)

                dfa_transition_dict[(dfa_state, symbol)] = final_destination

                if tuple(final_destination) not in self.q:
                    self.q.append(tuple(final_destination))

        # Convert NFA states to DFA states
        for key, value in dfa_transition_dict.items():
            self.transition_functions.append((self.q.index(key[0]), key[1], self.q.index(value)))

        for q_state in self.q:
            for nfa_final_state in nfa.final_states:
                if nfa_final_state in q_state:
                    self.final_states.append(self.q.index(q_state))
                    self.num_final_states += 1

    def print(self):
        print(len(self.q))
        print(''.join(self.symbols))
        print(str(self.num_final_states) + ' ' + ' '.join(str(final_state) for final_state in self.final_states))
        print(self.start_state)

        for transition in sorted(self.transition_functions):
            print(' '.join(str(value) for value in transition))
