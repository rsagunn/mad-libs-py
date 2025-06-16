#scrpts
import time #Built in clock abt clocks, pausing, n timers
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()



# Function to force non-empty input
def get_non_empty_input(prompt): #Keep asking untill you input something.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Oops! Please enter something.")
        
def get_yes_no(prompt): # y or no question
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer
        print("Please enter Y or N.")


# Introduction
name = get_non_empty_input("Hello! Welcome to Reilan's Madlib's, what is your name: ")

# Madlib 1
print("Fill out the questions provided to generate your madlib!")
print("A Mysterious Discovery Madlib")
place = get_non_empty_input("Place: ")
adjective = get_non_empty_input("Adjective: ")
noun = get_non_empty_input("Noun: ").capitalize()
adjective2 = get_non_empty_input("Adjective2: ")
animal = get_non_empty_input("Animal: ")
adjective3 = get_non_empty_input("Adjective3: ")
sound = get_non_empty_input("Sound: ")
noun2 = get_non_empty_input("Noun 2: ").capitalize()
adjective4 = get_non_empty_input("Adjective4: ")
object = get_non_empty_input("Object: ")

print("\nGenerating madlib...") #Gives a countdown to generate madlib
time.sleep(5) # pauses code for 5 secs

discovery_story = (
    f"While exploring {place}, I stumbled upon a {adjective} {noun} buried in the ground. "
    f"As soon as I touched it, a {adjective2} {animal} appeared and made a {sound} sound! "
    f"It grabbed a {object} and waved it around. Suddenly, the {noun2} began to glow, "
    f"and I knew this was going to be a {adjective4} day!"
)
print(f"Here is your madlib, {name}!")
    
print(f"\n{discovery_story}")
save_choice = get_yes_no("\nWould you like to save this story as a file? Y or N: ")

if save_choice == "y":
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save your Madlib"
    )
    if file_path:  # If the user didn’t cancel
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(discovery_story)
        print("Story saved!")
        



# Ask for madlib 2
madlib2 = get_non_empty_input("Would you want to do madlib #2? Y or N: ").lower()
if madlib2 == "y":
    print("\nLoading next adventure...") #Creates waiting time
    time.sleep(3)
    print("\nThe Wildest Road Trip Madlib")
    ffriendname = get_non_empty_input("Friend's name: ").capitalize()
    pplace = get_non_empty_input("Place: ")
    aadjective = get_non_empty_input("Adjective: ")
    ppluralnoun = get_non_empty_input("Plural noun: ").capitalize()
    aadjective2 = get_non_empty_input("Adjective 2: ")
    aadjective3 = get_non_empty_input("Adjective 3: ")
    aanimal = get_non_empty_input("Animal: ")
    nnoun = get_non_empty_input("Noun: ").capitalize()
    ppluralnoun2 = get_non_empty_input("Plural noun 2: ").capitalize()
    pplace2 = get_non_empty_input("Place 2: ")
    aadjective4 = get_non_empty_input("Adjective 4: ")
    ccelebname = get_non_empty_input("Celebrity name: ").capitalize()
    nnoun2 = get_non_empty_input("Noun: ").capitalize()
    ppluralnoun3 = get_non_empty_input("Plural noun 3: ").capitalize()

    print("\nGenerating madlib...") #Gives a countdown to generate madlib
    time.sleep(5)

    road_trip_story = (
    f"The Wildest Road Trip Madlib\n"
    f"Last summer, my best friend {ffriendname} and I decided to take a road trip to {pplace}. "
    f"We packed our {aadjective} bags, grabbed some {ppluralnoun}, and hit the road in our {aadjective2} car. "
    f"Everything was going smoothly until a {aadjective3} {aanimal} suddenly ran across the highway! "
    f"I swerved and accidentally knocked over a {nnoun}, causing a huge {ppluralnoun2} to spill everywhere. "
    f"Panicked, we pulled over near a {pplace2}, hoping to find help. That’s when we met a {aadjective4} {ccelebname}, "
    f"who was carrying a {nnoun2} and offered us advice. After a few {ppluralnoun3} and some deep breaths, "
    f"we finally continued our journey, laughing at the crazy adventure we would never forget!"
)

    
print(f"\n{road_trip_story}")
save_choice = get_yes_no("\nWould you like to save this story as a file? Y or N: ")

if save_choice == "y":
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save your Madlib"
    )
    if file_path:  # If the user didn’t cancel
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(road_trip_story)
        print("Story saved!")


elif madlib2 == "n":
    print(f"\nThanks for playing, {name}!")

else:
    print("\nOops! Please enter Y or N.")
