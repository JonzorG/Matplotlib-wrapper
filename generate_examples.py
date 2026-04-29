import matplotlib.pyplot as plt
import numpy as np

from splitplot import plot_split_color

# Use a cool dark theme
plt.style.use('dark_background')

# Generate volatile, realistic-looking data
np.random.seed(42)
x = np.linspace(0, 15, 60)
# A sine wave mixed with an expanding trend and random noise
y = np.sin(x) * (x/2) + np.random.randn(60) * 2 

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9))

# --- BEFORE: The standard Matplotlib Masking problem ---
# Masking data leaves physical gaps where the lines cross zero
y_above = np.ma.masked_where(y < 0, y)
y_below = np.ma.masked_where(y > 0, y)

ax1.plot(x, y_above, color='#00ff00', linewidth=2, marker='o', markersize=4)
ax1.plot(x, y_below, color='#ff003c', linewidth=2, marker='o', markersize=4)
ax1.axhline(0, color='white', linestyle='--', alpha=0.4)
ax1.set_title("BEFORE: Standard Matplotlib (Masking leaves ugly gaps where data crosses 0)", fontsize=14, pad=15)
ax1.grid(True, alpha=0.15)

# --- AFTER: Your new library ---
plot_split_color(ax2, x, y, threshold=0, color_above='#00ff00', color_below='#ff003c', linewidth=2, marker='o', markersize=4)
ax2.axhline(0, color='white', linestyle='--', alpha=0.4)
ax2.set_title("AFTER: matplotlib-splitplot (Seamless linear interpolation across the threshold!)", fontsize=14, pad=15)
ax2.grid(True, alpha=0.15)

plt.tight_layout(pad=3.0)
plt.savefig('assets/showcase.png', dpi=300, bbox_inches='tight')
print("High-res showcase.png generated successfully!")
