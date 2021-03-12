d = {'a': 'apple'}

def default_value():
    print(f'default_value called')
    return 'howdy'

def tryme():
    v = d.setdefault('a', default_value())
    print(f'{v}')

tryme()

value = []
b = d.setdefault('b', value)
c = d.setdefault('c', value)
value.append('yep')
assert value is b
assert value is c

s = 'howdy'
print(f'{s!r}')
print(f'{s}')

a = None
if not a:
    print('huh?')