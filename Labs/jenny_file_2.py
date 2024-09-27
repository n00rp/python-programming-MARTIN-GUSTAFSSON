from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

path = "Data/datapoints.txt"
def clean_and_parse_data(input_file):
    points = {'Pichu': [], 'Pikachu': []}
    for line in open(input_file, "r"):
        try:
            value1, value2, classification = map(float, line.split(","))
            points['Pikachu' if classification else 'Pichu'].append([value1, value2])
        except ValueError:
            print(f"Removed line: {line.strip()}")
    return points
# Define the points dictionary
points = clean_and_parse_data(path)

# Function to calculate the Euclidean distance between two points

def euclidean_distance(p, q):
    return np.linalg.norm(np.array(p) - np.array(q))
# Function to classify and plot the user-input point along with test data
def classify_and_plot(test_points, k=1):
    plt.title("Pikachu vs Pichu Classification")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

    # Calculate distances and classify for each test point
    for new_point in test_points:
        distances = [(euclidean_distance(p, new_point), pokemon) for pokemon in points for p in points[pokemon]]
        nearest_classes = [cls for _, cls in sorted(distances)[:k]]
        new_class = Counter(nearest_classes).most_common(1)[0][0]
        
        # Plot the data points and the new point
        for pokemon, points_list in points.items():
            color = '#FFCC00' if pokemon == 'Pikachu' else '#00CCCC'
    for p in points_list:
        plt.scatter(p[0], p[1], color=color, label=pokemon if pokemon not in plt.gca().get_legend_handles_labels()[1] else "")
    plt.scatter(test_points[0], test_points[1], color='#FFAA00' if new_class == 'Pikachu' else '#00FFAA', marker='*', s=200, label=f'New Point: {new_class}')

    plt.legend()
    plt.show()

# Get user input for new points
def get_user_input():
    while True:
        try:
            x = float(input("Enter the x-coordinate of the new point: "))
            y = float(input("Enter the y-coordinate of the new point: "))
            return [x, y]
        except ValueError:
            print("Invalid input. Please enter numerical values.")

# Populate the points dictionary


points = clean_and_parse_data(path)

# Classify and plot the user-input points
test_points = get_user_input()
classify_and_plot(test_points, k=1)