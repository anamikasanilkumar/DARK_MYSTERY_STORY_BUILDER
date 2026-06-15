import random
from colorama import init,Fore,Style

init(autoreset=True)

templates=[
   
    """
    After receiving a strange letter,a {adjective} {character} entered the abandoned house near the {place}.Inside,they discovered a {item} hidden beneath the floorboards.The moment they tried to {action},the walls echoed with whispers.
   
    A cold wind swept through the halls as shadowy figures appeared in every mirror.
   
    Suddenly the light went out.
    
    When the {character} finally reached the basement,they uncovered the terrible truth:
   
    the house had been hiding the spirits of missing villagers for decades.
    
    Using the {item}, they managed to break the curse before sunrise.
   
    As dawn arrived,the abandoned house collapsed into silence,leaving the {character} forever {emotion}.

   """,

  """
    A {character} became trapped inside an abandoned mansion beside the {place}.Every room contained clues about a missing {item}.
    
    While attempting to {action},they discovered secret messages written behind the walls.
    
    Footsteps echoed upstairs even though nobody else was inside.
    
    Near midnight,a hidden door slowly opened by itself.
    
    Behind it stood the ghost of a child guarding the truth about the mansion's dark past.
    
    The {character} solved the mystery just before sunrise and escaped the mansion alive,though they remained deeply {emotion} for the rest of their life.
    
    """,
]
adjectives=[
    "terrified",
    "silent",
    "cursed",
    "unknown",
    "lonely"
    ]
characters=[
    "student",
    "detective",
    "boy",
    "girl",
    "photographer"
]
places=[
    "abandoned village",
    "foggy forest",
    "silent lake",
    "old graveyard"
]
items=[
    "broken photograph",
    "music box",
    "bloodstained diary",
    "old cassette tape",
    "rusted key"
]
actions=[
    "solve the hidden puzzle",
    "escape before midnight",
    "follow the whispering voice",
    "unlock the basement door",
    "find the missing key"
]
emotions=[
    "speechless",
    "terrified",
    "confused",
    "suspicious",
    "emotionally broken"
]
def get_input(prompt,word_bank):
    print( Fore.RED+f"\nsuggestions:{','.join(random.sample(word_bank,3))}")
    user_input=input(f"{prompt}:").strip()

    if user_input=="":
     random_word=random.choice(word_bank)
     print(Fore.GREEN+f"(Using random word:{random_word})")
     return random_word
    
    return user_input

def story_building(mode):
   template=random.choice(templates)
   print( Fore.MAGENTA+"\n Fill in the story blanks")
   print(Fore.MAGENTA+"press enter for random words")

   if mode=="1":
      adjective=get_input("Enter the adjective",adjectives)
      character=get_input("Enter the character",characters)
      place=get_input("Enter the place",places)
      item=get_input("Enter the item",items)
      action=get_input("Enter the action",actions)
      emotion=get_input("Enter the emotion",emotions)
   else:
      adjective=random.choice(adjectives)
      character=random.choice(characters)
      place=random.choice(places)
      item=random.choice(items)
      action=random.choice(actions)
      emotion=random.choice(emotions)

   story=template.format(
         adjective=adjective,
         character=character,
         place=place,
         item=item,
         action=action,
         emotion=emotion
        )
   return story
   
def save_story(story):
   filename="abandoned_house.txt"
   with open(filename,"a")as file:
       file.write(story+"\n\n")

   print(Fore.GREEN+f"\n story saved to'{filename}'")

def main():
   print(Fore.RED+"="*50)
   print(Fore.WHITE+Style.BRIGHT+f"🔮 DARK MYSTERY STORY BUILDER")
   print(Fore.RED+Style.BRIGHT+f"="*50)

   while True:
      print(Fore.CYAN+f"\n Choose An Option:")
      print(Fore.WHITE+"1.Build a story manually")
      print(Fore.WHITE+"2.Generate random story")
      print(Fore.WHITE+"3.Quit")

      choice=input(Fore.RED+"\nEnter choice (1/2/3):").strip()

      if choice in ("1","2"):
         story=story_building(choice)

         print(Fore.RED+Style.BRIGHT+f"\n"+"="*50)
         print(Fore.RED+Style.BRIGHT+f"📖 YOUR STORY")
         print(Fore.RED+Style.BRIGHT+f"="*50)

         print(f"\n{story}\n")

         save=input(Fore.RED+"👤 Do you want to save this story ?(yes/no):").lower()
         if save=="yes":
            save_story(story)
      elif choice=="3":
            print(Fore.RED+"\n👋GOOD BYE... And Stay Away From The Abandoned House.")
            break
      else:
            print(Fore.RED+"\n Invalid Choice.Try Again.")

if __name__=="__main__":
    main()


