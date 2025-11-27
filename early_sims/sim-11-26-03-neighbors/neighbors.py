import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotpng(quantity,ylabel,log,cutoffs):
    file = quantity + ".txt"
    columns = ["ac"+str(c) for c in cutoffs]
    data = pd.read_csv(file,  sep=" ",skiprows=2, names=["time",*columns])
    plt.figure()
    for i,cutoff in enumerate(cutoffs):
        plt.plot(data["time"],data[columns[i]],lw=1,label=f"cutoff={cutoff}")
    plt.xlabel("Time")
    plt.ylabel(ylabel)
    if log:
        plt.xscale("log")
        plt.yscale("log")
    plt.legend()
    plt.savefig(quantity+("loglog" if log else "")+".png")
    plt.close()

cutoffs = np.arange(0.5, 1.5, 0.25)

plotpng("avgcoord", "Average coordination number", False, cutoffs)