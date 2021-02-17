#%%
# Merge the Tools!
def merge_the_tools(string,k):
    final = ''
    for i in range(0,len(string),k):
        add_to_map = []
        for j in string[i:i+k]:
            if j not in add_to_map:
                add_to_map.append(j)
                final += j
        final += '\n'
    return final

# Running some tests...
print(merge_the_tools('AABCAAADA',3) == 'AB\nCA\nAD\n')
print(merge_the_tools('AAABCADDE',3) == 'A\nBCA\nDE\n')
