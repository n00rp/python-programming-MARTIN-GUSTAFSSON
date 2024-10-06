import csv
import matplotlib.pyplot as plt



cordinates = []
with open ("Data/unlabelled_data.csv") as file:
    lines = csv.reader(file)
    for row in lines:
        cordinates.append((float(row[0]), float(row[1])))
x = [x[0] for x in cordinates]
y = [y[1] for y in cordinates]


#Dra linje i grafen
x_medium = sum(x)/len(x)
y_medium = sum(y)/len(y)
standardavvikelse = sum((x - x_medium) * (y - y_medium) for x, y in zip(x, y)) /len(x)
varians = sum((x - x_medium)**2 for x in x) / len(x)
k = standardavvikelse/varians 
m = 0  #y = kx + m


plt.scatter(x, y, s=12, color = "blue")
line = [k * xi + m for xi in x]
plt.plot(x, line, color = "red")
plt.scatter(0, 0, s = 90, color = "green", marker = "*")
plt.show()  