#%%
# The Minion Game
def minion_game(string):
    VOWELS = 'AEIOU'
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        if string[i] in VOWELS:
            kevin += len(string)-i
        else:
            stuart += len(string)-i
    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

print(minion_game('BANANA'))
# print(minion_game('BANANA') == 'Stuart 12')