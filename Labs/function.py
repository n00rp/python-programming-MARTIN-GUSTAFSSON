file_name = 'Data/datapoints.txt'
import matplotlib.pyplot as plt
def open_file(file_name):
    with open(file_name, 'r') as file:
        next(file)
        return file.readlines()
    

def clean_data(data):
    cleaned_data = []
    for line in data:
        cleaned_line = line.strip().split(',')
        cleaned_data.append(cleaned_line)
    return cleaned_data

def scatter_plot(cleaned_data):
    x = []
    y = []
    for line in cleaned_data:
        x.append(float(line[0]))
        y.append(float(line[1]))
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')
    plt.show()


