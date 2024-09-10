weight = int(input(f"Please enter the weight of your bag (kg): "))
length = int(input(f"Please enter the dimensions of your bag length)"))
width = int(input(f"Please enter the dimensions of your bag width )"))
height = int(input(f"Please enter the dimensions of your bag height: )"))

def dimensions(length, width, height):
    if ((length < 55 and width < 40 and height < 23)):
        return True
    else:
        return False
def bag_weight(weight):
    if weight <= 8:
        return True
    else:
        return False
if bag_weight and dimensions(bag_weight, dimensions):
    print(f"Your bag is okay, have a nice trip!")
else:
    print(f"Your bag is not up to code, please check paramaters")
