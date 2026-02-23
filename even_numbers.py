even = []

for i in range(1, 51):
    if i % 2 == 0:
        even.append(i)

print("Even Numbers:", even)
print("Three Minimum:", even[:3])
print("Three Maximum:", even[-3:])
print("Average:", sum(even) / len(even))
