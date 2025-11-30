import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

volfrac = [10,20,40]

def plotpng(quantity,ylabel,log,types):
    plt.style.use("seaborn-v0_8-poster")
    fig,ax = plt.subplots(1,2,figsize=(14,5))
    for i,vf in enumerate(volfrac):
        file = quantity + "-b" + str(vf) + ".txt"
        columns = ["ac"+str(c) for c in types]
        data = pd.read_csv(file,  sep=" ",skiprows=2, names=["time",*columns])
        for j,t in enumerate(types):
            ax[j].plot(data["time"][:100],data[columns[j]][:100],label=f"{vf} vol%")
    for j,t in enumerate(types):
        ax[j].set_ylim([0,None])
        ax[j].set_xlabel("Time")
        ax[j].set_ylabel(ylabel)
        ax[j].legend()
        ax[j].set_title("For atoms of type " + str(t) + r" ($D=$" + str(diams[j]) + ")")
        if log:
            ax[j].set_xscale("log")
            ax[j].set_yscale("log")
    fig.tight_layout()
    fig.savefig(quantity+("loglog" if log else "")+"-b.png")

types = [1,2]
diams = [1.0, 0.5]

plotpng("avgcoord", "Average coordination number", False, types)