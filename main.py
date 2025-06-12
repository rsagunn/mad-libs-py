#Introduction
name = input("Hello! Welcome to Reilan's Madlib's, what is your name: ")

#madlib var 1
print("Fill out the questions provided to generate your madlib!")
print("A Mysterious Discovery Madlib")
place = input("Place: ")
adjective = input("Adjective: ")
noun = input("Noun: ")
adjective2 = input("Adjective2: ")
animal = input("Animal: ")
adjective3 = input("Adjective3: ")
sound = input("Sound: ")
noun2 = input("Noun 2: ")
adjective4 = input("Adjective4: ")
object = input("Object: ")

#madlib 1 paragraph

print(f"While exploring {place}, I stumbled upon a {adjective} {noun} buried in the ground. As soon as I touched it, a {adjective2} {animal} appeared and made a {sound} sound! It grabbed a {object} and waved it around. Suddenly, the {noun2} began to glow, and I knew this was going to be a {adjective4} day!")
print(f"Here is your madlib, {name}!")
print("Would you want to do madlib #2? Y or N")

# Ask for madlib 2
madlib2 = input("Y or N: ").lower()
if "y":
    print("The Wildest Road Trip Madlib")
    ffriendname = input("Friends name: ")
    pplace = input("Place: ")
    aadjective = input("Adjective: ")
    ppluralnoun = input("Plural noun: ")
    aadjective2 = input("Adjective 2: ")
    aadjective3 = input("Adjective 3: ")
    aanimal = input("Animal: ")
    nnoun = input("Noun: ")
    ppluralnoun2 = input("Plural noun 2: ")
    pplace2 = input("Place 2: ")
    aadjective4 = input("Adjective 4: ")
    ccelebname = input("Celebrity name: ")
    nnoun2 = input("Noun: ")
    ppluralnoun2 = input("Plural noun 2: ")
    
    print("The Wildest Road Trip Madlib")
    print(f"Last summer, my best friend {ffriendname} and I decided to take a road trip to {pplace}. We packed our {aadjective} bags, grabbed some {ppluralnoun}, and hit the road in our {aadjective2} car. Everything was going smoothly until a {aadjective3} {aanimal} suddenly ran across the highway! I swerved and accidentally knocked over a {nnoun}, causing a huge {ppluralnoun2} to spill everywhere. Panicked, we pulled over near a {pplace}, hoping to find help. That’s when we met a {aadjective4} {ccelebname}, who was carrying a {nnoun2} and offered us advice. After a few {ppluralnoun3} and some deep breaths, we finally continued our journey, laughing at the crazy adventure we would never forget!")
    

elif "n":
    print(f"Thanks for playing, {name}!")