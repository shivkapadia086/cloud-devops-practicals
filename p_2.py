# Right-Aligned Inverted Pyramid

rows = 5

for i in range(rows, 0, -1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    
    # Print stars
    for j in range(i):
        print("* ", end="")
    
    print()
    
# Alphabet Triangle Shape

rows = 5

for i in range(1, rows + 1):
    
    # spaces for triangle shape
    print(" " * (rows - i), end="")
    
    # alphabets
    for j in range(i):
        print(chr(65 + j), end=" ")
        
    print()