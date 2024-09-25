
path = "Data/datapoints.txt"

with open(path, "r") as f:
    text = f.read()

print(repr(text))

import re

quotes = []

with open(path, "r") as f_read, open("Data/datapoints_clean.txt", "w") as f_write:
    f_write.write("Pokémon list\n\n")
    for quote in f_read:
        #quote = quote.strip(" \n")
        #quote = re.sub(r" +", " ", quote)
        if quote != "":
            f_write.write(f"{quote}\n")

with open("Data/datapoints_clean.txt", "r") as type:
    pokemon_type = None




        
            
                             