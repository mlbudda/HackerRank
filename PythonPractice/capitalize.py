#%%
# Capitalize!
def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s

# Running some tests..
print(solve('hello world') == 'Hello World')
print(solve('hello   world  lol') == 'Hello   World  Lol')
print(solve('1 w 2 r 3g') == '1 W 2 R 3g')
print(solve('1 2 2 3 4 5 6 7 8  9') == '1 2 2 3 4 5 6 7 8  9')
print(solve('132 456 Wq  m e') == '132 456 Wq  M E')
