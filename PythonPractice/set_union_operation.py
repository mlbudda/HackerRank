# Set .union() Operation

n = int(input())
s1 = set(map(int, input().split()))

m = int(input())
s2 = set(map(int, input().split()))

result = len(s1 | s2)
print(result)