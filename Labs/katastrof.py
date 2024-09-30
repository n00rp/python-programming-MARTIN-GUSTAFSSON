import math
import numpy as np

file_name = "Data/datapoints.txt"
test_data = "Data/testpoints.txt"
import matplotlib.pyplot as plt

def open_file(file_name): #Fuction to read the file
    with open(file_name, "r") as file:
        next(file)
        return file.readlines()


def new_points():
    test_points = []
    with open("Data/testpoints.txt", 'r') as f:
        next(f)  # Ta bort den första raden ("Test points:")
        for line in f:
            cordinate = line.split('(')[1].split(')')[0].split(', ')
            x = float(cordinate[0])
            y = float(cordinate[1])
            test_points.append((x, y))
    return test_points



def clean_data(data): #Data is a list of lines
    cleaned_data = []
    for line in data:
        cleaned_line = line.strip().split(",")
        cleaned_data.append(cleaned_line)
    return cleaned_data

def separate_data(data): #Function to separate the data into pichu and pikachu
    pichu = []
    pikachu = []
    for row in data:
        x, y, label = row
        if label == " 0":
            pichu.append((float(x), float(y)))
        elif label == " 1":
            pikachu.append((float(x), float(y)))
    
    return pichu, pikachu

def plot_data(pichu, pikachu): #Fuction to plot the data
    plt.figure(figsize=(8, 6))
    plt.title("Scatter Plot of Pikachu and Pichu Data")
    plt.xlabel("X-values (Length)")
    plt.ylabel("Y-values (Height)")
    plt.scatter(*zip(*pichu), color='orange', label='Pichu', marker='o')
    plt.scatter(*zip(*pikachu), color='blue', label='Pikachu', marker='o')

    plt.legend()
    plt.show()

#plot_data(*separate_data(clean_data(open_file(file_name))))
print(type(new_points()))

def simplified_knn(pichu, pikachu, new_points, user_input):
    classification = []
    for point in new_points + [tuple(user_input)]:
        print(type(point))
        minimum_distance = float('inf')
        closest_point = None
        for data_point in pichu + pikachu:
            print(type(data_point))
            distance = math.sqrt((point[0] - data_point[0])**2 + (point[1] - data_point[1])**2)
            if distance < minimum_distance:
                minimum_distance = distance
                closest_point = data_point
        classify = 0 if closest_point in pichu else 1
        classification.append(classify)
    return classification
#print(simplified_knn(*separate_data(clean_data(open_file(file_name))), new_points()))


def plot_and_classify(new_data, pichu, pikachu, user_input):
    # Klassificera ny data
    new_data_classification = simplified_knn(pichu, pikachu, new_data, [user_input])[0]

    # Plotta befintlig data och ny data
    plt.scatter([point[0] for point in pichu], [point[1] for point in pichu], color ='magenta', label='Pichu', marker='o', s=50)
    plt.scatter([point[0] for point in pikachu], [point[1] for point in pikachu], color ='aqua', label='Pikachu', marker='o', s=50)
    if new_data_classification == 0:
        plt.scatter(user_input[0], user_input[1], color ='blueviolet', s= 100, label='New Pichu', marker='*')
    else:
        plt.scatter(user_input[0], user_input[1], color ='deepskyblue', s= 100, label='New Pikachu', marker='*')
    plt.legend()
    plt.show()
#plot_data(*separate_data(clean_data(open_file(file_name))))


def get_user_input():
    while True:
        try:
            return [float(input("Enter the x-coordinate of the new point: ")), float(input("Enter the y-coordinate of the new point: "))]
        except ValueError:
            print("Invalid input. Please enter numerical values.")

user_input_point = get_user_input()
user_input = user_input_point



print(type(user_input))

plot_and_classify(new_points(), *separate_data(clean_data(open_file(file_name))), user_input)

