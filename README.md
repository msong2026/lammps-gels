# lammps-gels
This is a repository for LAMMPS simulations of percolation in monodisperse and bidisperse colloidal gels, created as part of a final project for the course PHYS 25000 Computational Physics (Autumn 2025) at the University of Chicago. The gel initialization scripts (gel_setup_bidisperse.py) are adapted from https://github.com/merrygoat/creep-sheared-gels. Scripts from https://doi.org/10.1007/s40571-023-00605-x were also referenced.

See sim-11-bidisperse-0.9 for an animation.

## Procedure for running simulations
Each folder starting with "sim" contains a single simulation and the associated post-processing files.
1. To execute the gel_setup_bidisperse.py script, run `bash setup_script.sh`, which contains the input parameters. This step produces the files morse_input_phi0.xxxx.lmp (which contains the initial particle configuration) and coeffs.in (which contains the pair interaction parameters for the Morse potential and `dpd/tstat`). The gel_setup_bidisperse.py file was modified many times throughout the project, so the number of parameters in setup_script.sh is not necessarily the same between folders. Some folders may not have any setup files because the input files from another simulation are reused.
2. To start a simulation, change the file name in submission_script.sh to match the morse_input_phi0.xxxx file, and then run `bash submission_script.sh`. The simulation will execute the contents of gel.in. At regular intervals, .dump files containing full particle configurations (viewable in OVITO) will be produced. In the newer simulations, the following will also be produced:
    - msd.txt: mean-squared displacement over time
    - pvf.txt: positions, velocities, and forces for every atom at every timestep corresponding to the dump frequency
    - com.txt: center of mass coordinates over time (used to confirm that there is no drifting)
    - avgcoord.txt: average coordination numbers, with columns organized by atom type for bidisperse setups and by neighbor cutoff for monodisperse setups
3. Various post-processing files were used to reorganize data or produce plots. These include:
    - plotdisp.py: plots the mean-squared displacement on a linear scale (msd.png) and a log-log scale (msdloglog.png)
    - neighbors.py: plots average coordination number over time (avgcoord.png)
    - forces.py: extracts the force components for individual atoms (forces_ID#.csv)
    - plotforces.py: plots force components and force magnitude for individual atoms (forces_ID#.png) and the force magnitude autocorrelation function for a selection of individual atoms (autocorrelation.png)

Note that .dump files were not uploaded for most simulations to reduce clutter. They were kept for sim-11-bidisperse-0.9, sim-11-monodisperse-0.4, and sim-11-monodisperse-0.4-np.

The numbers following monodisperse- and bidisperse- in the directory names indicate number density. Number densities were chosen to yield volume fractions of approximately 10%, 20%, and 40% for each of the setups (monodisperse and bidisperse).