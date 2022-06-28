from automata.fa.dfa import DFA

# Accepts the language "every 'a' is followed by 'b'"
spec = DFA(
    states={'0', '1', '2', '3'},
    input_symbols=set("ab"),
    transitions={
        '0': {'a': '1', 'b': '0'},
        '1': {'a': '3', 'b': '2'},
        '2': {'a': '1', 'b': '2'},
        '3': {'a': '3', 'b': '3'}
    },
    initial_state='0',
    final_states={'0', '1', '2'}
)

# Accepts the language "every b is followed by b"
bug = DFA(
    states={'0', '1', '2'},
    input_symbols=set("ab"),
    transitions={
        '0': {'a': '0', 'b': '1'},
        '1': {'a': '0', 'b': '2'},
        '2': {'a': '2', 'b': '2'}
    },
    initial_state='0',
    final_states={'2'}
)