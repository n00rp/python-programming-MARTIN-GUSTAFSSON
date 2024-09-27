# Datapoints
path = "Data/datapoints.txt" # Gå in i fil, open folder, välj den mapp som du vill öppna vs code med. (Python-programming-JENNY_SKOGLUND)

with open(path, "r") as f:
    text = f.read()
# print(repr(text))

quotes = []

with open(path, "r") as f_read, open("Data/datapoints_new.txt", "w") as f_write:
    f_write.write("Pokemon list\n\n")
    for quote in f_read:
        if quote != "":
            f_write.write(f"{quote}\n")
            
# nedan sorterar listan i datapoints, för att få ut 0 = pichu och 1 = pikachu.
pichu = []
pikachu = []

with open("Data/datapoints_new.txt", "r") as list:
    for line in list:
        line_separate = line.strip()
        if line_separate:
            text_split = line_separate.split(",")

            try:
                width = round(float(text_split[0].strip()), 2)
                hight = round(float(text_split[1].strip()), 2)
                label = int(text_split[2].strip())

                if label == 0:
                    pichu.append([width, hight, label])
                elif label == 1:
                    pikachu.append([width, hight, label])
            except ValueError:
                print(f"Wrong in lines in the loop 'try' for float and int.")
                
import matplotlib.pyplot as plt
pichu_x = [x[0] for x in pichu]
pichu_y = [y[1] for y in pichu]
pikachu_x = [x[0] for x in pikachu]
pikachu_y = [y[1] for y in pikachu]

plt.title("Pikachu and Pichus width and hight. Pikachu as Purple, Pichu as pink")
plt.xlabel("Pikachu and Pichus X variable")
plt.ylabel("Pikachu and Pichus Y variable")
plt.scatter(pichu_x, pichu_y, marker="*", color="pink")
plt.scatter(pikachu_x, pikachu_y, marker="*", color="purple")
plt.show()

# Test points

path_test = "Data/testpoints.txt" 

with open(path_test, "r") as f:
    test_points = f.read()

with open("Data/testpoints.txt", "r") as test_list:
    for line in test_list:
        line_separate_test = line.strip()
        if line_separate_test:
            text_split_test = line_separate_test.split(",")
        # print(text_split_test)

point1 = np.array((25, 24.2, 22, 20.5))
point2 = np.array((32, 31.5, 34, 34))
distance = np.linalg.norm(point1 - point2)
print(distance)

import matplotlib.pyplot as plt

plt.title("The classification for the nearest point")
plt.scatter(pichu_x, pichu_y, marker="*", color="pink")
plt.scatter(pikachu_x, pikachu_y, marker="*", color="purple")
plt.scatter(point1, point2, marker="X", color="green")
plt.show()