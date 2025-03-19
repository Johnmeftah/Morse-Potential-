import numpy as np
import matplotlib.pyplot as plt

# def the Lennard-Jones potential function
def lennard_jones(r, epsilon=1, sigma=1):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# generate r values, avoiding r=0 to prevent division by zero
r = np.linspace(0.5, 3, 500)
U = lennard_jones(r)

# plotting
plt.figure(figsize=(6, 4))
plt.plot(r, U, 'k', linewidth=2)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(x=1, color='black', linestyle='dashed')  # to mark equilibrium position
plt.text(1.05, -0.5, 'R', fontsize=12)


plt.xlabel('r')
plt.ylabel('U')
plt.title('Potential Energy Curve')
plt.ylim(-1.5, 2)
plt.xlim(0.5, 3)
plt.show()
