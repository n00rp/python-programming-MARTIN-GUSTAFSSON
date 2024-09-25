
path = "Data/datapoints.txt"

with open(path, "r") as f:
    text = f.read()

#print(repr(text))

import re
import math
quotes = []

with open(path, "r") as f_read, open("Data/datapoints_clean.txt", "w") as f_write:
    f_write.write("Pokémon list\n\n")
    for quote in f_read:
        #quote = quote.strip(" \n")
        #quote = re.sub(r" +", " ", quote)
        if quote != "":
            f_write.write(f"{quote}\n")

pichu = []
pikachu = []

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
                    pichu.append([value1, value2, classification])
                elif classification == 1:
                    pikachu.append([value1, value2, classification])

            except ValueError:
                print(f"Removed lines that were not able to be made into float or int")
                


    

import matplotlib.pyplot as plt

pichu_x = [point[0] for point in pichu]
pichu_y = [point[1] for point in pichu]

pikachu_x = [point[0] for point in pikachu]
pikachu_y = [point[1] for point in pikachu]

plt.title("Scatter chart over length and hight of Pikachu and Pichu")
plt.xlabel("Pikachus and Pichus X-values")
plt.ylabel("Pikachus and Pichus Y-values")
plt.legend()
plt.scatter(pichu_x, pichu_y, color= "orange", marker = "o")
plt.scatter(pikachu_x, pikachu_y, color= "blue", marker = "o")
plt.show()

path_new = "Data/testpoints.txt"

with open(path_new, "r") as f:
    test_points = f.read()

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
            
                             