import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

timestep = 0.001

def autocorrelation(x,lag): # lag in number of timesteps, not time units
    n = len(x)
    xd = x - np.mean(x)
    xlagged = xd[lag:]
    xcropped = xd[:n-lag]
    product = xlagged * xcropped
    normfac = np.var(xd) # R for lag=0
    R = np.mean(product)/normfac
    return R

def plotforces(atomid):
    df = pd.read_csv(f"forces_ID{atomid}.csv")
    plt.style.use("seaborn-v0_8-poster")
    fig,ax = plt.subplots(1,2,figsize=(12,5))
    cs = ["x","y","z"]
    for c in cs:
        ax[0].plot(df["time"]*timestep,df["f"+c],label=f"{c}-direction")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Force")
    ax[0].legend()
    ax[0].set_title(f"Force components (Atom ID {atomid})")
    
    fmag = [np.sqrt(df["fx"][i]**2 + df["fy"][i]**2 + df["fz"][i]**2) 
            for i in range(df.shape[0])]
    ax[1].plot(df["time"]*timestep,fmag)
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Force")
    ax[1].set_ylim([0,None])
    ax[1].set_title(f"Force magnitude (Atom ID {atomid})")

    fig.text(0,0.95,"a",size="xx-large")

    fig.tight_layout()
    fig.savefig(f"forces_ID{atomid}.png")

interval = 10000
timeperlag = interval * timestep

def plotforcewcorr(atomids):
    plt.style.use("seaborn-v0_8-poster")
    fig,ax = plt.subplots(1,1,figsize=(7,5))
    
    for atomid in atomids:
        df = pd.read_csv(f"forces_ID{atomid}.csv")
        fmag = [np.sqrt(df["fx"][i]**2 + df["fy"][i]**2 + df["fz"][i]**2) 
            for i in range(df.shape[0])]
        lags = np.array([int(x) for x in np.arange(20+1)])
        ac = [autocorrelation(fmag,l) for l in lags]
        ax.plot(lags*timeperlag, ac, label=f"Atom ID {atomid}")
    ax.axhline(y=0,lw=1,c="k",ls="--")
    ax.legend(ncols=2)
    ax.set_xlabel("Lag time")
    ax.set_ylabel("Force autocorrelation")

    fig.text(0,0.95,"b",size="xx-large")

    fig.tight_layout()
    fig.savefig(f"autocorrelation.png")

selection = [73, 86, 90, 99, 101, 102, 117, 121]
for id in selection:
    plotforces(id)

plotforcewcorr(selection)