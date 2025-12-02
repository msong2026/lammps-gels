import numpy as np
import matplotlib.pyplot as plt

filename = "morse_yukawa.txt"

# Load the data, skipping header lines if present
# Many pair_write files have a header of 3–4 lines, adjust skiprows accordingly
data = np.loadtxt(filename, skiprows=6, usecols=(1,2,3))

r = data[:,0]
energy = data[:,1]
force = data[:,2]

# Plot potential energy vs distance
plt.figure(figsize=(7,5))
plt.plot(r, energy, label="type 1 & type 1", color="blue")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)

plt.xlabel("Distance r")
plt.ylabel("Potential Energy")
plt.legend()
plt.tight_layout()
plt.savefig("totalpotential.png")