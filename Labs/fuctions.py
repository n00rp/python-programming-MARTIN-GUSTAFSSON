def euclidean_distance(point1, point2):
    # Ensure both points have the same dimensions
    assert len(point1) == len(point2), "Points should have the same dimensions."
    
    # Compute the Euclidean distance
    distance = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5
    return distance

def find_neighbors(X_train, query_point, k):

    distances = []
      # Calculate distance from the query point to each point in the training set
    for i, data_point in enumerate(X_train):
        distance = euclidean_distance(query_point, data_point)
        distances.append((i, distance))
    
    # Sort distances in ascending order
    distances.sort(key=lambda x: x[1])
    
    # Get indices of the 'k' nearest neighbors
    neighbors = [index for index, _ in distances[:k]]
    return neighbors

def predict(X_train, y_train, query_point, k):

    # Find the k nearest neighbors
    neighbors = find_neighbors(X_train, y_train, query_point, k)
    neighbor_labels = [y_train[i] for i in neighbors]
    
    # Count occurrences of each label among neighbors
    label_counts = {}
    for label in neighbor_labels:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    
    # Get the label with the highest count
    predicted_class = max(label_counts, key=label_counts.get)
    return predicted_class

def find_neighbors(X_train, query_point, k):

    distances = []
    
    # Calculate distance from the query point to each point in the training set
    for i, data_point in enumerate(X_train):
        distance = euclidean_distance(query_point, data_point)
        distances.append((i, distance))
    
    # Sort distances in ascending order
    distances.sort(key=lambda x: x[1])
    
    # Get indices of the 'k' nearest neighbors
    neighbors = [index for index, _ in distances[:k]]
    return neighbors


def predict(X_train, y_train, query_point, k):

    neighbors = find_neighbors(X_train, y_train, query_point, k)
    neighbor_labels = [y_train[i] for i in neighbors]
    
    # Count occurrences of each label among neighbors
    label_counts = {}
    for label in neighbor_labels:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    
    # Get the label with the highest count
    predicted_class = max(label_counts, key=label_counts.get)
    return predicted_class


import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(file_name):
    # Load the dataset with semicolon delimiter
    data = pd.read_csv(file_name, delimiter=';')
    return data

def split_data(data):
    # Extract features and labels
    X = data.drop('quality', axis=1)
    y = data['quality']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    return X_train, X_test, y_train, y_test

def fit_model(X_train, y_train, k = 5):
    # Implement KNN classifier
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Predict on the train set
    train_preds = knn.predict(X_train)

    # Calculate and return accuracy on train set
    train_accuracy = accuracy_score(y_train, train_preds)
    return train_accuracy, knn


def test_model(model, X_test, y_test):
    # Predict on the test set
    test_preds = model.predict(X_test)

    # Calculate and return accuracy on test set
    test_accuracy = accuracy_score(y_test, test_preds)
    return test_accurac