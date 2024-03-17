import numpy as np
import matplotlib.pyplot as plt


def estimate_pi(num_samples):
    points_inside_circle = 0
    points_inside_square = 0

    # Generate random points within the square
    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)

        # Check if the point is inside the circle
        if x ** 2 + y ** 2 <= 1:
            points_inside_circle += 1
        points_inside_square += 1

    # Calculate the pi approximation
    pi_approximation = 4 * (points_inside_circle / points_inside_square)
    return pi_approximation


def visualize_pi(pi_approximation):
    angles = np.linspace(0, 2 * np.pi, 1000)
    x = np.cos(angles)
    y = np.sin(angles)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

    # Plot the circle in different colors
    num_lines = 1000
    colors = plt.cm.rainbow(np.linspace(0, 1, num_lines))
    for i in range(num_lines):
        ax.plot(x, y, color=colors[i], linewidth=0.5)

    # Generate random points and connect them to form a circle
    num_points = 1000
    points = np.random.uniform(-1, 1, (num_points, 2))
    points = points / np.linalg.norm(points, axis=1)[:, None]
    ax.plot(points[:, 0], points[:, 1], 'k-', linewidth=0.5)

    # Show the pi approximation as the title
    ax.set_title(f"Approximation of Pi: {pi_approximation:.6f}")
    plt.show()


# Number of samples to use for the Monte Carlo method
num_samples = 10000

# Estimate pi using the Monte Carlo method
pi_approximation = estimate_pi(num_samples)

# Visualize the approximation of pi
visualize_pi(pi_approximation)