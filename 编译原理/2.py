'''

S → aU | bV    
U → bV | aQ  
V → aU |bQ   
Q → aQ | bQ |e

'''

dists = {
    ('S', 'a'): 'U',
    ('S', 'b'): 'V',
    ('V', 'a'): 'U',
    ('V', 'b'): 'Q',
    ('U', 'a'): 'Q',
    ('U', 'b'): 'V',
    ('Q', 'a'): 'Q',
    ('Q', 'b'): 'Q',
    ('Q',''): 'e',
}

def main():
    str = 'ab'
    masterctrl(str)


def error():
    print('Error')
    exit()


def masterctrl(str):
    stack = []
    stack1 = []
    for x in (str):
        stack.append(x)

    c = dists[('S', stack[0])]

    if c == 'Q':
        error()

    d = len(stack)

    d = d - 1

    i = 1

    while d != 0:
        c = dists[(c,stack[i])]
        i = i + 1
        d = d - 1

    return c
    if c != 'Q':
        print('不符合!')

    else:
        print('符合!')

# if __name__ == '__main__':



