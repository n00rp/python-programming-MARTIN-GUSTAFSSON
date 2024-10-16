 

 ## Intro

The following program reads in coordinates to calculate if they are above or below the line.

The program is based on linear algebra (Y = KX + M) that goes through the origo.

To use the program, you can either load your own file (in this case, a CSV file) with minimal code changes. Alternatively, you can add an input function where you can manually enter points to classify them yourself.

The program will classify the point graphically using a scatter plot in either red or blue depending on whether the point is above or below the line. All points entered will be classified by the program and be written to a separate CSV file, where each point will receive a classification of 0 if it is above the line and 1 if it is below the line.

# 2: Explanation of the Program's Parts
#### 1: The first part of the program reads in all points, originally through a CSV file, and separates them into X and Y coordinates.

#### 2: The program then uses these in a function (def line_position) to calculate whether each point is above or below the line.

#### 3: The program then takes all points and plots them with a scatter plot, draws a line, and marks all points depending on their position.

#### 4: The final part of the program puts all points into a new CSV file and marks them with a 0 or a 1 depending on their position.