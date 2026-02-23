# Right Half Pyramid Pattern

rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("1 2 3 4 5")
print("6 7 8 9")
print("1 2 3")
print("4 5")
print("6")