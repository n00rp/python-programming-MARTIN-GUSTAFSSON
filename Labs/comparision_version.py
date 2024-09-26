import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    points = {'Pichu': [], 'Pikachu': []}
    with open(file_path, "r") as f:
        for line in f:
            try:
                value1, value2, classification = map(float, line.split(","))
                points['Pikachu' if classification else 'Pichu'].append([value1, value2])
            except ValueError:
                print(f"Removed line: {line.strip()}")
    return points

def euclidean_distance(p, q):
    return np.linalg.norm(np.array(p) - np.array(q))

def classify_and_plot(points, test_points, k=27):
    plt.title("Pikachu vs Pichu Classification")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

    for pokemon, p_list in points.items():
        plt.scatter(*zip(*p_list), color='#FFCC00' if pokemon == 'Pikachu' else '#00CCCC', label=pokemon)

    for new_point in test_points:
        distances = [(euclidean_distance(p, new_point), pokemon) for pokemon, p_list in points.items() for p in p_list]
        new_class = max(set([cls for _, cls in sorted(distances)[:k]]), key=[cls for _, cls in sorted(distances)[:k]].count)
        plt.scatter(*new_point, color='#FFAA00' if new_class == 'Pikachu' else '#00FFAA', marker='*', s=200, label=f'New Point: {new_class}')
        print(f"The new point {new_point} is classified as: {new_class}")

    plt.legend()
    plt.show()

def get_user_input():
    while True:
        try:
            return [float(input("Enter the x-coordinate of the new point: ")), float(input("Enter the y-coordinate of the new point: "))]
        except ValueError:
            print("Invalid input. Please enter numerical values.")

file_path = "Data/datapoints.txt"
points = load_data(file_path)
user_input_point = get_user_input()
classify_and_plot(points, [user_input_point], k=27)