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

# Combine pichu and pikachu into points dictionary
points = {'blue': pichu, 'orange': pikachu}

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
        distances = [(euclidean_distance(p, new_point), color) for color in points for p in points[color]]
        nearest_classes = [cls for _, cls in sorted(distances)[:k]]
        new_class = Counter(nearest_classes).most_common(1)[0][0]
        
        # Plot the data points and the new point
        for color in points:
            for p in points[color]:
                plt.scatter(*p, color=color)
        plt.scatter(*new_point, color=new_class, marker='*', s=200)  # New point with larger size
        print(f"The new point {new_point} is classified as: {new_class}")

    plt.show()

# Step 4: Test points
test_points = [(25, 32), (24.2, 31.5), (22, 34), (20.5, 34)]

# Step 5: Classify and plot the test points
classify_and_plot(test_points, k=1)  # Use k=1 for classification
