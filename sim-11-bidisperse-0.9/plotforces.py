import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

timestep = 0.001

def plotforces(atomid):
    df = pd.read_csv(f"forces_ID{atomid}.csv")
    fig,ax = plt.subplots(1,2,figsize=(12,5))
    cs = ["x","y","z"]
    for c in cs:
        ax[0].plot(df["time"]*timestep,df["f"+c],label=f"{c}-direction")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Force")
    ax[0].legend()
    ax[0].set_title("Force components")
    
    fmag = [np.sqrt(df["fx"][i]**2 + df["fy"][i]**2 + df["fz"][i]**2) for i in range(df.shape[0])]
    ax[1].plot(df["time"]*timestep,fmag)
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Force")
    ax[1].set_ylim([0,None])
    ax[1].set_title("Force magnitude")

    fig.suptitle("Atom ID "+str(atomid))

    fig.tight_layout()
    fig.savefig(f"forces_ID{atomid}.png")

selection = [73, 86, 90, 99, 101, 102, 117, 121]
for id in selection:
    plotforces(id)