import numpy as np
import matplotlib.pyplot as plt

def getdata(types):
    type1, type2 = types
    filename = "morse_yukawa_" + str(type1) + str(type2) + ".txt"
    data = np.loadtxt(filename, skiprows=6, usecols=(1,2,3))
    return data

pairs = [(1,1), (1,2), (2,2)]

plt.style.use("seaborn-v0_8-poster")

# Plot potential energy vs distance
plt.figure(figsize=(7,5))
for p in pairs:
    data = getdata(p)
    r = data[:,0]
    energy = data[:,1]
    force = data[:,2]
    plt.plot(r, energy, label=f"type {p[0]} & type {p[1]}")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.ylim([None,200])

plt.xlabel("Distance r")
plt.ylabel("Morse and Yukawa potentials")
plt.legend()
plt.tight_layout()
plt.savefig("totalpotential.png")