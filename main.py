#timer
import time
# Function to force non-empty input
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Oops! Please enter something.")

# Introduction
name = get_non_empty_input("Hello! Welcome to Reilan's Madlib's, what is your name: ")

# Madlib 1
print("Fill out the questions provided to generate your madlib!")
print("A Mysterious Discovery Madlib")
place = get_non_empty_input("Place: ")
adjective = get_non_empty_input("Adjective: ")
noun = get_non_empty_input("Noun: ").upper()
adjective2 = get_non_empty_input("Adjective2: ")
animal = get_non_empty_input("Animal: ")
adjective3 = get_non_empty_input("Adjective3: ")
sound = get_non_empty_input("Sound: ")
noun2 = get_non_empty_input("Noun 2: ").upper()
adjective4 = get_non_empty_input("Adjective4: ")
object = get_non_empty_input("Object: ")

print("\nGenerating madlib...") #Gives a countdown to generate madlib
time.sleep(5)

print(f"\nWhile exploring {place}, I stumbled upon a {adjective} {noun} buried in the ground. As soon as I touched it, a {adjective2} {animal} appeared and made a {sound} sound! It grabbed a {object} and waved it around. Suddenly, the {noun2} began to glow, and I knew this was going to be a {adjective4} day!")
print(f"Here is your madlib, {name}!")

# Ask for madlib 2
madlib2 = get_non_empty_input("Would you want to do madlib #2? Y or N: ").lower()
if madlib2 == "y":
    print("\nLoading next adventure...") #Creates waiting time
    time.sleep(5)
    print("\nThe Wildest Road Trip Madlib")
    ffriendname = get_non_empty_input("Friend's name: ").upper()
    pplace = get_non_empty_input("Place: ")
    aadjective = get_non_empty_input("Adjective: ")
    ppluralnoun = get_non_empty_input("Plural noun: ").upper()
    aadjective2 = get_non_empty_input("Adjective 2: ")
    aadjective3 = get_non_empty_input("Adjective 3: ")
    aanimal = get_non_empty_input("Animal: ")
    nnoun = get_non_empty_input("Noun: ").upper()
    ppluralnoun2 = get_non_empty_input("Plural noun 2: ").upper()
    pplace2 = get_non_empty_input("Place 2: ")
    aadjective4 = get_non_empty_input("Adjective 4: ")
    ccelebname = get_non_empty_input("Celebrity name: ").upper()
    nnoun2 = get_non_empty_input("Noun: ").upper()
    ppluralnoun3 = get_non_empty_input("Plural noun 3: ").upper()

    print("\nGenerating madlib...") #Gives a countdown to generate madlib
    time.sleep(5)

    print("\nThe Wildest Road Trip Madlib")
    print(f"Last summer, my best friend {ffriendname} and I decided to take a road trip to {pplace}. We packed our {aadjective} bags, grabbed some {ppluralnoun}, and hit the road in our {aadjective2} car. Everything was going smoothly until a {aadjective3} {aanimal} suddenly ran across the highway! I swerved and accidentally knocked over a {nnoun}, causing a huge {ppluralnoun2} to spill everywhere. Panicked, we pulled over near a {pplace2}, hoping to find help. That’s when we met a {aadjective4} {ccelebname}, who was carrying a {nnoun2} and offered us advice. After a few {ppluralnoun3} and some deep breaths, we finally continued our journey, laughing at the crazy adventure we would never forget!")

elif madlib2 == "n":
    print(f"\nThanks for playing, {name}!")

else:
    print("\nOops! Please enter Y or N.")
