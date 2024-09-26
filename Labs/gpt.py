import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# File paths
path = "Data/datapoints.txt"
cleaned_path = "Data/datapoints_clean.txt"

# Step 1: Read and clean data from the file
pichu = []
pikachu = []
with open(path, "r") as f_read, open(cleaned_path, "w") as f_write:
    f_write.write("Pokémon list\n\n")
    for line in f_read:
        line_strip = line.strip()
        if line_strip:
            data_split = line_strip.split(",")
            try:
                value1 = round(float(data_split[0].strip()), 2)
                value2 = round(float(data_split[1].strip()), 2)
                classification = int(data_split[2].strip())
                if classification == 0:
                    pichu.append([value1, value2])
                elif classification == 1:
                    pikachu.append([value1, value2])
                f_write.write(f"{value1}, {value2}, {classification}\n")
            except ValueError:
                print(f"Removed line: {line.strip()}")

# Combine Pichu and Pikachu into points dictionary
points = {'Pichu': pichu, 'Pikachu': pikachu}

# Step 2: Euclidean distance function
def euclidean_distance(p, q):
    return np.linalg.norm(np.array(p) - np.array(q))

# Step 3: k-NN function to classify and plot
def classify_and_plot(test_points, k=1):  # Set k=1 for nearest neighbor classification
    plt.title("Pikachu vs Pichu Classification")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

    # Calculate distances and classify for each test point
    for new_point in test_points:
        distances = [(euclidean_distance(p, new_point), pokemon) for pokemon in points for p in points[pokemon]]
        nearest_classes = [cls for _, cls in sorted(distances)[:k]]
        new_class = Counter(nearest_classes).most_common(1)[0][0]
        
        # Plot the data points and the new point
        for pokemon in points:
            color = '#FFCC00' if pokemon == 'Pikachu' else '#00CCCC'
            for p in points[pokemon]:
                plt.scatter(*p, color=color, label=pokemon if pokemon not in plt.gca().get_legend_handles_labels()[1] else "")
        plt.scatter(*new_point, color='#FFAA00' if new_class == 'Pikachu' else '#00FFAA', marker='*', s=200, label=f'New Point: {new_class}')
        
        print(f"The new point {new_point} is classified as: {new_class}")

    plt.legend()
    plt.show()

# Step 4: Function to accept user input
def get_user_input():
    try:
        x = float(input("Enter the x-coordinate of the new point: "))
        y = float(input("Enter the y-coordinate of the new point: "))
        return [x, y]
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return get_user_input()

# Step 5: Test point entered by the user
user_input_point = get_user_input()

# Step 6: Classify and plot the user-input point along with test data
test_points = [user_input_point]  # We can add more test points if needed
classify_and_plot(test_points, k=3)  # Use k=3 for classification
