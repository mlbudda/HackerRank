# %%
# Alphabet Rangoli
import string
def print_rangoli(size):
    all_strings = string.ascii_lowercase
    temp = []
    for i in range(size):
        s = "-".join(all_strings[i:size])
        temp.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(temp[:0:-1]+temp))
    

print_rangoli(3)
# print_rangoli(5)
# print_rangoli(10)