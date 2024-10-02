import math
import matplotlib.pyplot as plt
file_name = "python-programming-MARTIN-GUSTAFSSON/Data/datapoints.txt"
test_file = "python-programming-MARTIN-GUSTAFSSON/Data/testpoints.txt"

#Rensa data för att kunna använda senare
def clean_data(data):
    cleaned_data = []
    for line in data:
        cleaned_line = line.strip().split(",")
        cleaned_data.append(cleaned_line)
    return cleaned_data

#Plockar pikachu och pichu och skapar listor med X och Y värden
def separate_data(data):
    pichu = []
    pikachu = []
    for row in data:
        x, y, label = row
        if label == " 0":
            pichu.append((float(x), float(y)))
        elif label == " 1":
            pikachu.append((float(x), float(y)))
    return pichu, pikachu

#Räknar ut minsta avståndet mellan punkterna för att kunna klassificera punkterna
def simplified_knn(pichu, pikachu, user_input, k=3):
    classification = []
    for point in user_input:
        closest_point = min(pichu + pikachu, key=lambda x: math.sqrt((point[0] - float(x[0]))**2 + (point[1] - float(x[1]))**2))[:k]
        classification.append(0 if closest_point in pichu else 1)
        
    return classification

#Plottar befintlig data och ny data efter att den klassificerats mellan pichu och pikachu
def plot_and_classify(pichu, pikachu, user_input, k=3):
    new_data_classification = simplified_knn(pichu, pikachu, [user_input])[0]
   
    plt.scatter([point[0] for point in pichu], [point[1] for point in pichu], color ='magenta', label='Pichu', marker='o', s=50)
    plt.scatter([point[0] for point in pikachu], [point[1] for point in pikachu], color ='aqua', label='Pikachu', marker='o', s=50)
    if new_data_classification == 0:
        plt.scatter(user_input[0], user_input[1], color ='blueviolet', s= 100, label='New Pichu', marker='*')
    else:
        plt.scatter(user_input[0], user_input[1], color ='deepskyblue', s= 100, label='New Pikachu', marker='*')
    plt.legend()
    plt.show()

#Får användaren att mata in X och Y värden
def get_user_input():
    while True:
        try:
            return [float(input("Enter the x-coordinate of the new point: ")), float(input("Enter the y-coordinate of the new point: "))]
        except ValueError:
            print("Invalid input. Please enter a real number.")



with open(file_name, "r") as file:
    next(file)
    data = file.readlines()

pichu, pikachu = separate_data(clean_data(data)) 
user_input_point = get_user_input()
plot_and_classify(pichu, pikachu, user_input_point, k=11) 

#Klassificera testdata och printa ut dess klassificering: 

test_points = []
with open(test_file, 'r') as f:
    next(f)  
    for line in f:
        cordinate = line.split('(')[1].split(')')[0].split(', ')
        x = float(cordinate[0])
        y = float(cordinate[1])
        test_points.append((x, y))
classification = simplified_knn(pichu, pikachu, test_points)
seen_points = set()
for i, point in enumerate(test_points):
    if point not in seen_points:
        print(f"Testpunkt ({point[0]}, {point[1]}) klassificerad som: {'Pichu' if classification[i] == 0 else 'Pikachu'}")
        seen_points.add(point)


