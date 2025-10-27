from pdb import Restart

branch1 = ""
branch2 = ""
branch3 = ""
   
def validateAnswer(prompt, validAnswers):
    while True:
        answer = input(prompt)          #storing text from question as "prompt"
        if answer in validAnswers:      #checking if answer is valid
            return answer               #putting answer into "branchX" if statement
        else: 
            print("Please enter a valid number")    
                                
                            #intro   
print("""                       
    You're walking down the street when, down a small alley, you notice - for the first time - a small, gnarled wooden door, its weathered surface hinting at many decades, if not centuries, of existence. 
    A faint light shines through its cracked window, casting an amber glow on the cobblestones. You've walked this route home almost every day for years. Surely you would have noticed it before?""") #introduction

                            #Decision tree 1 (open the door) 
branch1 = validateAnswer("""
    1. You walk up to the door and try to open it.
    2. You continue home. Nothing good can come of a place like this.\n""", ["1","2"])

if (branch1 == "1"):        #Continuation of story (mirror) 
    print("""
    As your hand brushes the iron-wrought handle, cool and rough under your fingers, the door swings open with a creak, revealing a colorfully lit shop. 
    The air hums with an odd energy, filled with the scent of aged wood and strange spices. Shelves tower overhead, cluttered with all manner of items: bottles full of swirling, unusual liquids, 
    glittering clockwork contraptions that tick faintly, gnarled wooden knickknacks carved with cryptic runes, and collections of claws, feathers, horns, and other remnants that seem to have once belonged 
    to creatures you could only dream of. One item in particular catches your eye: an ornate mirror hanging on the wall, its frame bordered with silver and glinting gems. A voice startles you out of your 
    reverie: “See something you like, child?” 
    You look across the room to see a very small, ancient man staring at you over wire-rimmed glasses, his eyes sharp despite his stooped frame.\n""")

elif(branch1 == "2"):       #Neutral ending (go home)
    print("""
    You shake off the unease and continue your walk home, the alley fading behind you. The evening air is crisp, and your footsteps echo on the familiar path.
    You have a perfectly normal walk back home, just like any other day.\n""")
    quit()
   
        #Decision tree 2 (inside the shop)
branch2 = validateAnswer("""
    1. You ask the man about the shop.
    2. You touch the mirror's surface.
    3. You pocket the closest item and bolt for the door.\n""", ["1","2","3"])

if (branch2 == "1"):        #Neutral ending (listen to shopkeep)
    print("""
    As you ask the man about the shop, he launches into a monotonous drone about its ancient origins, detailing every merchant and spell that once thrived there. 
    The air, once thick with magic, seems to still, the glow fading as his voice fills the space. When you finally step outside, the sky has darkened, and you realize many hours have passed. 
    You return home weary but unharmed, the experience a strange blur, leaving you with a vague sense of time lost.\n""")
    quit()

elif (branch2 == "2"):      #Continuation of story (sphinx)
    print("""
    As you touch the mirror's surface, a sudden jolt pulls you forward, and the room spins into darkness. When the world stabilizes, you stand in a vast, stone chamber lit by flickering torches. 
    Before you sits a majestic sphinx, its lion body coiled and its human face gazing with piercing eyes. It speaks in a resonant voice, 
    'To leave, you must choose your path wisely. Answer my riddle or face my wrath.'
    
    Silver thread across the land
    Cannot be held by mortal hand
    Lipless mouth and bed of sand
    Speak my name is my command\n""")

elif (branch2 == "3"):      #Bad ending (steal pendant)
    print("""
    Your eyes dart to a small, engraved pendant glinting on a shelf. 
    You snatch it, your pulse racing as you turn to bolt for the door. The shopkeeper's voice rises in a sharp cry, “Thief!” but before you can reach the exit, 
    the door slams shut with a thunderous bang, sealing you inside. The air thickens, and the walls pulse with a malevolent energy. The shopkeeper's eyes glow as he mutters an incantation, 
    and the floor beneath you opens into a dark chasm. You fall, the pendant slipping from your grasp, and the last thing you hear is his cold laughter as the darkness claims you.\n""")
    quit()
   
                                            #Decision tree 3 (riddle)
branch3 = input("""\nWhat is your answer?\n""")

if "river" in branch3.lower():          #Good ending (answer correctly)
    print("""
    The sphinx's eyes soften, and it nods solemnly. "Very good," it rumbles, as the chamber glows with golden light. 
    A portal opens, returning you to the shop, where the shopkeeper stands nodding to you. He places a small trinket in your hand, which fills you with warmth. 
    You thank him and return home with a sense of fulfillment and happiness.
    
    Congratulations on reaching the end of this adventure!""")

else:                                   #Bad ending (answer incorrectly)
    print("""
    The sphinx rears back, its voice booming with disapproval. "Foolish," it sneers, and the air grows heavy. 
    The chamber collapses inward, pulling you into a swirling abyss. 
    You awaken bound in chains within the mirror's shattered frame, doomed to serve the sphinx's will for eternity.""")
    quit()
