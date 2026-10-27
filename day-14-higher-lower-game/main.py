from game_data import data
import art
import random

def print_information(person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}."



contender_a = random.choice(data)
followers_a = contender_a["follower_count"]

contender_b = random.choice(data)
followers_b = contender_b["follower_count"]

print(art.logo)
print("Compare A: " + print_information(contender_a))
print(f"DEBUG FOLLOWERS FROM A: {contender_a["follower_count"]}")
print(art.vs)
print("Against B: " + print_information(contender_b))
print(f"DEBUG FOLLOWERS FROM B: {contender_b["follower_count"]}")
user_choice = input("Who has more followers? Type 'A' or 'B'").lower()

if user_choice == "a":
    if followers_a > followers_b:
        print("You win")
    else:
        print("You lose")