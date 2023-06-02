n = int(input())
sum = (n * (n-1)) / 2
print(sum)

# O(1)

# or
sum = 0
for i in range(n):
    sum += i
print(sum)

# O(n)