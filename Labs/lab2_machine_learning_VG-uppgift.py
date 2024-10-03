import random
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

accuracies = []
true_positives = []
false_negatives = []
false_positives = []
true_negatives = []

for _ in range(10):
    with open("python-programming-MARTIN-GUSTAFSSON/Data/datapoints.txt", 'r') as f:
        next(f)
        data = []
        for line in f:
            x, y, label = line.strip().split(',')
            data.append((x, y, label))

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

    pichu, pikachu = separate_data(data)

    random.shuffle(pichu)
    random.shuffle(pikachu)

    training_pichu = pichu[:50]
    training_pikachu = pikachu[:50]
    test_pichu = pichu[50:]
    test_pikachu = pikachu[50:]

    test_data = test_pichu + test_pikachu
    test_labels = [0] * len(test_pichu) + [1] * len(test_pikachu)

    train_data = []
    for point in training_pichu + training_pikachu:
        train_data.append([point[0], point[1]])
    labels = []
    for i in range(len(training_pichu)):
        labels.append(0)
    for i in range(len(training_pikachu)):
        labels.append(1)

    knn = KNeighborsClassifier(10) #Använt Sckit-learn dokumentation samt AI stöd för implementation och förstå vad den gör
    knn.fit(train_data, labels)

    predictions = knn.predict(test_data)

    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(test_labels)): #Tog hjälp från en GitHub för inspiration: https://github.com/ML4ITS/mtad-gat-pytorch/blob/main/eval_methods.py
        if test_labels[i] == 1 and predictions[i] == 1:
            TP += 1
        elif test_labels[i] == 0 and predictions[i] == 1:
            FP += 1
        elif test_labels[i] == 0 and predictions[i] == 0:
            TN += 1
        elif test_labels[i] == 1 and predictions[i] == 0:
            FN += 1

   

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    accuracies.append(accuracy)
    true_positives.append(TP)
    false_negatives.append(FN)
    false_positives.append(FP)
    true_negatives.append(TN)
mean_accuracy = sum(accuracies) / len(accuracies)
print(accuracies)
plt.plot(range(len(accuracies)), accuracies)
plt.xlabel('Iteration')
plt.ylabel('Noggrannhet')
plt.title('Noggrannhet över iterationer')
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.title("Accuracy for TP, FN, FP, TN över 10 iteration")
plt.legend()
plt.show()
print(f"Mean accuracy: {mean_accuracy*100}%")