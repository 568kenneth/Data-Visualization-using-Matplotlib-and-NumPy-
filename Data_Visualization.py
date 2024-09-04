# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Gravitational acceleration values for Earth, Jupiter, and Mercury (m/s^2)
g_earth = 9.81
g_jupiter = 24.79
g_mercury = 3.72

# Generate an array of time values from 0 to 10 seconds in 1-second intervals
time = np.arange(0, 11, 1)

# Define a function to calculate displacement using the formula: s = 0.5 * g * t^2
def displacement(g, t):
    result = 0.5 * g * t**2
    return result

# Calculate displacement for each planet using the corresponding gravitational acceleration
y_earth = displacement(g_earth, time)
y_jupiter = displacement(g_jupiter, time)
y_mercury = displacement(g_mercury, time)

# Print the calculated displacements for each planet
print(y_earth)
print(y_jupiter)
print(y_mercury)

# Plot the distance fallen over time on Earth
plt.plot(time, y_earth, label='Earth', color='b')
plt.title('Distance fallen as a function of time on Earth')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.legend()
plt.show()

# Plot the distance fallen over time on both Earth and Jupiter for comparison
plt.plot(time, y_earth, label='Earth', color='b')
plt.plot(time, y_jupiter, label='Jupiter', color='r')
plt.title('Distance fallen as a function of time on Earth and Jupiter')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.legend()
plt.show()

# Create a subplot with 3 rows and 1 column to plot each planet's distance fallen separately
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Plot the distance fallen over time on Earth in the first subplot
axs[0].plot(time, y_earth, label='Earth', color='b')
axs[0].set_title('Distance fallen as a function of time on Earth')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Distance (m)')
axs[0].legend()

# Plot the distance fallen over time on Jupiter in the second subplot
axs[1].plot(time, y_jupiter, label='Jupiter', color='r')
axs[1].set_title('Distance fallen as a function of time on Jupiter')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Distance (m)')
axs[1].legend()

# Plot the distance fallen over time on Mercury in the third subplot
axs[2].plot(time, y_mercury, label='Mercury', color='g')
axs[2].set_title('Distance fallen as a function of time on Mercury')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Distance (m)')
axs[2].legend()

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
