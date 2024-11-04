

#1. Basic lineplot
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot
plt.figure()
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

#2. Scatter plot
import matplotlib.pyplot as plt

# Data
x = np.random.rand(50)
y = np.random.rand(50)

# Plot
plt.figure()
plt.scatter(x, y, color='blue', alpha=0.5)
plt.title("Random Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()


#3. Bar Chart
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Plot
plt.figure()
plt.bar(categories, values, color='orange')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


#4. Histogram
import matplotlib.pyplot as plt

# Data
data = np.random.randn(1000)

# Plot
plt.figure()
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


#5. Pie Chart
import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Plot
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart Example")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



#6. Subplots
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

axs[0].plot(x, y1, 'r', label='sin(x)')
axs[0].set_title("Sine Function")
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x, y2, 'b', label='cos(x)')
axs[1].set_title("Cosine Function")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()


#7. Customized plot
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.tan(x)

# Plot
plt.figure()
plt.plot(x, y, color='green', linestyle='--', linewidth=2)
plt.title("Tangent Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.ylim(-10, 10)  # Limit y-axis to avoid extreme values
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Add x-axis line
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Add y-axis line
plt.grid(True)
plt.show()

