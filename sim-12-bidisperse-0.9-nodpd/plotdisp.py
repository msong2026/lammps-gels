import pandas as pd
import matplotlib.pyplot as plt

def plotpng(quantity,ylabel,log):
    file = quantity + ".txt"
    data = pd.read_csv(file,  sep=" ",skiprows=2, names=["time",quantity])
    plt.style.use("seaborn-v0_8-poster")
    plt.figure(figsize=(8,5))
    plt.plot(data["time"]*0.001,data[quantity])
    plt.xlabel("Time")
    plt.ylabel(ylabel)
    if log:
        plt.xscale("log")
        plt.yscale("log")
    plt.tight_layout()
    plt.savefig("msd"+("loglog" if log else "")+".png")
    plt.close()

plotpng("msd", "Mean-squared displacement", False)
plotpng("msd", "Mean-squared displacement", True)