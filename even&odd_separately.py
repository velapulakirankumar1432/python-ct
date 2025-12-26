s = [1, 34, 5, 23, 56, 0, 1, 2, 7]
even = []
odd = []

for num in s:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)
