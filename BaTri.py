import matplotlib.pyplot as plt
import numpy as np


def point_triangle(p, a, b, c):
    """
    Determine whether a point lies inside a triangle.

    Parameters
    ----------
    p : numpy.ndarray
        Point to test.
    a : numpy.ndarray
        First triangle vertex.
    b : numpy.ndarray
        Second triangle vertex.
    c : numpy.ndarray
        Third triangle vertex.

    Returns
    -------
    bool
        True if the point lies inside or on the boundary of the
        triangle, otherwise False.
    """
    v0 = c - a
    v1 = b - a
    v2 = p - a

    dot00 = np.dot(v0, v0)
    dot01 = np.dot(v0, v1)
    dot02 = np.dot(v0, v2)
    dot11 = np.dot(v1, v1)
    dot12 = np.dot(v1, v2)

    denom = dot00 * dot11 - dot01 * dot01

    u = (dot11 * dot02 - dot01 * dot12) / denom
    v = (dot00 * dot12 - dot01 * dot02) / denom

    return (u >= 0) and (v >= 0) and (u + v <= 1)


def plot_point(point=(550, 500), point_label="My Research"):
    """Plot and label a point on the triangle."""
    px, py = point

    plt.scatter(px, py, c="black", s=100, label=point_label)
    plt.text(px + 15, py + 15, point_label,
             fontsize=12, fontfamily="serif",
             fontweight="bold")


def plot_triangle(width=800, height=700, border=10, point=(550, 500), point_label="My Research",
                  filename=None):
    """
    Generate and display a color triangle visualization.

    Parameters
    ----------
    width : int, optional
        Width of the image in pixels. Default is 800.
    height : int, optional
        Height of the image in pixels. Default is 700.
    border : int, optional
        Margin between the triangle and image boundaries.
        Default is 10.
    point : tuple, optional
        Coordinates of the point to display on the triangle.
        Default is (550, 500).
    point_label : str, optional
        Label displayed beside the point.
        Default is "My Research".
    filename : str, optional
        Filename used to save the figure.

    Returns
    -------
    None
        Displays the triangle plot.
    """
    image = np.ones((height, width, 3), dtype=float)

    red_point = np.array([width / 2, border * 4])
    green_point = np.array([border * 4, height - border * 4])
    blue_point = np.array([width - border * 4, height - border * 4])

    max_dist = max(
        np.linalg.norm(red_point - green_point),
        np.linalg.norm(red_point - blue_point),
        np.linalg.norm(green_point - blue_point),
    )

    # Generate triangle image
    for y in range(height):
        for x in range(width):
            p = np.array([x, y])

            if point_triangle(p, red_point, green_point, blue_point):
                d_red = np.linalg.norm(p - red_point)
                d_green = np.linalg.norm(p - green_point)
                d_blue = np.linalg.norm(p - blue_point)

                r = 1.0 - d_red / max_dist
                g = 1.0 - d_green / max_dist
                b = 1.0 - d_blue / max_dist

                color = np.array([r, g, b])
                color /= color.max()

                image[y, x] = color

    # Plot
    plt.figure(figsize=(8, 7))
    plt.imshow(image)

    plt.text(red_point[0], red_point[1] - 20, "Physical",
             fontsize=12, fontweight="bold",
             fontfamily="serif", ha="center")

    plt.text(green_point[0] - 25, green_point[1] + 20, "Analytical",
             fontsize=12, fontweight="bold",
             fontfamily="serif", ha="center")

    plt.text(blue_point[0] + 25, blue_point[1] + 20, "Data-driven",
             fontsize=12, fontweight="bold",
             fontfamily="serif", ha="center")

    plot_point(point, point_label)

    plt.axis("off")

    if filename:
        plt.savefig(filename, bbox_inches="tight")

    plt.show()


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    plot_triangle(filename=filename)