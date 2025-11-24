import pandas as pd
import matplotlib.pyplot as plt

def plotpng(quantity,ylabel,log):
    file = quantity + ".txt"
    data = pd.read_csv(file,  sep=" ",skiprows=2, names=["time",quantity])
    plt.figure()
    plt.scatter(data["time"],data[quantity],s=1)
    plt.xlabel("Time")
    plt.ylabel(ylabel)
    if log:
        plt.xscale("log")
        plt.yscale("log")
    plt.savefig("msd"+("loglog" if log else "")+".png")
    plt.close()

plotpng("msd", "Mean-squared displacement", False)
plotpng("msd", "Mean-squared displacement", True)