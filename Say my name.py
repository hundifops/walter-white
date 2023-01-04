# Say my name. You have to input the exact wording from the hit TV show *Breaking Bad*, or else you lose :(

scene = print("You've been killed by the heisenburg")

text = input("Who the hell are you? ")
if text == ("You know. You all know exactly who I am. Say my name."):
    print("Do what? [Declan says, humored] I don't... I don't have a damn clue who the hell you are ")
else:
    scene

text = input()
if text == "Yeah, you do. I'm the cook. I'm the man who killed Gus Fring.":
    print("Bullshit. Cartel got Fring.")
else: 
    scene

text = input()
if text == "Are you sure?":
    print("[Declan looks at Mike and Mike shakes his head]")
else:
    scene

text = input()
if text == "That's right. Now. Say my name.":
    print("[Quietly]... Heisenburg")
else:
    scene

text = input()
if text == "You're God damn right":
    print("You then get shot in the head by Heisenburg, the man who bombed a nursing home :-<")
else:
    scene