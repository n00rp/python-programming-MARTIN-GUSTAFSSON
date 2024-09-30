# Datapoints
path = "Data/datapoints.txt" # Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)
def open_text(path):
    with open(path, "r") as f:
        next(f)
        return f.readlines()
#print(repr(text))
 
def clean_data(data): # funktion som gör en lista av alla rader i Data/datapoints.txt
    clean_data = []
    for line in data:
        clean_line = line.strip().split(",")
        clean_data.append(clean_line)
    return clean_data
# print(clean_data(open_text(path)))
 
def separate_clean_data(data): # funktion som hämtar värderna från clean_data och appendar pichus x, y värde från label 0. samt pikachus x,y värde från label 1.
    pichu = []
    pikachu = []
    for row in data:
        width,hight,label = row
        if label == " 0":
            pichu.append((float(width), float(hight)))
        elif label == " 1":
            pikachu.append((float(width), float(hight)))
    return pichu, pikachu
#print(separate_clean_data(clean_data(open_text(path))))
 
import matplotlib.pyplot as plt
import numpy as np
import math
 
def knn_equation(pichu, pikachu, user_input, k=11):
    classification = []
    for point in user_input:
        closest_points = sorted(pichu + pikachu, key=lambda x: math.sqrt((point[0] - float(x[0]))**2 + (point[1] - float(x[1]))**2))[:k]
        labels = [0 if point in pichu else 1 for point in closest_points]
        print(f"Etiketter för punkten {point}: {labels}")
        classify = 0 if labels.count(0) > labels.count(1) else 1
        classification.append(classify)
    return classification
#print(knn_equation(*separate_clean_data(clean_data(open_text(path))), new_test_points()))
 
def plott_classify_pokemon(pichu, pikachu, user_input, k=3): # Klassificerar ny data
    plott_new_classify_pokemon = knn_equation(pichu, pikachu, user_input)
    plt.scatter(*zip(*pichu), color= 'hotpink', label= 'Pichu', marker='*')
    plt.scatter(*zip(*pikachu), color= 'purple', label = 'Pikachu', marker='*')
    plt.title("Classification for the nearest point")
    plt.xlabel("X = Lenght")
    plt.ylabel("Y = Height")
 
    # Plottar ny data och klassificerar dessa som Pichu eller Pikachu
    for i, classifikation in enumerate(plott_new_classify_pokemon):
        if classifikation == 0:
            plt.scatter(user_input[i][0], user_input[i][1], color= 'aqua', label= 'New Pichu Point', marker= "X")
        else:
            plt.scatter(user_input[i][0], user_input[i][1], color= 'deepskyblue', label= 'New Pikachu Point', marker= "X")
    plt.legend()
    plt.show()
#plott_classify_pokemon(new_test_points(), *separate_clean_data(clean_data(open_text(path))))
 
def user_input():
    while True:
        try:
            x = float(input("Please enter an x-coordinate: "))
            y = float(input("Please enter an y-coordinate: "))
 
            if x < 0 or y < 0:
                print(f"Coordinates can't be negative. Please select new coordinates for X and Y.")
               
            else:
                print(f"The coordinate you choosed are: ({x}, {y}) and its classified in the Plot.")
                return [(x, y)]
        except ValueError:
            print("Invalid. You can only choose numeric inputs. Please choose positiv input for X and Y.")
 
user_inputs = user_input()
input = user_inputs
plott_classify_pokemon(*separate_clean_data(clean_data(open_text(path))), input, k=11)
 