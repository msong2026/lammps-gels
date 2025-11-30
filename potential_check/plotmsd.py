import pandas as pd
import matplotlib.pyplot as plt

comps = [r"Monodisperse ($D=1$)", r"Bidisperse ($D_1=1$, $D_2=0.5$)"]
potls = ["with potentials", "without potentials"]

cb = ["m0.4", "b1.7"]
pot = ["", "np"]

def plotpng(quantity,ylabel,log):
    plt.style.use("seaborn-v0_8-poster")
    fig,ax = plt.subplots(1,2,figsize=(15,5))
    for i in range(2):
        ax[i].set_title(comps[i])
        for j,potl in enumerate(potls):
            file = quantity + "-" + cb[i] + pot[j] + ".txt"
            data = pd.read_csv(file,  sep=" ",skiprows=2, names=["time",quantity])
            ax[i].plot(data["time"],data[quantity],label=potl)
        ax[i].set_xlabel("Time")
        ax[i].set_ylabel(ylabel)
        ax[i].legend()
        if log:
            ax[i].set_xscale("log")
            ax[i].set_yscale("log")
    fig.tight_layout()
    fig.savefig(quantity+("loglog" if log else "")+".png")

plotpng("msd", "Mean-squared displacement", True)