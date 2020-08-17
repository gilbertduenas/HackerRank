# Got stumped, had to google it.
def print_formatted(n):
    w = n.bit_length()

    for i in range(1, n+1):
        print(f'{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}')
