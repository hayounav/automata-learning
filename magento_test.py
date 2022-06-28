from automata.fa.dfa import DFA

M1 = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={"L1", "L2", "A", "C"},
    transitions={
        '0': {'L1': '1', 'L2': '0', 'A': '3', 'C': '0'},
        '1': {'L1': '1', 'L2': '1', 'A': '2', 'C': '1'},
        '2': {'L1': '2', 'L2': '2', 'A': '2', 'C': '2'},
        '3': {'L1': '3', 'L2': '3', 'A': '3', 'C': '3'},
    },
    initial_state='0',
    final_states={'0', '1', '2'}
)

M2 = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={"L1", "L2", "A", "C"},
    transitions={
        '0': {'L1': '0', 'L2': '1', 'A': '0', 'C': '3'},
        '1': {'L1': '1', 'L2': '1', 'A': '1', 'C': '2'},
        '2': {'L1': '2', 'L2': '2', 'A': '2', 'C': '2'},
        '3': {'L1': '3', 'L2': '3', 'A': '3', 'C': '3'},
    },
    initial_state='0',
    final_states={'0', '1', '2'}
)

M3 = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={"L1", "L2", "A", "C"},
    transitions={
        '0': {'L1': '0', 'L2': '0', 'A': '1', 'C': '3'},
        '1': {'L1': '1', 'L2': '1', 'A': '1', 'C': '2'},
        '2': {'L1': '2', 'L2': '2', 'A': '2', 'C': '0'},
        '3': {'L1': '3', 'L2': '3', 'A': '3', 'C': '3'},
    },
    initial_state='0',
    final_states={'0', '1', '2'}
)

spec = (M1 & M2) & M3

bug = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={"L1", "L2", "A", "C"},
    transitions={
        '0': {'L1': '0', 'L2': '1', 'A': '3', 'C': '0'},
        '1': {'L1': '1', 'L2': '1', 'A': '1', 'C': '2'},
        '2': {'L1': '2', 'L2': '2', 'A': '2', 'C': '2'},
        '3': {'L1': '3', 'L2': '3', 'A': '3', 'C': '3'},
    },
    initial_state='0',
    final_states={'2'}
)
