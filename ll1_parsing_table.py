terminals = ['$', 'a', 'b', 'c', 'p'] # put terminals
non_terminals = ['A', 'B', 'C', 'D'] # put non_terminals
productions_dict = {'S' : ['A', 'BC'], 'A' : ['a', '#']} # put all the rules in this manner.
FOLLOW = {'S' : {'$', ''}}  # add Follow
def first(string):
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]
        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}
    elif string=='' or string=='#':
        first_ = {'#'}
    else:
        first_2 = first(string[0])
        if '#' in first_2:
            i = 1
            while '#' in first_2:
                first_ = first_ | (first_2 - {'#'})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'#'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'#'}
                i += 1
        else:
            first_ = first_ | first_2

    return  first_


def create_ll1_table():
    ll1_table = {}
    for non_terminal in non_terminals:
        ll1_table[non_terminal] = {}
        for terminal in terminals:
            ll1_table[non_terminal][terminal] = []

    for non_terminal, productions in productions_dict.items():
        for production in productions:
            first_set = first(production)
            for terminal in first_set:
                if terminal != '#':
                    ll1_table[non_terminal][terminal].append(production)
            if '#' in first_set:
                for terminal in FOLLOW[non_terminal]:
                    ll1_table[non_terminal][terminal].append(production)
            if '#' in first_set and '$' in FOLLOW[non_terminal]:
                ll1_table[non_terminal]['$'].append(production)
    return ll1_table

def print_ll1_table(ll1_table):
    print("\nLL(1) Parsing Table:")
    print("{: ^20} | {: ^80}".format('Non Terminal', 'Production Rule'))
    print('-' * 180)
    print("{: ^20} |".format(''), end='')
    for terminal in terminals + ['$']:
        print("{: ^20}|".format(terminal), end='')
    print()
    print('-' * 180)

    for non_terminal, row in ll1_table.items():
        print("{: ^20} |".format(non_terminal), end='')
        for terminal in terminals + ['$']:
            if ll1_table[non_terminal][terminal]:
                production_rules = ', '.join(ll1_table[non_terminal][terminal])
                print("{: ^20}|".format(production_rules), end='')
            else:
                print("{: ^20}|".format(''), end='')
        print()

ll1_table = create_ll1_table()
print_ll1_table(ll1_table)