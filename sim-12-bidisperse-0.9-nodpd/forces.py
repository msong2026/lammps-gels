# Extracting local force information from pvf.txt

import pandas as pd
import numpy as np
import csv

def getforces(num_atoms,atomid,dumps,totalsteps):
    print("\nAtom ID: " + str(atomid))
    t_int = totalsteps/dumps # 1000000/100 = 10000
    lines = (num_atoms+9)*1000
    timesteps = np.arange(t_int, totalsteps+t_int, t_int)

    with open(f"forces_ID{atomid}.csv", "w") as outputfile:
        csvwriter = csv.writer(outputfile)
        csvwriter.writerow(["time", "fx", "fy", "fz"])
        for i in range(dumps):
            current_row = i*1000 + (i+1)*9        # 0 indexing
            if current_row == lines:
                break
            block = range(current_row, current_row+1000)
            print(block)
            toskip = []
            for line in range(lines):
                if line not in block:
                    toskip.append(line)
            irrelevant = np.array(toskip)
            data = pd.read_csv("pvf.txt",skiprows=irrelevant,delimiter=" ",
                               names=["id","x","y","z",
                                      "vx", "vy", "vz",
                                      "fx", "fy", "fz"])
            print(data["id"])
            index = np.where(data["id"]==atomid)[0][0]
            fx = data["fx"][index]
            fy = data["fy"][index]
            fz = data["fz"][index]

            csvwriter.writerow([timesteps[i], fx, fy, fz])

    return "done"

selection = [73, 86, 90, 99, 101, 102, 117, 121]
for id in selection:
    getforces(1000, id, 100, 10**6)