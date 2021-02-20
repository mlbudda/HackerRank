#%%
# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
m = int(input())
for _ in range(int(m)):
    temp = input().split()
    if temp[0].startswith('remove'):
        s.remove(int(temp[1]))
    elif temp[0].startswith('discard'):
        s.discard(int(temp[1]))
    elif temp[0].startswith('pop'):
        s.pop()

print(sum(s))