import numpy as np
import matplotlib.pyplot as plt

def target(x):
    
    k=np.cos(x)**4
    return k

def prop():
    a=0
    b=3
    return np.random.uniform(a, b)


def reject_sampl(target, proposal, num_sampl):
    samples = []
    for i in range(num_sampl):
        rejected = True
        while rejected:
            y = prop()
            u = np.random.uniform(0,1,1)
            if u <= (target(y)):
                samples.append(y)
                rejected = False
    return samples

samples = reject_sampl(target, prop, 1000000)

#plot 
x = np.linspace(0, 3, 1000)
plt.hist(samples, bins=80, density=True, alpha=0.7, label='Samples', color='skyblue')
plt.plot(x, target(x), label='Target Distribution')
plt.plot(x, np.ones_like(x), label='Proposal Distribution', color='r')
plt.xlim(0,3)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rejection sampling')
plt.legend()
plt.savefig('plot.png')
plt.show()


