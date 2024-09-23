import numpy as np
import matplotlib.pyplot as plt

# Initialize random number generator
rng = np.random.default_rng()

def count_six_and_print(dice_rolls):
    num_six = []  # Store the six counts, as in your original code
    
    # Simulate dice rolls
    for _ in range(dice_rolls):
        dice = rng.integers(1, 7)  # Get random integers between 1 and 6
        if dice == 6:
            num_six.append(dice)
    
    # Print the number of sixes
    print(f"Number of sixes for {dice_rolls} rolls: {len(num_six)}")
    print(f"The probability of getting a sex in {dice_rolls} is: {len(num_six) / dice_rolls}")
    print()
    print()
    # Return the probability
    return len(num_six) / dice_rolls

# List of dice rolls for each test
rolls_list = [10, 100, 1000, 10000, 100000, 1000000]

# Store the calculated probabilities
probabilities = [count_six_and_print(rolls) for rolls in rolls_list]

# Plotting the probabilities
plt.plot(rolls_list, probabilities, marker='o', linestyle='-', color='b', label='Probability of rolling a 6')
plt.axhline(y=1/6,)
plt.xscale('log')  # Use logarithmic scale for x-axis
plt.xlabel('Number of Dice Rolls')
plt.ylabel('Probability')
plt.title('Probability of Rolling a Six vs Number of Dice Rolls')
plt.legend()
plt.grid(True)
plt.show()