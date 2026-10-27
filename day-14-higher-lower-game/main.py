from game_data import data
import art
import random

def print_information(person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}."

score = 0

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

if followers_a > followers_b:
    winner = "a"
else:
    winner = "b"

#print("DEBUG WINNER: " + winner)
#print("DEBUG USER_CHOICE:" + user_choice)

if user_choice == winner:
    score += 1
    print("That's correct! Current score: " + str(score))
else:
    print("You lose! Final score: " + str(score))