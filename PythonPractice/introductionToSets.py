#%%
# Introduction to Sets
def average(array):
    arr_unique = set(array)
    temp = 0
    for i in arr_unique:
        temp += i
    return temp/len(arr_unique)


print(average([161,182,161,154,176,170,167,171,170,174]) == 169.375)