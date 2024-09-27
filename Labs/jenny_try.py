import numpy as np
import matplotlib.pyplot as plt
datapoints_file = "Data/datapoints.txt"
# Load data from file
def load_data(datapoints_file):
    points = {}
    with open("Data/datapoints.txt", "r") as f:
        for line in f:
            pokemon, x, y = line.strip().split(',')
            if pokemon not in points:
                points[pokemon] = []
            points[pokemon].append((float(x), float(y)))
    return points

# Calculate distances and classify points
def classify_points(points):
    classified_points = {}
    for pokemon, points_list in points.items():
        for point in points_list:
            distances = [(np.linalg.norm(np.array(point) - np.array(other_point)), other_pokemon) for other_pokemon, other_points in points.items() for other_point in other_points]
            closest_point = min(distances, key=lambda x: x[0])
            classified_points[point] = closest_point[1]
    return classified_points

# Plot points and distances
def plot_points(points, classified_points):
    for pokemon, points_list in points.items():
        for point in points_list:
            plt.scatter(point[0], point[1], color='red' if pokemon == 'Pikachu' else 'blue', marker='o', label=pokemon)
    for point, classification in classified_points.items():
        plt.scatter(point[0], point[1], color='green' if classification == 'Pikachu' else 'yellow', marker='*', s=200, label=f'Classified as {classification}')
    plt.title("The classification for the nearest point")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

# Main program
def main():
    filename = "datapoints.txt"
    points = load_data(filename)
    classified_points = classify_points(points)
    plot_points(points, classified_points)

if __name__ == "__main__":
    main()