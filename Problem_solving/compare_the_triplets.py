# %%
# Compare the Triplets

def compareTriplets(a, b):
    """ Determines their respective comparison points """
    alice = 0;
    bob = 0;
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice,bob

# Running some tests..
print(compareTriplets([5,6,7], [3,6,10]) == (1, 1))
