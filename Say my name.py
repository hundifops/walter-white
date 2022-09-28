# Say my name

from os import kill


text = input("Who the hell are you? ")
if text == ("You know. You all know exactly who I am. Say my name."):
    print("Do what? I don't... I don't have a damn clue who the hell you are ")
else:
    print("Scene failed")

text = input()
if text == "Yeah, you do. I'm the cook. I'm the man who killed Gus Fring.":
    print("Bullshit. Cartel got Fring.")
else: 
    print("Scene failed")

text = input()
if text == "Are you sure?":
    print("[Declan looks at Mike and Mike shakes his head]")
else:
    print("Scene failed")

text = input()
print("[Quietly]... Heisenburg")

text = input()
print("You then get shot in the head by Heisenburg, the man who bombed a nursing home :-<")