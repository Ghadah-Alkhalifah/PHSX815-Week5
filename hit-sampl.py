import numpy as np
import matplotlib.pyplot as plt

def target(x):
    
    k=np.cos(x)**4
    return k

def prop():
    a=0
    b=3
    return np.random.uniform(a, b)


def reject_sampl(target, prop):
    samples = []
    for i in range(1000000):
        reject = True
        while reject:
            y = prop()
            u = np.random.uniform(0,1)
            if u <= ((target(y))/1):
                samples.append(y)
                reject = False
    return samples

samples = reject_sampl(target, prop)

#plot 
x = np.linspace(0, 3, 1000)
plt.hist(samples, bins=80, density=True, alpha=0.7, label='Samples', color='skyblue')
plt.plot(x, target(x), label='Target function')
plt.plot(x, np.ones_like(x), label='Proposal function', color='r')
plt.xlim(0,3)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rejection sampling')
plt.legend()
plt.savefig('plot.png')
plt.show()


