import random as rng
user_score = 0

print(f"Please choose a difficulty level.")
print(f"1 - Easy")
print(f"2 - Medium")
print(f"3 - Hard")

difficulty = int(input(f"Choose a difficulty setting for this excercise (1-3): "))


while True:

    if difficulty == "1":
        x = rng.randint(2, 2)
        y = rng.randint(2, 2)
    if difficulty == "2":
        x = rng.randint(3, 5)
        y = rng.randint(3, 5)
    if difficulty == "3":
        x = rng.randint(1, 10)
        y = rng.randint(1, 10)

    user_input = int(input(f"What is {x} x {y}?. "))
    if user_input == x*y:
        print(f"Good work")
        user_score += 1    
    else:
        print(f"{x*y} is the correct answer")
    print(f"Your score is now {user_score}")    
    play_again = input(f"Do you want to play again? (y / n): ")
    if play_again != "y":
        print(f"Thank you for playing, have a nice day!")
        break