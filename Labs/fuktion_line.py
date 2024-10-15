import csv
import matplotlib.pyplot as plt
import pandas as pd

x = []
y = []
k = 1
m = 0
with open ("Data/unlabelled_data.csv") as file:
    lines = csv.reader(file)
    for row in lines:
        x.append((float(row[0])))
        y.append((float(row[1])))

def line_position(x, y, k, m):
    above = []
    below = []
    for i in range(len(x)):
        if y[i] > k * x[i] + m:         #y = kx + m
            above.append((x[i], y[i]))
        else:
            below.append((x[i], y[i]))
    return above, below

above, below = line_position(x, y, k, m)
line = [k * xi + m for xi in x]

# Plotta punkterna i olika färger
plt.scatter(x, y, c=['blue' if (xi, yi) in above else 'red' for xi, yi in zip(x, y)] )
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Seperated points")
plt.plot(x, line, color = "green")
plt.show()


# Spara data till en ny CSV-fil
with open('labelled_data.csv', 'w') as f:
    categories = [0 if (xi, yi) in above else 1 for xi, yi in zip(x, y)]
    sorted_categories = sorted(zip(x, y, categories), key=lambda x: x[2])
    for (x, y, category) in sorted_categories:
        f.write(f"{x}, {y}, {category}" '\n')



