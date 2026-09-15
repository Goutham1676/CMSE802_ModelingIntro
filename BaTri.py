import numpy as np
import matplotlib.pyplot as plt

def point_triangle(p, a, b, c):
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


def plot_triangle(width=800, height=700, border=10,
                  point=(630, 500), point_label="My Research"):

    image = np.ones((height, width, 3), dtype=float)

    red_point = np.array([width / 2, border * 4])
    green_point = np.array([border * 4, height - border * 4])
    blue_point = np.array([width - border * 4, height - border * 4])

    max_dist = max(
        np.linalg.norm(red_point - green_point),
        np.linalg.norm(red_point - blue_point),
        np.linalg.norm(green_point - blue_point),
    )

    # --- Generate triangle image ---
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

    # --- Plot everything (correct indentation!) ---
    plt.figure(figsize=(8, 7))
    plt.imshow(image)

    plt.text(red_point[0], red_point[1] - 20, "Physical",
             fontsize=12, fontweight='bold', fontfamily='serif', ha='center')
    plt.text(green_point[0] - 25, green_point[1] + 20, "Analytical",
             fontsize=12, fontweight='bold', fontfamily='serif', ha='center')
    plt.text(blue_point[0] + 25, blue_point[1] + 20, "Data-driven",
             fontsize=12, fontweight='bold', fontfamily='serif', ha='center')

    px, py = point
    plt.scatter(px, py, c='black', s=100, label=point_label)
    plt.text(px + 15, py + 15, point_label,
             fontsize=12, fontfamily='serif', fontweight='bold')

    plt.axis("off")
    plt.show()

    # return image, red_point, green_point, blue_point (indentated if the image is not needed outside function
