import matplotlib.pyplot as plt

feldliste = []
graincount = 1
totalgrains = 0
rowS = "A B C D E F G H".split()
columnS = "1 2 3 4 5 6 7 8".split()

print("Grains on each field on the chessboard:")

for column in columnS:
    Ccolumn = column
    for row in rowS:
        Crow = row
        totalgrains += graincount
        feldliste.append(graincount)
        print(F"{Crow}{Ccolumn}: {graincount:>25,}")
        graincount *= 2
    print()  
  
print(f"number of total grains: {totalgrains:,}")

plt.plot(feldliste)
plt.show()