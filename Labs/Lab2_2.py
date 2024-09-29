import numpy as np
import matplotlib.pyplot as plt

def read_data_from_file(filename):
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    return data

def classify_new_point(data, new_point):
    # Beräkna euklidiska avstånden
    distances = np.linalg.norm(data[:, :2] - new_point, axis=1)
    # Hitta de närmsta grannarna
    indices = np.argsort(distances)[:3]
    # Hitta klasserna
    labels = data[indices, 2]
    # Kontrollera att det finns förekomster av varje klass
    if np.any(labels == "Pichu") and np.any(labels == "Pikachu"):
        # Klassificera den nya datapunkten
        predicted_label = np.bincount(labels.astype(int)).argmax()
        # Omvandla till sträng
        if predicted_label == 0:
            return "Pichu"
        else:
            return "Pikachu"
    else:
        return "Okänd klass"

def plot_data_and_classification(data, new_point, predicted_label):
    # Plotta datan
    pichu_data = data[data[:, 2] == "Pichu"]
    pikachu_data = data[data[:, 2] == "Pikachu"]
    plt.scatter(pichu_data[:, 0], pichu_data[:, 1], c='b')
    plt.scatter(pikachu_data[:, 0], pikachu_data[:, 1], c='r')
    # Plotta den nya datapunkten
    plt.scatter(new_point[0], new_point[1], c='g', marker='x')
    # Plotta klassificeringen
    plt.annotate(predicted_label, (new_point[0], new_point[1]))
    plt.xlabel('Bredd (cm)')
    plt.ylabel('Höjd (cm)')
    plt.title('Klassificering av Pichu och Pikachu')
    plt.show()

def main():
    filename = 'koordinater.txt'  # byt ut mot din filnamn
    data = read_data_from_file(filename)
    new_point = np.array([20, 30])  # byt ut mot din nya datapunkt
    predicted_label = classify_new_point(data, new_point)
    plot_data_and_classification(data, new_point, predicted_label)

if __name__ == "__main__":
    main()