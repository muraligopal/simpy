steps = []
pote = []
potf = []

f = open("OSZICAR", "r")

for i in f:
    if "=" in i:
        tokens = i.strip().split()
        steps.append(int(tokens[0]))
        pote.append(float(tokens[8]))

f.close()

import matplotlib.pyplot as plt

plt.plot(pote)
plt.show()