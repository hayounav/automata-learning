from aalpy.utils import dfa_from_state_setup
from aalpy.learning_algs import run_RPNI
from aalpy.utils import save_automaton_to_file


def DfaToAalpyDFA(dfa):
    state_setup = {dfa.initial_state: (
        dfa.initial_state in dfa.final_states, {x: dfa.transitions[dfa.initial_state][x] for x in dfa.input_symbols})}
    for s in dfa.states:
        if s == dfa.initial_state:
            continue
        state_setup[s] = (s in dfa.final_states, {x: dfa.transitions[s][x] for x in dfa.input_symbols})

    return dfa_from_state_setup(state_setup)


#from aabb_test import *
from magento_test import *

real_system = spec & bug

real_system_dfa = DfaToAalpyDFA(real_system)
bug_dfa = DfaToAalpyDFA(bug)
spec_dfa = DfaToAalpyDFA(spec)

from random import Random
random = Random(42)

# num_sequences = 250
# data = []
# for _ in range(num_sequences):
#     seq_len = random.randint(1, 20)
#     random_seq = random.choices(real_system_dfa.get_input_alphabet(), k=seq_len)
#     spec_output = spec_dfa.compute_output_seq(spec_dfa.initial_state, random_seq)[-1]
#     if spec_output:
#         output = real_system_dfa.compute_output_seq(real_system_dfa.initial_state, random_seq)[-1]
#         data.append((random_seq, output))

from itertools import product
data = []
possible_words = list(product(real_system_dfa.get_input_alphabet(), repeat=5))+list(product(real_system_dfa.get_input_alphabet(), repeat=4))
for s in possible_words:
    spec_output = spec_dfa.compute_output_seq(spec_dfa.initial_state, s)[-1]
    if spec_output:
        output = real_system_dfa.compute_output_seq(real_system_dfa.initial_state, s)[-1]
        data.append((s, output))


model = run_RPNI(data, automaton_type='dfa')
vis = save_automaton_to_file(model, file_type="string")
print(vis)

brkpnt = 1
