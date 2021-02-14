#%%
n, m = map(int, input().split())
a = '.|.'
b = '-'
c = 'WELCOME'

for i in range(1,n,2):
    print((a*i).center(m,b))
print(c.center(m,b))
for i in range(n-2,0,-2):
    print((a*i).center(m,b))

