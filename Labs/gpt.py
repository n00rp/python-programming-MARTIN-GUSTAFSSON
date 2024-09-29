import numpy as np

# Funktionen för att läsa in datapunkterna på en fil
def read_data_from_file(file_path):
    cordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            lines = line.strip().split(',')
            if len(lines) < 3:
                continue
            features = []
            for x in lines[:-1]:
                try:
                    features.append(float(x))
                except ValueError:
                    break
            if len(features) == len(lines) - 1:
                label = int(lines[-1])
                cordinates.append((features, label))
    return cordinates

# Skapa en variabel för att läsa in datapunkterna från en fil
cordinates = read_data_from_file('Data/datapoints.txt')

# Skapa en lista med datapunkter och lables
data_points = []
for point in cordinates:
    features = point[0]
    label = point[1]
    data_points.append((features, label))

# Funktionen för att läsa in datapunkterna på en fil
def k_nn(data, new_point, k):
    # Beräkna avståndet mellan datapunkter
    distances = np.linalg.norm(data[:, 0] - new_point, axis=1)
    
    # Hitta de k närmaste grannarna
    indices = np.argsort(distances)[:k]
    
    # Rösta om etiketten
    labels = data[indices, 1]
    predicted_label = np.bincount(labels).argmax()
    
    return predicted_label

# Exempel på hur du kan använda funktionen
data = np.array([[23.4, 23], [12.3, 45], [34.5, 12], [45.6, 78]])  # Träningsdata
new_point = np.array([25.6, 34])  # Ny datapunkt
k = 3

predicted_label = k_nn(data_points, new_point, k)
print(predicted_label)