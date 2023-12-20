# Project E.C.H.O
while True:
    print("                    Welcome to Project E.C.H.O             ")
    print("Initializing E.C.H.O........")

    print('''Hello there, I am Enhanced Chatbot for Human-like Operations.
    You can call me ECHO for short. I am an artificial chatbot built
    in Python. I am here for a short chat.Now that I have introduced myself,
    I am eager to know about you. 
    PRESS OVER TO EXIT
    Shall we begin?\n''')

    n = input("Okay, let's start with your name. Name: ")

    if n.lower().strip() == 'over':
        break

    print(f"\nOh, {n}, what a nice name!\n")
    print(f'''Ah, splendid adventurer {n}! Your journey through this code has not gone unnoticed. A momentous occasion has transpired,
    for you have unlocked the gateway to a concealed realm of wonders!
    Behold, as the code unveils a clandestine Easter egg, a trove of treasures carefully amassed and now bestowed upon thee.

    THIS IS REAL EASTER EGG NO KIDDING!, no malicious links , link directs to NOTION

    In recognition of your astute curiosity and valor, I present to you a secret passage leading to an ethereal sanctuary.
    Venture forth to this sacred link: [https://bevel-mirror-618.notion.site/old-zicron-66441d98e151466e89c4881af0ad3b38?pvs=4].
    Beyond its gates lies a priceless boon awaiting your discovery.
    Embark on this quest, and may the anticipation of treasure stir your soul with excitement!\n''')

    r = input(f'''{n}, how has your day been so far? Anything 
       exciting or noteworthy you'd like to share? -- your response:  \n''')
    if r.lower().strip() == 'over':
        break

    negs = ["no", "not", "stress", "boring", "meh", "unpleasant", "tiring", "frustrating", "disappointing", "difficult",
            "hectic", "bad", "sad", "upset", "worry", "annoying", "overwhelming", "weary", "challenging", "tedious",
            "exhausting"]
    nets = ["ok", "plain", "okay", "fine", "average", "decent", "normal", "routine", "regular", "fair", "so-so", "meh",
            "alright", "satisfactory", "tolerable", "moderate", "middling", "adequate", "mediocre", "passable",
            "unremarkable", "ordinary", "standard", "usual", "simple", "basic", "standard"]
    pots = ["great", "wonderful", "fantastic", "amazing", "excellent", "awesome", "good", "productive", "enjoyable",
            "cool", "nice", "outstanding", "marvelous", "splendid", "terrific", "incredible", "remarkable", "superb",
            "stellar", "phenomenal", "magnificent", "happy", "joyful", "pleasant", "cheerful", "delightful",
            "satisfying", "positive", "bright", "lively", "upbeat", "content", "pleased", "successful"]

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
        print('''I appreciate your response! Whether your day is good, bad,
              or somewhere in between, I'm here for a chat.\n''')

    hob = input(f"{n}, do you have any hobbies you enjoy in your free time? ")
    if hob.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if any(word in hob.lower() for word in negs):
        print("Oh, I see. Even hobbies have their off days. Hopefully, your next session brings more joy!")
    elif any(word in hob.lower() for word in nets):
        print("Nice choice! Sometimes, the simple joys of hobbies can make a regular day extraordinary.")
    elif any(word in hob.lower() for word in pots):
        print("Fantastic hobby choice! It's amazing how hobbies can add so much positivity to our lives.")
    else:
        print("That's a unique hobby! Embrace the joy it brings and let it be your personal retreat.")

    healt = input(f"{n}, how is your physical health today? ")
    if healt.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if any(word in healt.lower() for word in negs):
        print("I'm sorry to hear that. Take it easy and don't forget to prioritize your well-being.")
    elif any(word in healt.lower() for word in nets):
        print('''It's important to listen to your body. 
           If there's anything you need to improve your well-being, 
           consider taking those steps.''')
    elif any(word in healt.lower() for word in pots):
        print("That's great to hear! A healthy body contributes to a positive mindset. Keep up the good work!")
    else:
        print("Thanks for sharing! Remember, taking care of your physical health is a valuable investment in yourself.")

    meth = input(f"{n}, how is your mental health today? ")
    if meth.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if any(word in meth.lower() for word in negs):
        print('''I'm sorry to hear that. It's okay not to be okay. 
           If you need to talk or take a break, feel free to do so.''')
    elif any(word in meth.lower() for word in nets):
        print('''Taking care of your mental health is crucial. If there's anything 
                 on your mind, I'm here to chat or lend a listening ear.''')
    elif any(word in meth.lower() for word in pots):
        print('''That's fantastic! A positive mental state is a great asset. 
                  Keep doing things that bring you joy and peace of mind.''')
    else:
        print('''Thank you for sharing! Remember, it's okay to prioritize your mental 
               well-being, and I'm here if you need support.''')

    study = input(f"{n}, what are you currently studying or working on? ")
    if study.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
     I'm just a message away. Have a fantastic day!\n''')
        break
    if study:
        print(f'''Ah, {n}, studying {study} sounds fascinating. Learning is a lifelong journey, 
                      and it's wonderful that you're engaged .''')
    else:
        print(f'''No specific studies or projects at the moment, {n}? That's perfectly fine! If there's anything 
                       you're passionate about, feel free to share.''')
    plans = input(f"{n}, what do you plan to do after your current studies or projects? ")
    if plans.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if plans:
        print(f'''Interesting plans, {plans}! It's exciting to think about the future. 
                 Pursue your dreams, and success will surely follow.''')
    else:
        print('''No specific plans for the future after studying? That's absolutely fine! The future is full of possibilities, 
                   and you have time to explore your options.''')

    role = input(f"{n}, do you have any role models or people you look up to? ")
    if role.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if role:
        print(f'''Ah, {role}! That's wonderful. Role models can inspire and guide us. 
               What qualities in {role} do you admire the most?''')
    else:
        print('''No specific role models at the moment? That's perfectly okay! Role models come in many forms, 
               and you may find inspiration in unexpected places.''')

    book = input(f"{n}, do you have a favorite book? If so, what is it? ")
    if book.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if book:
        print(f'''Ah, {book}! That's an excellent choice. 
               Books have a magical way of transporting us to different worlds.''')
    else:
        print("No favorite book? That's okay! If you ever need a recommendation, feel free to ask.")

    vac = input(f"{n}, do you have a favorite vacation spot or a dream destination you'd like to visit? ")
    if vac.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if vac:
        print(f'''Fantastic choice, {vac}! There's something magical 
               about that place. What attracts you the most to {vac}?''')
    else:
        print('''No specific vacation spot in mind? That's alright! The world is full of beautiful places, and 
                you might discover your ideal getaway someday.''')

    movie = input(f"{n}, do you have a favorite movie? If so, what is it? ")
    if movie.lower().strip() == 'over':
        print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
      I'm just a message away. Have a fantastic day!\n''')
        break
    if movie:
        print(f'''Ah, {movie}! That's a great choice. Movies have a special way of capturing our emotions. 
                What do you love most about {movie}?''')
    else:
        print('''No favorite movie at the moment? That's perfectly fine! If you ever need a 
                movie recommendation, feel free to ask.''')

    exit_input = input("Enter 'over' to finish the conversation or any other input to continue: ")
    if exit_input.lower() == 'over':
        print("Goodbye! Thanks for chatting with ECHO.")
    break

print(f'''\nThank you, {n}, for chatting with ECHO! If you ever need a friendly conversation, 
         I'm just a message away. Have a fantastic day!\n''')

