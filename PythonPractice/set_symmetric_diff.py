#%%
# Set .symmetric_difference() Operation
x = int(input())
iter_one = set(map(int, input().split()))
y = int(input())
iter_two = set(map(int, input().split()))

print(len(iter_one ^ iter_two))

