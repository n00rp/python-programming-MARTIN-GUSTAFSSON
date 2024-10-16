 

 ## Intro

The following program reads in coordinates to calculate if they are above or below the line.

The program is based on a straight line equation (Y = KX + M) that goes through the origo.

To use the program, you can either load your own file (in this case, a CSV file) with minimal code changes. Alternatively, you can add an input function where you can manually enter points to classify them yourself.

The program will classify the point graphically using a scatter plot in either red or blue depending on whether the point is above or below the line. All points entered will be classified by the program and be written to a separate CSV file, where each point will receive a classification of 0 if it is above the line and 1 if it is below the line.

## Förklaring av programmets delar

## 1 
Första delen av programmet läser in samtliga punkter, i orginalet genom en CSV-fil och delar upp dessa i X och Y kordinater. 

## 2 
Programmet använder sedan dessa i en fukntionen (def line_position) för att beräkna om respektive punkt ligger ovanför, eller under linjen.

## 3 
Programmet tar sedan samtliga punkter och plottar dessa med en scatter-plot samt drar en linje och märker samtliga punkter beroende på position.

## 4 
Sista delen av programmet lägger samtliga punkter i en ny CSV-fil och märker dem med en 0 eller en 1 beroende på positionen.