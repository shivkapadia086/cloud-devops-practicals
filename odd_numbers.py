odd = []

for i in range(1, 101):
    if i % 2 != 0:
        odd.append(i)

print("Odd Numbers:", odd)
print("Minimum:", min(odd))
print("Maximum:", max(odd))
print("Sum:", sum(odd))