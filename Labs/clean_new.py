import numpy as np
import matplotlib.pyplot as plt

# File paths
path = "Data/datapoints.txt"

# Step 1: Read and clean data from the file
def clean_and_parse_data(input_file):
    points = {'Pichu': [], 'Pikachu': []}
    for line in open(input_file, "r"):
        try:
            value1, value2, classification = map(float, line.split(","))
            points['Pikachu' if classification else 'Pichu'].append([value1, value2])
        except ValueError:
            print(f"Removed line: {line.strip()}")
    return points

points = clean_and_parse_data(path)

# Step 2: Euclidean distance function
def euclidean_distance(p, q):
    return np.linalg.norm(np.array(p) - np.array(q))

# Step 3: k-NN function to classify and plot
def classify_and_plot(test_points, k=1):
    plt.title("Pikachu vs Pichu Classification")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

    for new_point in test_points:
        distances = [(euclidean_distance(p, new_point), pokemon) for pokemon, p_list in points.items() for p in p_list]
        new_class = max(set([cls for _, cls in sorted(distances)[:k]]), key=[cls for _, cls in sorted(distances)[:k]].count)

        for pokemon, p_list in points.items():
            color = '#FFCC00' if pokemon == 'Pikachu' else '#00CCCC'
            plt.scatter(*zip(*p_list), color=color, label=pokemon)
        plt.scatter(*new_point, color='#FFAA00' if new_class == 'Pikachu' else '#00FFAA', marker='*', s=200, label=f'New Point: {new_class}')

        print(f"The new point {new_point} is classified as: {new_class}")

    plt.legend()
    plt.show()

# Step 4: Function to accept user input
def get_user_input():
    while True:
        try:
            return [float(input("Enter the x-coordinate of the new point: ")), float(input("Enter the y-coordinate of the new point: "))]
        except ValueError:
            print("Invalid input. Please enter numerical values.")

# Step 5: Test point entered by the user
user_input_point = get_user_input()

# Step 6: Classify and plot the user-input point along with test data
test_points = [user_input_point]
classify_and_plot(test_points, k=1)