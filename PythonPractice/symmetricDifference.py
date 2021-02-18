#%%
# Symmetric Difference
# Get input
a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
# prepare empty sets
b_s = set()
d_s = set()
# convert each to integer (required for sorting later)
for i in b:
    b_s.add(int(i))
for i in d:
    d_s.add(int(i))
# merge two sets with symetric_difference 
result = b_s ^ d_s
# print out
for i in sorted(result):
    print(i)



