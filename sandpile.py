import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
sns.set()

def addsand(lattice):
    """add sand to model

    Args:
        lattice (2d_array): 

    Returns:
        2d_array: lattice that sand has been added
    """
    N = len(lattice)
    x,y = np.random.randint(N, size=2)
    lattice[x,y] +=1
    return lattice
    
def check(lattice):
    """check that an avalanche is happend or not

    Args:
        lattice (2d_array):
    """
    size = set()
    n = len(lattice)
    while True:
        unstable = np.argwhere(lattice >= 4)
        if unstable.size == 0:
            break
        for i,j in unstable:
            size.add((i,j))
            lattice[i,j] -= 4
            if i > 0:
                lattice[i-1,j] += 1
            if i < n-1:
                lattice[i+1,j] += 1
            if j > 0:
                lattice[i,j-1] += 1
            if j < n-1:
                lattice[i,j+1] += 1
    return lattice,size

        
def simulate(lattice,i):
    """simulate sand pile

    Args:
        lattice (2d_array): 
        i (int): number of itreation

    Returns:
        2d_array: lattice
    """
    Size = []
    for _ in range(i):
        lattice = addsand(lattice)
        lattice, size = check(lattice)
        Size.append(size)

    return lattice, np.array(Size)

def CountFrequency(my_list):
    """count frequency of the list

    Args:
        my_list (list): list of a pint that avalanche has happend

    Returns:
        dictinary: a dictionary that keys are items in list and its values are frequency of items
    """
    L = []
    for i in my_list:
        L.append(len(i))
    freq = {}
    for item in L:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def line(x,a,b):
    """equation of line"""
    return a*x+b

if __name__ == "__main__":

    N = 50 #number of lattice
    nstep = 1000 #number of iteration
    lattice = np.random.choice(range(4), (N,N)) # initital state

    lattice , Size = simulate(lattice, nstep)

    Freq = CountFrequency(Size)
    Freq = dict(sorted(Freq.items()))
    size = np.array([i for i in Freq.keys()])
    freq = np.array([j for j in Freq.values()])
    
    #add some small value to data for zero 
    size = np.log10(size+ 1.000001)
    freq = np.log10(freq+ 1.000001)

    #fit a line on data for find slop
    param, _ = curve_fit(line,size, freq)
    curve = line(size, param[0], param[1])

    #plot
    fig = plt.figure(figsize=(9,7))
    ax = plt.axes()
    ax.set_title(f"Sandpile simultion with N = {N} after {nstep} iterations")
    sns.heatmap(lattice, cmap="viridis", cbar=True, yticklabels=False, xticklabels=False, vmin = 0, vmax = 4)
    plt.savefig(f"Sandpile simultion_{N}")


    fig2 = plt.figure(figsize=(9,7))
    plt.plot(size, freq, 'm.')
    plt.plot(size , curve)
    plt.xlabel("Size of avalanches")
    plt.ylabel("Frequency")
    plt.title(fr"Frequency of avalanches with N = {N} after {nstep} iterations, $\tau = {param[0]}$")
    plt.savefig(f"size-frequency_g_{N}")
