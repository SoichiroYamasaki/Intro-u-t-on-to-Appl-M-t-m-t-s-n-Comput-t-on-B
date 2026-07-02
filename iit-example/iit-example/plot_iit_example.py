#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Time steps
time = np.arange(0, 20, 1)

# Independent system:
# Node A and Node B change independently
A_independent = np.sin(time)
B_independent = np.cos(time * 1.7)

# Integrated system:
# Node A and Node B influence each other
A_integrated = np.sin(time)
B_integrated = 0.7 * A_integrated + 0.3 * np.cos(time)

plt.figure(figsize=(10, 5))

# Plot independent system
plt.subplot(1, 2, 1)
plt.plot(time, A_independent, label="Node A")
plt.plot(time, B_independent, label="Node B")
plt.title("Independent System")
plt.xlabel("Time")
plt.ylabel("State")
plt.legend()

# Plot integrated system
plt.subplot(1, 2, 2)
plt.plot(time, A_integrated, label="Node A")
plt.plot(time, B_integrated, label="Node B")
plt.title("Integrated System")
plt.xlabel("Time")
plt.ylabel("State")
plt.legend()

plt.suptitle("Example of IIT: Independent vs Integrated Information")
plt.tight_layout()
plt.show()
