import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

volfrac = [10,20,40]

def plotpng(quantity,ylabel,log,cutoffs,sc):
    plt.style.use("seaborn-v0_8-poster")
    nc = len(cutoffs)
    start = nc - sc
    fig,ax = plt.subplots(1,start,figsize=(start*5+4,5))
    for vf in volfrac:
        file = quantity + "-m" + str(vf) + ".txt"
        columns = ["ac"+str(c) for c in cutoffs]
        data = pd.read_csv(file,  sep=" ",skiprows=2, names=["time",*columns])
        for i,cutoff in enumerate(cutoffs):
            if i>=sc:
                ax[i-sc].set_title(f"cutoff={cutoff}")
                ax[i-sc].plot(data["time"][:100],data[columns[i]][:100],label=f"{vf} vol%")
    for i in range(2):
        ax[i].set_ylim([0,None])
        ax[i].set_xlabel("Time")
        ax[i].set_ylabel(ylabel)
        ax[i].legend()
        if log:
            ax[i].xscale("log")
            ax[i].yscale("log")
    fig.tight_layout()
    fig.savefig(quantity+("loglog" if log else "")+"-m.png")

cutoffs = np.arange(0.5, 1.5, 0.25)

plotpng("avgcoord", "Average coordination number", False, cutoffs, 2)