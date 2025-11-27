# Writing a LAMMPS input file for a system with Morse interaction and uniform particle size

import numpy as np
from scipy.stats import norm
import sys

from numpy.random import Generator, PCG64
rng = Generator(PCG64())


def main(epsilon: float = 5, gamma0: float = 5, number_density: float = 0.2, rho: float = 33,
         dratio: float = 0.5, num_particles: int = 1000):
    """Main function
    :param epsilon: Morse potential well depth.
    :param gamma0: Dissipative coefficient between particles of type 1.
    :param number_density: Density of particles.
    :param rho: Morse interaction distance.
    :param dratio: Ratio of particle diameters; 1 if monodisperse.
    :param num_particles: Number of particles in simulation box.
    """

    print("num_particles:", num_particles)
    
    density = 2.35 # mass per volume of each particle

    r_cut_coeff = 2.0               # Morse cutoff
    # If turned on, "dpd_thermostat" will add "Morse" to the interaction potential to allow use
    # of the hybrid/overlay style
    dpd_thermostat = True

    box_volume = num_particles/number_density
    side_len = box_volume ** (1/3)
    
    d1 = 1.0
    
    if dratio < 1.0 and dratio > 0:
        num_types = 2
        print("bidisperse")

        # Set up the particle diameters
        d2 = d1 * dratio
        diameters = [d1, d2]

        # Mass fractions
        mf1 = 0.5
        mf2 = 0.5

        # Number fractions (assuming equal density)
        vratio = dratio**3
        denominator = mf1*vratio + mf2
        p1 = mf1*vratio / denominator
        p2 = mf2 / denominator
        # Assign a type to each particle; probability of type 1 is p1, etc.
        particle_species = rng.choice([1,2], num_particles, p=[p1,p2])

    elif dratio == 1.0:
        num_types = 1
        print("monodisperse")

        diameters = [d1]

        particle_species = np.array([1]*num_particles)

    else:
        raise ValueError("dratio must be in the range (0,1]")

    # Create random particle coordinates
    x = np.random.uniform(0, side_len, size=num_particles)
    y = np.random.uniform(0, side_len, size=num_particles)
    z = np.random.uniform(0, side_len, size=num_particles)

    packing = 0
    for i in range(num_particles):
        packing += np.pi / 6 * (diameters[particle_species[i] - 1] ** 3) / box_volume

    print(f"* The packing fraction is {packing:.4f}")

    filename = "morse_input_phi%.4f.lmp" % packing

    with open(filename, 'w') as ouptut_file:
        # Write the LAMMPS file header
        ouptut_file.write("LAMMPS Description\n\n")
        ouptut_file.write("{} atoms\n\n".format(num_particles))

        # Write the box size
        ouptut_file.write("{} atom types\n".format(num_types))
        ouptut_file.write("0 {:.6f} xlo xhi\n"
                          "0 {:.6f} ylo yhi\n"
                          "0 {:.6f} zlo zhi\n\n".format(side_len, side_len, side_len))

        # If the hybrid/overlay command is used, need to specify the type of the potential
        if dpd_thermostat:
            keyword = " morse "
        else:
            keyword = ""

        # Specify the interaction coefficients for the Morse potential:
        # in LAMMPS's documentation they are: d0 alpha r0 cutoff
        ouptut_file.write("PairIJ Coeffs\n\n")
        for type_1 in range(num_types):
            for type_2 in range(type_1, num_types):
                diam_i = diameters[type_1]
                diam_j = diameters[type_2]
                mixed_diam = 0.5 * (diam_i + diam_j)
                ouptut_file.write(f"{type_1 + 1:d} {type_2 + 1:d}{keyword:s}{epsilon:g} {rho:g} "
                                  f"{mixed_diam:g} {r_cut_coeff * mixed_diam:g}\n")
                # Specify the interaction coefficients for dpd/tstat in a separate file
                with open("dpdcoeffs.in", "w") as coefffile:
                    coefffile.write(f"pair_coeff {type_1 + 1:d} {type_2 + 1:d} dpd/tstat {gamma0*mixed_diam/d1:g}\n")

        # Write coordinates
        ouptut_file.write("\nAtoms # sphere\n\n")
        for i in range(num_particles):
            particle_type = particle_species[i]
            ouptut_file.write(f"{i + 1:d} {particle_type:d} {diameters[particle_type-1]:g} {density:g} {x[i]:g} {y[i]:g} {z[i]:g}\n")


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 7:
        raise SyntaxError("Incorrect syntax.\nUse python gel_setup.py epsilon gamma0 number_density "
                          "rho_0 dratio num_particles")
    epsilon = float(sys.argv[1])
    gamma0 = float(sys.argv[2])
    number_density = float(sys.argv[3])
    rho_0 = float(sys.argv[4])
    dratio = float(sys.argv[5])
    num_particles = int(sys.argv[6])
    main(epsilon, gamma0, number_density, rho_0, dratio, num_particles)