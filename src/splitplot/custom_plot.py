import numpy as np


def plot_split_color(ax, x, y, threshold=0, color_above='red', color_below='blue', **kwargs):
    """
    Plots a line on the given axes, changing color when it crosses a specific threshold.
    """
    # Ensure inputs are numpy arrays for mathematical operations
    x = np.asarray(x)
    y = np.asarray(y)

    # 1. Find crossings relative to the threshold
    # np.signbit returns True for negative numbers. We check the sign of (y - threshold).
    crossings = np.where(np.diff(np.signbit(y - threshold)))[0]
    
    # 2. Calculate slopes (dx, dy) for interpolation
    dx = x[crossings + 1] - x[crossings]
    dy = y[crossings + 1] - y[crossings]

    # Avoid division by zero if two adjacent points have the exact same y-value
    dy[dy == 0] = 1e-9 
    
    # 3. Interpolate the exact x-coordinates where y crosses the threshold
    x_cross = x[crossings] - (y[crossings] - threshold) * (dx / dy)
    y_cross = np.full_like(x_cross, threshold) # The y-value is exactly the threshold

    # 4. Combine and sort the arrays
    x_combined = np.concatenate([x, x_cross])
    y_combined = np.concatenate([y, y_cross])

    sort_idx = np.argsort(x_combined)
    x_combined = x_combined[sort_idx]
    y_combined = y_combined[sort_idx]

    # 5. Mask the data for plotting
    y_above = np.ma.masked_where(y_combined < threshold, y_combined)
    y_below = np.ma.masked_where(y_combined > threshold, y_combined)

    # 6. Plot the separated lines
    ax.plot(x_combined, y_above, color=color_above, **kwargs)
    ax.plot(x_combined, y_below, color=color_below, **kwargs)
    
    return ax
