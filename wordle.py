import random
words = [
    "crane", "blitz", "sword", "plant", "grace", "flint", "march", "bound", "skate", "pride",
    "clamp", "trend", "vapor", "quick", "jumpy", "frost", "blend", "chart", "speak", "drive",
    "flock", "stamp", "brick", "ghost", "waltz", "zebra", "yacht", "prank", "smoke", "glare",
    "thorn", "cabin", "dwarf", "spice", "mound", "flare", "joint", "brush", "crown", "phase",
    "light", "frame", "sound", "grasp", "knife", "storm", "badge", "clown", "fresh", "adorn",
    "quilt", "shark", "tiger", "vixen", "broad", "flame", "crisp", "jokes", "wrist", "punch",
    "sling", "mirth", "globe", "track", "spare", "blown", "draft", "honey", "squad", "prism",
    "fable", "charm", "siren", "tulip", "vigor", "zesty", "amber", "slope", "grain", "fetch",
    "mango", "piano", "risky", "tango", "woven", "unity", "ocean", "raven", "solar", "tiger",
    "umbra", "adore", "bloom", "candy", "delta", "eager"
]
choose = random.randint(0, 99)
wordle = words[choose]
wordle1 = wordle[0]
wordle2 = wordle[1]
wordle3 = wordle[2]
wordle4 = wordle[3]
wordle5 = wordle[4]

for i in range(1, 11):
    print(f"You're on attempt {i}/10 ")
    guess = input("Enter 5 letters to guess the word (The same letter cannot appear twice in this word) ")
    letter1 = guess[0]
    letter2 = guess[1]
    letter3 = guess[2]
    letter4 = guess[3]
    letter5 = guess[4]
    if guess == wordle:
        print("You guessed it!")
        break
    else:
        if letter1 == wordle1:
            print(f"{letter1} is in this word and in the right place")
        elif letter1 == wordle2 or letter1 == wordle3 or letter1 == wordle4 or letter1 == wordle5:
            print(f"{letter1} is in this word and in the wrong place")
        else:
            print(f"{letter1} is not in this word")
            
        if letter2 == wordle2:
            print(f"{letter2} is in this word and in the right place")
        elif letter2 == wordle1 or letter2 == wordle3 or letter2 == wordle4 or letter2 == wordle5:
            print(f"{letter2} is in this word and in the wrong place")
        else:
            print(f"{letter2} is not in this word")
            
        if letter3 == wordle3:
            print(f"{letter3} is in this word and in the right place")
        elif letter3 == wordle1 or letter3 == wordle2 or letter3 == wordle4 or letter3 == wordle5:
            print(f"{letter3} is in this word and in the wrong place")
        else:
            print(f"{letter3} is not in this word")
            
        if letter4 == wordle4:
            print(f"{letter4} is in this word and in the right place")
        elif letter4 == wordle1 or letter4 == wordle2 or letter4 == wordle3 or letter4 == wordle5:
            print(f"{letter4} is in this word and in the wrong place")
        else:
            print(f"{letter4} is not in this word")
            
        if letter5 == wordle5:
            print(f"{letter5} is in this word and in the right place")
        elif letter5 == wordle1 or letter5 == wordle2 or letter5 == wordle3 or letter5 == wordle4:
            print(f"{letter5} is in this word and in the wrong place")
        else:
            print(f"{letter5} is not in this word")
    print("")
print(f"The word was {wordle}")
