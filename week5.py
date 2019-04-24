sum = 0
i = 1523
while i <= 10503:
    sum = sum + i
    i = i + 2
print(sum)

sum = 0
for i in range(1523, 10503 + 1, 2):
    sum = sum + i

print(sum)

def increment_items(L, inc):
    i = 0
    while i < len(L):
        L[i] = L[i] + inc
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
