# %%
# String Formatting
def print_formatted(number):
    result = ''
    for i in range(1, number+1):
        result += (f'{i}'.rjust(len(bin(number)[2:]))
        + f'{i:o}'.rjust(len(bin(number)[2:])+1)
        + (f'{i:X}').rjust(len(bin(number)[2:])+1)
        + f'{bin(i)[2:]}\n'.rjust(len(bin(number)[2:])+2))
    return print(result)

print_formatted(17)
print_formatted(2)
print_formatted(99)
print_formatted(63)
