

pichu = []
pikachu = []
classes = []
with open("Data/datapoints_clean.txt", "r") as list:
    for line in list:
        line_strip = line.strip()
        if line_strip:
            data_split = line_strip.split(",")

            try:
            
                value1 = round(float(data_split[0].strip()), 2)
                value2 = round(float(data_split[1].strip()), 2)
                classification = int(data_split[2].strip())
             

                if classification == 0:
                    pichu.append([value1, value2])
                    classes.append([classification])
                elif classification == 1:
                    pikachu.append([value1, value2])
                    classes.append([classification])

            except ValueError:
                print(f"Removed lines that were not able to be made into float or int")
            


import matplotlib.pyplot as plt

pichu_x = [point[0] for point in pichu]
pichu_y = [point[1] for point in pichu]

pikachu_x = [point[0] for point in pikachu]
pikachu_y = [point[1] for point in pikachu]

import matplotlib.pyplot as plt
import math

# k-NN Algorithm: Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Function to classify new points using k-Nearest Neighbors
def classify_new_point(new_point, dataset, k=3):
    distances = []
    
    # Calculate the distance between the new point and all points in the dataset
    for i, point in enumerate(dataset):
        distance = euclidean_distance(new_point, point[:2])
        distances.append((distance, i))  # Store the distance and the index of the point
    
    # Sort the distances (ascending order) and select the k closest points
    distances.sort(key=lambda x: x[0])
    nearest_neighbors = distances[:k]

    # Count the number of Pichu (class 0) and Pikachu (class 1) among the nearest neighbors
    class_votes = {0: 0, 1: 0}
    
    for _, idx in nearest_neighbors:
        class_votes[classes[idx][0]] += 1  # Increment the class vote (either Pichu or Pikachu)
    
    # Classify based on the majority vote
    if class_votes[1] > class_votes[0]:
        return "Pichu"
    else:
        return "Pikachu"

# Plot function for Pichu, Pikachu, and New Classified Points
def plot_data(pichu, pikachu, new_point=None, prediction=None):
    pichu_x = [point[0] for point in pichu]
    pichu_y = [point[1] for point in pichu]

    pikachu_x = [point[0] for point in pikachu]
    pikachu_y = [point[1] for point in pikachu]

    plt.figure(figsize=(8, 6))
    plt.title("Scatter Plot of Pikachu and Pichu Data")
    plt.xlabel("X-values (Length)")
    plt.ylabel("Y-values (Height)")

    # Plot Pichu in orange
    plt.scatter(pichu_x, pichu_y, color="orange", label="Pichu", marker="o")

    # Plot Pikachu in blue
    plt.scatter(pikachu_x, pikachu_y, color="blue", label="Pikachu", marker="o")

    # If a new point is classified, plot it in green with its prediction label
    if new_point:
        plt.scatter(new_point[0], new_point[1], color="green", label=f"New point ({prediction})", marker="x", s=100)
    
    plt.legend()
    plt.show()

# Function to read and clean data
def clean_and_parse_data(input_file):
    pichu = []
    pikachu = []
    classes = []

    with open(input_file, "r") as file:
        for line in file:
            line_strip = line.strip()
            if line_strip:
                data_split = line_strip.split(",")
                try:
                    value1 = round(float(data_split[0].strip()), 2)
                    value2 = round(float(data_split[1].strip()), 2)
                    classification = int(data_split[2].strip())
                    
                    if classification == 0:
                        pichu.append([value1, value2])
                        classes.append([classification])
                    elif classification == 1:
                        pikachu.append([value1, value2])
                        classes.append([classification])
                except ValueError:
                    print(f"Removed lines that could not be converted to float or int")

    return pichu, pikachu, classes

# Main function
def main():
    # Path to the cleaned data file
    data_path = "Data/datapoints_clean.txt"

    # Clean and parse data into Pichu, Pikachu, and classes
    pichu, pikachu, classes = clean_and_parse_data(data_path)

    # Plot the original data
    plot_data(pichu, pikachu)

    # Input new point for classification (You can also hardcode these values)
    try:
        new_value1 = float(input("Enter the X value for the new point: "))
        new_value2 = float(input("Enter the Y value for the new point: "))
        new_point = [new_value1, new_value2]
        
        # Classify the new point using k-NN
        dataset = pichu + pikachu  # Combine Pichu and Pikachu for classification
        prediction = classify_new_point(new_point, dataset, k=3)

        print(f"The new point ({new_value1}, {new_value2}) is classified as: {prediction}")

        # Plot the data along with the new point
        plot_data(pichu, pikachu, new_point, prediction)
    
    except ValueError:
        print("Invalid input. Please enter valid numerical values for the new point.")

# Run the main function
if __name__ == "__main__":
    main()
