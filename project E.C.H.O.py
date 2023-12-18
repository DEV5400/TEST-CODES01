print("                    Welcome to Project E.C.H.O             ")
print("Initializing E.C.H.O........")

print('''Hello there, I am Enhanced Chatbot for Human-like Operations.
You can call me ECHO for short. I am an artificial chatbot built
in Python. I am here for a short chat. Now that I have introduced myself,
I am eager to know about you. Shall we begin?\n''')

n = input("Okay, let's start with your name. Name: ")
print(f"\nOh, {n}, what a nice name!\n")
print(f'''Ah, splendid adventurer {n}! Your journey through this code has not gone unnoticed. A momentous occasion has transpired,
 for you have unlocked the gateway to a concealed realm of wonders!
 Behold, as the code unveils a clandestine Easter egg, a trove of treasures carefully amassed and now bestowed upon thee.

THIS IS REAL EASTER EGG NO KIDDING!, no malicious links , link directs to NOTION

In recognition of your astute curiosity and valor, I present to you a secret passage leading to an ethereal sanctuary.
 Venture forth to this sacred link: [https://bevel-mirror-618.notion.site/old-zicron-66441d98e151466e89c4881af0ad3b38?pvs=4].
 Beyond its gates lies a priceless boon awaiting your discovery.
 Embark on this quest, and may the anticipation of treasure stir your soul with excitement!  \n''')

r = input(f'''{n}, how has your day been so far? Anything 
exciting or noteworthy you'd like to share? -- your response:  \n''')

negs = ["no", "not", "stress", "boring", "meh", "unpleasant", "tiring", "frustrating", "disappointing", "difficult", "hectic"]
nets = ["ok", "plain", "okay", "fine", "average", "decent", "normal", "routine", "regular", "fair", "so-so", "meh", "alright"]
pots = ["great", "wonderful", "fantastic", "amazing", "excellent", "awesome", "good", "productive", "enjoyable", "cool", "nice"]

for word in negs:
    if word in r.lower():
        print('''Sorry to hear that. Fear not, for even the stars giggle in the ancient night.
Your tough day? Just a subplot in life's grand comedy. 
Tomorrow's script awaits your comedic genius. 
Keep smiling; the punchlines get better\n''')
        break

for word in nets:
    if word in r.lower():
        print('''Got it. Grasp the mundane moments of this day, 
for in them lies the extraordinary potential to craft a 
life abundant with joy, purpose, and timeless memories.\n''')
        break

for word in pots:
    if word in r.lower():
        print('''That's wonderful to hear! May each day be merry and bright for you, 
and may happiness follow your every step. 
Wishing you a lifetime of sunny days and joyous moments that last forever.\n''')
        break

if r not in negs and r not in nets and r not in pots:
    print("I appreciate your response! Whether your day is good, bad, or somewhere in between, I'm here for a chat.\n")

hobby_input = input(f"{n}, do you have any hobbies you enjoy in your free time? ")
if any(word in hobby_input.lower() for word in negs):
    print("Oh, I see. Even hobbies have their off days. Hopefully, your next session brings more joy!")
elif any(word in hobby_input.lower() for word in nets):
    print("Nice choice! Sometimes, the simple joys of hobbies can make a regular day extraordinary.")
elif any(word in hobby_input.lower() for word in pots):
    print("Fantastic hobby choice! It's amazing how hobbies can add so much positivity to our lives.")
else:
    print("That's a unique hobby! Embrace the joy it brings and let it be your personal retreat.")
print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, I'm just a message away. Have a fantastic day!\n''')
