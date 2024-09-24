

path = "../Data/datapoint.txt"

with open(path, "r") as f:
    text = f.read()

print(repr(text))