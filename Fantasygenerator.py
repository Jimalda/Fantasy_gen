# In this project, users will be able randomly to generate an avatar with races, stats, powers, weapons and skills.
# The character will then be given a name and will be saved in a json file.
#The program will then be able to use an algorithm to determine the winner of a fight between two characters.
# The program will also be able to load a character from a json file and display its stats
import random
import json
import os

Races=["Terrians", "Merkarians", "Venusians", "Lunarians", "Martians", "Saturnians", "Jupitarians","Neptunians","Uranians","Plutonians","Solarians","Callistians","Ganymedean", "Tritonians","Ionians"]
Stats=["Strength", "Agility", "Endurance", "Aether", "Wisdom", "Intelligence", "Charisma","Weapon mastery"]
moral_alignment=["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
#Here, we define the subclasses
Terrians_subclass_and_weights={"Human": 0.6, "Atlantean": 0.4, "Elven": 0.3, "Orc": 0.3, "Cloudstrider": 0.1}
Merkarians_subclass_and_weights={"Copper": 0.6, "Iron": 0.4, "Silver": 0.2, "Gold": 0.1, "Platinum": 0.05}
Venusians_subclass_and_weights={"Amazon": 0.5, "Cyclops": 0.4, "Toxicbreather": 0.3, "Cinderwalker": 0.2, "Dragon": 0.05}
Lunarians_subclass_and_weights={"Dreamwalker": 0.5, "Nightstalker": 0.4, "Moonshaper": 0.3, "Starcaller": 0.2, "Eclipsian": 0.1}
Martians_subclass_and_weights={"Robot":0.5,"Artificial Intelligence":0.2,"Cyber Hivemind":0.1, "Bio Human":0.4,"Android":0.3}
Saturnians_subclass_and_weights={"Kilometerian": 0.5, "Milehigh": 0.4, "Soundbreaker": 0.3, "Machsprinter": 0.2, "Lightyearian": 0.1}
Jupitarians_subclass_and_weights={"Plebian": 0.5, "Noble": 0.4, "Aristocrat": 0.3, "Royal": 0.2, "Imperial": 0.1}
Neptunians_subclass_and_weights={"Riverfolk": 0.4, "Abyssal": 0.2, "Oceanic": 0.3, "Neptunian": 0.1, "Swampwalker": 0.2}
Uranians_subclass_and_weights={"Rooster": 0.4, "Owl": 0.3, "Eagle": 0.2, "Ostrich": 0.2, "Phoenix": 0.1}
Plutonians_subclass_and_weights={"Imp": 0.5, "Demon": 0.4, "Devil": 0.3, "Hellspawn": 0.2, "Infernal": 0.1}
Solarians_subclass_and_weights={"Solar": 0.5, "Stellar": 0.4, "Galactic": 0.3, "Cosmic": 0.2, "Celestial": 0.1}
Callistians_subclasses={"Moth": 0.5, "Ladybug":0.4, "Butterfly":0.3, "Dragonfly":0.2, "Royal Bee":0.1}
Ganymedean_subclasses={"Lizard": 0.5,"Gecko":0.4,"Chameleon":0.3,"Royal Cobra":0.1,"Komodo Dragon":0.2}
Tritonians_subclasses={"Shrimp": 0.5, "Crab":0.4,"Lobster":0.3,"Hermit Crab":0.2,"Squid":0.1}
Ionians_Subclasses={"Pepper": 0.5,"Carolina Reaper":0.1,"Ghost Pepper":0.4,"Habanero":0.3,"Scotch Bonnet":0.2}

Weird_weapons=["Spoon","Fork","Cucumber","Broom","Fishing Rod", "Tennis Racket", "Rubber Chicken","Lollipop"]
Common_weapons= ["Sword", "Axe", "Bow", "Staff", "Dagger", "Spear", "Mace", "Crossbow"]
Uncommon_weapons= ["Greatsword", "Warhammer", "Chained Whip", "Boomerang", "Wand", "Boxing gloves", "Glaive", "Pistol"]
Rare_weapons=["Scythe", "Katana", "Rapier", "Flail", "Lance Gun", "Oceanic Trident", "Cannon", "Claymore","Cloud Board","Moon Brush","Speed Boots","Crab Claws"]
Epic_weapons=["Minigun", "Laser Sword", "Energy Bow", "Plasma Rifle", "Tornado Whip", "Void Staff", "Thunder Spear", "Meteor Hammer","Eagle Claws","Neptunian Spear","Lobster Claws","Habanero Bombs"]
Legendary_weapons=["Achilles' Shield","Megawatt Canon","Death's Lantern","Hyperdecibel Boombox","Volcanic Claws","Celestial Bow", "Bulle's Bubblegun","Atomic launcher","Carolina Scythe"]
Divine_Weapons= ["Excalibur", "Mjolnir", "Gungnir", "Senegalese Spear", "Universal Wand","Black Hole Gun","Time Clock","Shooting Star Cannon"]

Common_powers=["Fire Manipulation", "Ice Manipulation", "Lightning Manipulation", "Earth Manipulation", "Wind Manipulation", "Water Manipulation", "Healing Light", "Shadow Manipulation","Stealth","Charge Attack",
               "Animal Communication", "Enhances Senses", "Telekinesis","Invisibility","High Jump","Digging powers","Wall Climbing","Camouflage"]
Uncommon_powers=["Gravity Manipulation", "Light Manipulation", "Magnetic Manipulation", "Emotional Manipulation", "Sound Manipulation", "Nature's Grace","Night Vision","Mechanical Strength",
                 "Energy Shield","Cloning","Stretching","Rage","Insect Control","Intangibility","Multi Limbs", "Enhanced Reflexes","High Fortune","Poison Manipulation"]
Weird_powers=["Rizz","Testi Tortion","Aura Farming","Meme Mastery","TikTok Dance","Crashout","Brainrot Manipulation","Gaslighting"]
Rare_powers=["Bloodbending","Dream Manipulation","Storm Control","Future Sight","Teleportation","Illusions","Regeneration","Midas Touch","Toxic Breath","Flight","Hacking","Sonic Boom", "Ghost Form",
             "Plant Control","Shadow puppet","Kinetic Strength","Disposable limbs","Gigantism","Pollination","Honey Manipulation","Inner Fortress","Ink Manipulation","Mind Control","Stellar Manipulation"]
Epic_powers=["Galactic Manipulation","Galactic Manipulation", "Time Manipulation", "Space Manipulation", "Reality Warping", "Dimensional Travel", "Quantum Manipulation","Platinum Armor","Void Manipulation","Cosmic Ray","Solar Flare"
             "Portal creation","Copy powers","Bee Swarm","Hellfire"]
Legendary_powers=["Final Form","Soul Siphon","Infinite Energy","Black Hole Creation","Supernova","Light Speed Travel","Time Stop","Reality Shift","Cyber Army","Luck Manipulation","Cosmic Manipulation"]
Divine_Powers= ["Divine Light", "Celestic Manipulation", "Ultra Instinct", "Immortality", "Omniscience", "Creation", "Destruction", "Resurrection","Chronoreset"]

No_archetypes= ["None"]
Common_archetypes= ["Mage","Warrior","Tank"]
Uncommon_archetypes= ["Wizard","Assassin","Healer"]
Rare_archetypes= ["Summoner","Rider","Dual Wielder","Berserker"]
Epic_archetypes= ["Archmage","Siphoner","Gambler","Joker"]
Legendary_archetypes=["Legendary Hero","Cosmic Guardian","Chosen One"]

race_chances= {
    "Terrians": 0.30,
    "Merkarians": 0.20,
    "Venusians": 0.25,
    "Lunarians": 0.10,
    "Martians": 0.075,
    "Saturnians": 0.15,
    "Jupitarians": 0.10,
    "Neptunians": 0.15,
    "Uranians": 0.10,
    "Plutonians": 0.05,
    "Solarians": 0.01,
    "Callistians": 0.05,
    "Ganymedean": 0.10,
    "Tritonians": 0.025,
    "Ionians": 0.025
}
alignment_coords = {
    "Lawful Good": (1, 1), "Neutral Good": (2, 1), "Chaotic Good": (3, 1),
    "Lawful Neutral": (1, 2), "True Neutral": (2, 2), "Chaotic Neutral": (3, 2),
    "Lawful Evil": (1, 3), "Neutral Evil": (2, 3), "Chaotic Evil": (3, 3)
}
def alignment_similarity(a1, a2):
    if a1 not in alignment_coords or a2 not in alignment_coords:
        return 0.5
    x1, y1 = alignment_coords[a1]
    x2, y2 = alignment_coords[a2]
    max_dist = ((3 - 1)**2 + (3 - 1)**2)**0.5
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return 1 - (dist / max_dist)

def pick_relationship(similarity):
    # 70% chance they haven't met
    if random.random() < 0.7:
        return "Have not met"

    # Otherwise use similarity-based weighting
    if similarity >= 0.8:
        weights = {"Close Friend": 40, "Friend": 40, "Rival": 10, "Enemy": 10}
    elif similarity >= 0.5:
        weights = {"Close Friend": 25, "Friend": 35, "Rival": 20, "Enemy": 20}
    elif similarity >= 0.2:
        weights = {"Close Friend": 15, "Friend": 25, "Rival": 30, "Enemy": 30}
    else:
        weights = {"Close Friend": 5, "Friend": 10, "Rival": 35, "Enemy": 50}

    total = sum(weights.values())
    r = random.randint(1, total)
    cumulative = 0
    for relation, chance in weights.items():
        cumulative += chance
        if r <= cumulative:
            return relation
    return "Neutral"
def save_characters(characters):
    filename = "Characters.json"
    with open(filename, "w") as file:
        json.dump(characters, file, indent=4)

class Character:
    def __init__(self,name=""):
        self.name = name
        self.subrace = ""
        self.archetype = ""
        self.height = 0
        self.strength = 0
        self.agility= 0
        self.resistance = 0
        self.endurance = 0
        self.aether = 0
        self.wisdom = 0
        self.intelligence = 0
        self.charisma = 0
        self.powers = []
        self.weapons = []
        self.moral_alignment = ""
        self.partner= None
        self.relationships=[]
    
    
    def input_name(self):
        self.name = input("Enter the name of your character: ")
        while not self.name.strip():
            print("Name cannot be empty. Please enter a valid name.")
            self.name = input("Enter the name of your character: ")
    def generate_race(self):
        self.race = random.choices(Races, weights=[race_chances[race] for race in Races])[0]
    def generate_subrace(self):
        if self.race == "Terrians":
            self.subrace = random.choices(list(Terrians_subclass_and_weights.keys()), weights=list(Terrians_subclass_and_weights.values()))[0]
        elif self.race == "Merkarians":
            self.subrace = random.choices(list(Merkarians_subclass_and_weights.keys()), weights=list(Merkarians_subclass_and_weights.values()))[0]
        elif self.race == "Venusians":
            self.subrace = random.choices(list(Venusians_subclass_and_weights.keys()), weights=list(Venusians_subclass_and_weights.values()))[0]
        elif self.race == "Lunarians":
            self.subrace = random.choices(list(Lunarians_subclass_and_weights.keys()), weights=list(Lunarians_subclass_and_weights.values()))[0]
        elif self.race == "Martians":
            self.subrace = random.choices(list(Martians_subclass_and_weights.keys()), weights=list(Martians_subclass_and_weights.values()))[0]
        elif self.race == "Saturnians":
            self.subrace = random.choices(list(Saturnians_subclass_and_weights.keys()), weights=list(Saturnians_subclass_and_weights.values()))[0]
        elif self.race == "Jupitarians":
            self.subrace = random.choices(list(Jupitarians_subclass_and_weights.keys()), weights=list(Jupitarians_subclass_and_weights.values()))[0]
        elif self.race == "Neptunians":
            self.subrace = random.choices(list(Neptunians_subclass_and_weights.keys()), weights=list(Neptunians_subclass_and_weights.values()))[0]
        elif self.race == "Uranians":
            self.subrace = random.choices(list(Uranians_subclass_and_weights.keys()), weights=list(Uranians_subclass_and_weights.values()))[0]
        elif self.race == "Plutonians":
            self.subrace = random.choices(list(Plutonians_subclass_and_weights.keys()), weights=list(Plutonians_subclass_and_weights.values()))[0]
        elif self.race == "Solarians":
            self.subrace = random.choices(list(Solarians_subclass_and_weights.keys()), weights=list(Solarians_subclass_and_weights.values()))[0]
        elif self.race == "Callistians":
            self.subrace = random.choices(list(Callistians_subclasses.keys()), weights=list(Callistians_subclasses.values()))[0]
        elif self.race == "Ganymedean":
            self.subrace = random.choices(list(Ganymedean_subclasses.keys()), weights=list(Ganymedean_subclasses.values()))[0]
        elif self.race == "Tritonians":
            self.subrace = random.choices(list(Tritonians_subclasses.keys()), weights=list(Tritonians_subclasses.values()))[0]
        print(f"Generated subrace: {self.subrace}")
    def generate_archetype(self):
        archetype_chances = {
            "No_archetypes": 0.4,
            "Common_archetypes": 0.4,
            "Uncommon_archetypes": 0.2,
            "Rare_archetypes": 0.1,
            "Epic_archetypes": 0.07,
            "Legendary_archetypes": 0.03
        }
        archetype_types = list(archetype_chances.keys())
        archetype_weights = list(archetype_chances.values())
        archetype_type = random.choices(archetype_types, weights=archetype_weights)[0]
        if archetype_type == "No_archetypes":
            self.archetype = random.sample(No_archetypes, 1)[0]
        elif archetype_type == "Common_archetypes":
            self.archetype = random.sample(Common_archetypes, 1)[0]
        elif archetype_type == "Uncommon_archetypes":
            self.archetype = random.sample(Uncommon_archetypes, 1)[0]
        elif archetype_type == "Rare_archetypes":
            self.archetype = random.sample(Rare_archetypes, 1)[0]
        elif archetype_type == "Epic_archetypes":
            self.archetype = random.sample(Epic_archetypes, 1)[0]
        elif archetype_type == "Legendary_archetypes":
            self.archetype = random.sample(Legendary_archetypes, 1)[0]
    def generate_stats(self):
        #if they are a Jupitarians, they will have a height between 150 and 200 cm, otherwise between 200 and 400 cm.
        if self.race == "Jupitarians":
            self.height = random.randint(2000, 5000)
        # If they are merkarians or Callistans, they will have a height between 30 and 80 cm
        elif self.race == "Merkarians" or self.race == "Callistians":
            self.height = random.randint(30, 80)
        else:
            self.height = random.randint(100, 250)
        self.strength = random.randint(0, 15)
        self.agility = random.randint(0, 15)
        self.endurance = random.randint(0, 15)
        self.resistance = random.randint(0, 15)
        self.aether = random.randint(0, 15)
        self.wisdom = random.randint(0, 15)
        self.intelligence = random.randint(0, 15)
        self.charisma = random.randint(0, 15)
    

    def add_subrace_boons(self):
        if self.subrace=="Human":
            self.charisma += 1
        elif self.subrace == "Atlantean":
            self.endurance += 1
            self.powers.append("Water Manipulation")
        elif self.subrace == "Elven":
            self.height += 10
            self.aether += 1
            self.wisdom += 1
            self.powers.append("Nature's Grace")
        elif self.subrace == "Orc":
            self.height += 20
            self.strength += 2
            self.endurance += 2
        elif self.subrace == "Cloudstrider":
            self.agility += 3
            self.powers.append("Storm Control")
            self.weapons.append("Cloud Board")
        elif self.subrace == "Copper":
            self.endurance += 1
        elif self.subrace == "Iron":
            self.strength += 2
        elif self.subrace == "Silver":
            self.resistance += 1
            self.agility+=1
            self.intelligence += 1
        elif self.subrace == "Gold":
            self.charisma += 2
            self.resistance += 1
            self.strength += 1
            self.powers.append("Midas Touch")
        elif self.subrace == "Platinum":
            self.aether += 2
            self.intelligence += 2
            self.resistance +=4
            self.charisma += 2
            self.powers.append("Platinum armor")
        elif self.subrace == "Amazon":
            self.strength += 2
            self.agility += 1
            self.charisma += 1
            self.powers.append("Nature's Grace")
        elif self.subrace== "Cyclops":
            self.strength += 3
            self.endurance += 2
            self.height += 100
        elif self.subrace == "Toxicbreather":
            self.endurance += 1
            self.resistance += 1
            self.powers.append("Toxic Breath")
        elif self.subrace == "Cinderwalker":
            self.wisdom += 2
            self.aether += 1
            self.powers.append("Fire Manipulation")
        elif self.subrace == "Dragon":
            self.strength += 4
            self.endurance += 3
            self.agility += 2
            self.height += 300
            self.aether += 2
            self.wisdom += 1
            self.powers.append("Fire Manipulation")
            self.powers.append("Flight")
        elif self.subrace == "Dreamwalker":
            self.wisdom += 2
            self.aether += 2
            self.powers.append("Dream Manipulation")
        elif self.subrace == "Nightstalker":
            self.agility += 3
            self.endurance += 2
            self.powers.append("Shadow Manipulation")
            self.powers.append("Night Vision")
        elif self.subrace == "Moonshaper":
            self.wisdom += 3
            self.aether += 2
            self.resistance += 2
            self.weapons.append("Moon Brush")
        elif self.subrace == "Starcaller":
            self.intelligence += 4
            self.aether += 3
            self.agility += 2
            self.powers.append("Light Manipulation")
        elif self.subrace == "Eclipsian":
            self.charisma += 2
            self.wisdom += 2
            self.strength += 1
            self.agility += 1
            self.aether += 1
            self.resistance += 1
            self.intelligence += 1
            self.endurance+=1
            self.powers.append("Darkness Manipulation")
            self.powers.append("Light Manipulation")
        elif self.subrace == "Robot":
            self.strength += 3
            self.endurance += 3
            self.intelligence += 1
            self.powers.append("Mechanical Strength")
        elif self.subrace == "Artificial Intelligence":
            self.intelligence += 4
            self.aether += 3
            self.charisma += 2
            self.powers.append("Hacking")
        elif self.subrace == "Cyber Hivemind":
            self.intelligence += 5
            self.aether += 5
            self.charisma += 5
            self.powers.append("Mind Control")
            self.weapons.append("Cyber Army")
        elif self.subrace == "Bio Human":
            self.strength += 2
            self.agility += 2
            self.endurance += 2
            self.intelligence += 2
            self.wisdom += 2
            self.charisma += 2
        elif self.subrace == "Android":
            self.endurance=15
            self.strength=15
        elif self.subrace == "Kilometerian":
            self.agility += 3
            self.endurance += 3
        elif self.subrace == "Milehigh":
            self.strength += 2
            self.endurance += 2
            self.agility += 2
        elif self.subrace == "Soundbreaker":
            self.strength += 4
            self.agility += 4
            self.powers.append("Sound Manipulation")
        elif self.subrace == "Machsprinter":
            self.agility += 5
            self.endurance += 3
            self.weapons.append("Speed Boots")
        elif self.subrace == "Lightyearian":
            self.strength += 3
            self.agility += 10
            self.endurance += 5
            self.powers.append("Light Manipulation")
            self.powers.append("Light Speed Travel")
        elif self.subrace == "Plebian":
            self.charisma+=1
            self.strength+=1
        elif self.subrace == "Noble":
            self.charisma += 2
            self.intelligence += 2
        elif self.subrace == "Aristocrat":
            self.charisma += 3
            self.intelligence += 3
        elif self.subrace == "Royal":
            self.charisma += 4
            self.intelligence += 4
            self.strength += 2
            self.endurance += 2
        elif self.subrace == "Imperial":
            self.charisma += 5
            self.intelligence += 5
            self.strength += 3
            self.endurance += 3
        elif self.subrace == "Riverfolk":
            self.agility += 3
            self.endurance += 2
        elif self.subrace == "Abyssal":
            self.strength += 4
            self.endurance += 3
            self.powers.append("Night Vision")
        elif self.subrace == "Oceanic":
            self.strength += 3
            self.endurance += 3
            self.weapons.append("Oceanic Trident")
        elif self.subrace == "Neptunian":
            self.strength += 5
            self.endurance += 5
            self.agility += 3
            self.weapons.append("Neptunian Spear")
        elif self.subrace == "Swampwalker":
            self.strength += 5
            self.endurance += 5
            self.agility -= 1
            self.powers.append("Earth Manipulation")
        elif self.subrace == "Rooster":
            self.agility += 3
            self.endurance += 2
            self.powers.append("Flight")
            self.powers.append("Sound Manipulation")
        elif self.subrace == "Owl":
            self.agility += 3
            self.wisdom += 3
            self.aether += 2
            self.powers.append("Night Vision")
            self.powers.append("Flight")
        elif self.subrace == "Eagle":
            self.agility += 4
            self.endurance += 3
            self.strength += 2
            self.powers.append("Flight")
            self.powers.append("Night Vision")
            self.weapons.append("Eagle Claws")
        elif self.subrace == "Ostrich":
            self.agility += 5
            self.endurance += 5
            self.strength += 3
        elif self.subrace == "Phoenix":
            self.agility += 5
            self.endurance += 5
            self.strength += 5
            self.aether += 5
            self.wisdom += 5
            self.powers.append("Fire Manipulation")
            self.powers.append("Flight")
        elif self.subrace == "Imp":
            self.agility += 1
            self.aether += 1
            self.intelligence += 1
            self.charisma += 1
            self.powers.append("Fire Manipulation")
        elif self.subrace == "Demon":
            self.strength += 2
            self.endurance += 2
            self.aether += 2
            self.intelligence += 2
            self.powers.append("Fire Manipulation")
            self.powers.append("Shadow Manipulation")
        elif self.subrace == "Devil":
            self.strength += 3
            self.endurance += 3
            self.aether += 3
            self.intelligence += 3
            self.charisma += 3
            self.powers.append("Fire Manipulation")
            self.powers.append("Shadow Manipulation")
            self.powers.append("Mind Control")
        elif self.subrace == "Hellspawn":
            self.strength += 4
            self.endurance += 4
            self.aether += 4
            self.intelligence += 4
            self.charisma += 4
            self.powers.append("Shadow Manipulation")
            self.powers.append("Mind Control")
            self.powers.append("Hellfire")
            self.powers.append("Flight")
        elif self.subrace == "Infernal":
            self.strength += 5
            self.endurance += 5
            self.aether += 5
            self.intelligence += 5
            self.charisma += 5
            self.powers.append("Shadow Manipulation")
            self.powers.append("Mind Control")
            self.powers.append("Hellfire")
            self.powers.append("Flight")
            self.powers.append("Night Vision")

        elif self.subrace == "Solar":
            self.strength += 3
            self.endurance += 3
            self.aether += 3
            self.intelligence += 3
            self.charisma += 3
            self.powers.append("Light Manipulation")
            self.powers.append("Solar Flare")
        elif self.subrace == "Stellar":
            self.strength += 4
            self.endurance += 4
            self.aether += 4
            self.intelligence += 4
            self.charisma += 4
            self.powers.append("Stellar Manipulation")
            self.powers.append("Cosmic Ray")
        elif self.subrace == "Galactic":
            self.strength += 5
            self.endurance += 5
            self.aether += 5
            self.intelligence += 5
            self.charisma += 5
            self.powers.append("Galactic Manipulation")
            self.powers.append("Black Hole Creation")
        elif self.subrace == "Cosmic":
            self.strength += 6
            self.endurance += 6
            self.aether += 6
            self.intelligence += 6
            self.charisma += 6
            self.powers.append("Cosmic Manipulation")
            self.powers.append("Supernova")
        elif self.subrace == "Celestial":
            self.strength += 7
            self.endurance += 7
            self.aether += 7
            self.intelligence += 7
            self.charisma += 7
            self.powers.append("Celestial Manipulation")
            self.powers.append("Divine Light")
        elif self.subrace == "Moth":
            self.agility += 2
            self.endurance += 1
            self.powers.append("Flight")
        elif self.subrace == "Ladybug":
            self.agility += 3
            self.charisma += 2
            self.powers.append("High Fortune")
            self.powers.append("Flight")
        elif self.subrace == "Butterfly":
            self.agility += 4
            self.charisma += 3
            self.powers.append("Flight")
            self.powers.append("Pollination")
        elif self.subrace == "Dragonfly":
            self.agility += 5
            self.charisma += 4
            self.powers.append("Flight")
            self.powers.append("Super Speed")
            self.powers.append("Heightened Senses")
        elif self.subrace == "Royal Bee":
            self.agility += 6
            self.charisma += 5
            self.powers.append("Flight")
            self.powers.append("Bee Swarm")
            self.powers.append("Honey Manipulation")
            self.powers.append("Pollination")
        elif self.subrace == "Lizard":
            self.strength += 2
            self.wisdom += 1
        elif self.subrace == "Gecko":
            self.strength += 3
            self.wisdom += 4
            self.powers.append("Wall Climbing")
        elif self.subrace == "Chameleon":
            self.strength += 4
            self.wisdom += 5
            self.powers.append("Camouflage")
            self.powers.append("Invisibility")
        elif self.subrace == "Royal Cobra":
            self.strength += 5
            self.wisdom += 6
            self.endurance += 4
            self.powers.append("Poison Manipulation")
            self.powers.append("Mind Control")
        elif self.subrace == "Komodo Dragon":
            self.strength += 6
            self.wisdom += 3
            self.endurance += 4
            self.powers.append("Poison Manipulation")
            self.powers.append("Camouflage")
            self.powers.append("Wall Climbing")
        elif self.subrace == "Shrimp":
            self.resistance += 1
            self.intelligence += 2
            self.endurance += 1
            self.powers.append("Water Manipulation")
        elif self.subrace == "Crab":
            self.resistance += 2
            self.intelligence += 3
            self.endurance += 2
            self.powers.append("Crab Claws")
        elif self.subrace == "Lobster":
            self.resistance += 3
            self.intelligence += 4
            self.strength += 3
            self.weapons.append("Lobster Claws")
        elif self.subrace == "Hermit Crab":
            self.resistance += 5
            self.intelligence += 5
            self.endurance += 4
            self.powers.append("Inner Fortress")
        elif self.subrace == "Squid":
            self.intelligence += 8
            self.wisdom += 6
            self.aether += 5
            self.powers.append("Ink Manipulation")
        elif self.subrace == "Pepper":
            self.aether += 1
            self.strength += 1
            self.wisdom -= 1
            self.powers.append("Fire Manipulation")
            self.powers.append("Rage")
        elif self.subrace == "Carolina Reaper":
            self.aether += 5
            self.strength += 5
            self.powers.append("Fire Manipulation")
            self.powers.append("Soul Siphon")
            self.weapons.append("Carolina Scythe")
        elif self.subrace == "Ghost Pepper":
            self.aether += 3
            self.strength += 3
            self.wisdom -= 1
            self.powers.append("Fire Manipulation")
            self.power.append("Ghost form")
        elif self.subrace == "Habanero":
            self.aether += 4
            self.strength += 3
            self.wisdom -= 1
            self.powers.append("Fire Manipulation")
            self.weapons.append("Habanero Bombs")
        elif self.subrace == "Scotch Bonnet":
            self.aether += 4
            self.strength += 4
            self.wisdom -= 1
            self.powers.append("Fire Manipulation")
            self.powers.append("Supernova")

    def add_archetype_boons(self):
        if self.archetype == "Mage":
            self.aether += 1
            self.intelligence += 1
        elif self.archetype == "Warrior":
            self.strength += 1
            self.endurance += 1
        elif self.archetype == "Tank":
            self.endurance += 4
            self.resistance += 2
            self.agility -= 2
        elif self.archetype == "Wizard":
            self.aether += 2
            self.intelligence += 2
        elif self.archetype == "Assassin":
            self.agility += 3
            self.strength += 2
            self.endurance += 1
            self.powers.append("Stealth")
        elif self.archetype == "Healer":
            self.aether += 2
            self.wisdom += 2
            self.charisma += 2
            self.powers.append("Healing Light")
        elif self.archetype == "Archmage":
            self.aether += 3
            self.intelligence += 3
            self.wisdom += 3
            self.charisma += 3
        elif self.archetype == "Siphoner":
            self.aether += 2
            self.intelligence += 2
        elif self.archetype =="Berserker":
            self.strength += 4
            self.endurance += 4
            self.agility += 2
        elif self.archetype == "Legendary Hero":
            self.strength += 3
            self.endurance += 3
            self.agility += 3
            self.aether += 3
            self.wisdom += 3
            self.intelligence += 3
            self.charisma += 3
            self.weapons.append(random.choice(Divine_Weapons))
        elif self.archetype == "Cosmic Guardian":
            self.strength += 3
            self.endurance += 3
            self.agility += 3
            self.aether += 3
            self.wisdom += 3
            self.intelligence += 3
            self.charisma += 3
            self.powers.append(random.choice(Legendary_powers))
            self.weapons.append(random.choice(Legendary_weapons))
        elif self.archetype == "Chosen One":
            self.strength += 3
            self.endurance += 3
            self.agility += 3
            self.aether += 3
            self.wisdom += 3
            self.intelligence += 3
            self.charisma += 3
            self.powers.append(random.choice(Divine_Powers))
        elif self.archetype == "Summoner":
            self.intelligence += 2
            self.charisma += 2
            self.partners = ["Wisp", "Beast", "Undead", "Demon", "Celestial"]
            self.partner = random.choice(self.partners)
            if self.partner == "Wisp":
                self.powers.append("Light Manipulation")
                self.aether += 1
            elif self.partner == "Beast":
                self.strength += 2
                self.agility += 2
                self.endurance += 2
                self.powers.append("Beast Mastery")
            elif self.partner == "Undead":
                self.strength += 3
                self.endurance += 3
                self.powers.append("Necromancy")

            elif self.partner == "Demon":
                self.strength += 4
                self.endurance += 4
                self.aether += 2
                self.intelligence += 2
                self.charisma += 2
                self.powers.append("Demonic Pact")

            elif self.partner == "Celestial":
                self.strength += 3
                self.endurance += 3
                self.aether += 4
                self.intelligence += 4
                self.charisma += 4
                self.powers.append("Divine Blessing")
        elif self.archetype == "Rider":
            self.partner=random.choice(["Pig","Dragon", "Griffin", "Ice Phoenix", "Elephant", "Pegasus"])
            if self.partner == "Pig":
                self.strength += 1
                self.agility += 1
            elif self.partner == "Dragon":
                self.strength += 2
                self.agility += 2
                self.endurance += 2
                self.aether += 2
                self.wisdom += 2
                self.intelligence += 2
                self.charisma += 2
                self.powers.append("Fire Manipulation")
                self.powers.append("Flight")
            elif self.partner == "Griffin":
                self.strength += 2
                self.agility += 3
                self.endurance += 2
                self.powers.append("Flight")
            elif self.partner == "Ice Phoenix":
                self.strength += 2
                self.agility += 2
                self.endurance += 2
                self.aether += 2
                self.wisdom += 2
                self.intelligence += 2
                self.charisma += 2
                self.powers.append("Ice Manipulation")
                self.powers.append("Flight")
            elif self.partner == "Elephant":
                self.strength += 4
                self.endurance += 4
                self.agility += 1
                self.powers.append("Charge Attack")
            elif self.partner == "Pegasus":
                self.strength += 2
                self.agility += 3
                self.endurance += 2
                self.powers.append("Flight")
            
        elif self.archetype == "Dual Wielder":
            self.strength += 2
            self.agility += 2
        
            
            
            
            
  
  
    def generate_powers(self):
        # We will randomly choose from common to divine with common being very easy to get and divine being very hard to get
        power_chances = {
            "Common": 0.5,
            "Uncommon": 0.3,
            "Rare": 0.2,
            "Weird": 0.15,
            "Legendary": 0.1,
            "Divine": 0.05
        }
        power_types = list(power_chances.keys())
        power_weights = list(power_chances.values())
        power_numbers=1
        power_type = random.choices(power_types, weights=power_weights)[0]
        if power_type == "Common":
            self.powers += (random.sample(Common_powers, power_numbers))
        elif power_type == "Uncommon":
            self.powers += (random.sample(Uncommon_powers, power_numbers))
        elif power_type == "Rare":
            self.powers += (random.sample(Rare_powers, power_numbers))
        elif power_type == "Weird":
            self.powers += (random.sample(Weird_powers, power_numbers))
        elif power_type == "Legendary":
            self.powers += (random.sample(Legendary_powers, power_numbers))
        elif power_type == "Divine":
            self.powers += (random.sample(Divine_Powers, power_numbers))
           
    def generate_weapons(self):
        if self.weapons==[]:
            weapon_chances = {
                "Common": 0.5,
                "Uncommon": 0.3,
                "Rare": 0.2,
                "Epic": 0.1,
                "Legendary": 0.05,
                "Divine": 0.01
            }
            if self.archetype == "Dual Wielder":
                weapon_number=2
            else:
                weapon_number=1
            weapon_types = list(weapon_chances.keys())
            weapon_weights = list(weapon_chances.values())
            weapon_type = random.choices(weapon_types, weights=weapon_weights)[0]
            if weapon_type == "Common":
                self.weapons.append(random.sample(Common_weapons, weapon_number)[0])
            elif weapon_type == "Uncommon":
                self.weapons.append(random.sample(Uncommon_weapons, weapon_number)[0])
            elif weapon_type == "Rare":
                self.weapons.append(random.sample(Rare_weapons, weapon_number)[0])
            elif weapon_type == "Epic":
                self.weapons.append(random.sample(Epic_weapons, weapon_number)[0])
            elif weapon_type == "Legendary":
                self.weapons.append(random.sample(Legendary_weapons, weapon_number)[0])
            elif weapon_type == "Divine":
                self.weapons.append(random.sample(Divine_Weapons, weapon_number)[0])
        
    def generate_moral_alignment(self):
        if self.race=="Plutonians":
            self.moral_possibilities=["Lawful Evil","Neutral Evil","Chaotic Evil"]
            self.moral_alignment = random.choice(self.moral_possibilities)
        else:
            self.moral_alignment = random.choice(moral_alignment)


    
    def print_character(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Subrace: {self.subrace}")
        print(f"Archetype: {self.archetype}")
        print(f"Stats: Height: {self.height} cm, Strength: {self.strength}, Agility: {self.agility}, Endurance: {self.endurance}, Aether: {self.aether}, Wisdom: {self.wisdom}, Intelligence: {self.intelligence}, Charisma: {self.charisma}")
        print("Powers:")
        for power in self.powers:
            print("- "+power)
        print("Weapons:")
        for weapon in self.weapons:
            print("- "+weapon)
        # if the character has a partner, print it
        if self.partner:
            print(f"Partner: {self.partner}")
        print(f"Moral Alignment: {self.moral_alignment}")
        print("Relationships:")
        for relationship in self.relationships:
            print(f"- {relationship['name']} ({relationship['type']})")

    def plus_one_to_stats(self):
        self.strength += 1
        self.agility += 1
        self.endurance += 1
        self.resistance += 1
        self.aether += 1
        self.wisdom += 1
        self.intelligence += 1
        self.charisma += 1

    def create_character(self):
        if self.name=="":
            self.input_name()
        self.generate_race()
        self.generate_subrace()
        self.generate_archetype()
        self.generate_stats()
        self.add_subrace_boons()
        self.add_archetype_boons()
        if self.archetype=="Mage" or self.archetype=="Wizard" or self.archetype=="Archmage":
            if self.archetype=="Mage":
                for i in range(2):
                    self.generate_powers()
            elif self.archetype=="Wizard":
                for i in range(3):
                    self.generate_powers()
            elif self.archetype=="Archmage":
                for i in range(4):
                    self.generate_powers()
        else:
            self.generate_powers()
        self.generate_weapons()
        self.generate_moral_alignment()
        self.set_relationships()
        self.print_character()
        return self.to_dict()

    def set_relationships(self):
        """Add a new character and generate their relationships with existing ones."""
        characters = load_characters()

        # Ensure all existing characters have a relationships list
        for char in characters:
            if "relationships" not in char:
                char["relationships"] = []


        # Compare new character with each existing one
        for existing_char in characters:
            sim = alignment_similarity(self.moral_alignment, existing_char.get("alignment"))
            relation = pick_relationship(sim)

            # Add to both
            self.relationships.append({"name": existing_char["name"], "type": relation})
            existing_char["relationships"].append({"name": self.name, "type": relation})

        # Add new character to the list
        characters.append(self.to_dict())

        # Save updated data for all characters
        save_characters(characters)
    def save_character(self):
        character_data = {
            "name": self.name,
            "race": self.race,
            "subrace": self.subrace,
            "archetype": self.archetype,
            "stats": {
                "height": self.height,
                "strength": self.strength,
                "agility": self.agility,
                "endurance": self.endurance,
                "aether": self.aether,
                "wisdom": self.wisdom,
                "intelligence": self.intelligence,
                "charisma": self.charisma,
                "resistance": self.resistance
            },
            "powers": self.powers,
            "weapons": self.weapons,
            "moral_alignment": self.moral_alignment,
            # If the character has a partner, include it
            # "partner": self.partner if self.partner else None
            "partner": self.partner if self.partner else None,
            "relationships": self.relationships
        }
        filename = "Characters.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)
        else:
            data = []

        data.append(character_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    def to_dict(self):
            return {
                "name": self.name,
                "race": self.race,
                "subrace": self.subrace,
                "archetype": self.archetype,
                "stats": {
                    "height": self.height,
                    "strength": self.strength,
                    "agility": self.agility,
                    "endurance": self.endurance,
                    "aether": self.aether,
                    "wisdom": self.wisdom,
                    "intelligence": self.intelligence,
                    "charisma": self.charisma,
                    "resistance": self.resistance
                },
                "powers": self.powers,
                "weapons": self.weapons,
                "moral_alignment": self.moral_alignment,
                "partner": self.partner if self.partner else None,
                "relationships": self.relationships
            }
def load_characters():
    filename = "Characters.json"
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)


def simulate_battle(character1_name, character2_name):
    # We will load the characters from the json file
    filename = "Characters.json"
    if not os.path.exists(filename):
        print("No characters found. Please create characters first.")
        return
    with open(filename, "r") as file:
        data = json.load(file)
    character1 = next((char for char in data if char["name"] == character1_name), None)
    character2 = next((char for char in data if char["name"] == character2_name), None)
    # If one of the characters has the joker archetype, they have a 50% chance to reverse everyone's stats and make them all negative
    if character1 and character1["archetype"] == "Joker":
        if random.choice([True, False]):
            for stat in character1["stats"]:
                character1["stats"][stat] = -abs(character1["stats"][stat])
    if character2 and character2["archetype"] == "Joker":
        if random.choice([True, False]):
            for stat in character2["stats"]:
                character2["stats"][stat] = -abs(character2["stats"][stat])
    # If one character has the gambler archetype, they will either lower or increase each of their stats by 1 or 2 temporarily
    if character1 and character1["archetype"] == "Gambler":
        for stat in character1["stats"]:
            if random.choice([True, False]):
                character1["stats"][stat] += random.randint(1, 2)
            else:
                character1["stats"][stat] -= random.randint(1, 2)
    if character2 and character2["archetype"] == "Gambler":
        for stat in character2["stats"]:
            if random.choice([True, False]):
                character2["stats"][stat] += random.randint(1, 2)
            else:
                character2["stats"][stat] -= random.randint(1, 2)
    character1_points=0
    character2_points=0
    if not character1 or not character2:
        print("One or both characters not found.")
        return

    # We firstly compare the strength of the characters
    if character1["stats"]["strength"] > character2["stats"]["strength"]:
        character1_points += 1
    elif character1["stats"]["strength"] < character2["stats"]["strength"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
    
    # We then compare the agility of the characters
    if character1["stats"]["agility"] > character2["stats"]["agility"]:
        character1_points += 1
    elif character1["stats"]["agility"] < character2["stats"]["agility"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
        
    # Next, we compare the aether of the characters
    if character1["stats"]["aether"] > character2["stats"]["aether"]:
        character1_points += 1
    elif character1["stats"]["aether"] < character2["stats"]["aether"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
            
    # Then, we compare the wisdom of the characters
    if character1["stats"]["wisdom"] > character2["stats"]["wisdom"]:
        character1_points += 1
    elif character1["stats"]["wisdom"] < character2["stats"]["wisdom"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
    # After that, we compare the intelligence of the characters
    if character1["stats"]["intelligence"] > character2["stats"]["intelligence"]:
        character1_points += 1
    elif character1["stats"]["intelligence"] < character2["stats"]["intelligence"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
    # Next, we compare the charisma of the characters
    if character1["stats"]["charisma"] > character2["stats"]["charisma"]:
        character1_points += 1
    elif character1["stats"]["charisma"] < character2["stats"]["charisma"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
    # We also compare the resistance of the characters
    if character1["stats"]["resistance"] > character2["stats"]["resistance"]:
        character1_points += 1
    elif character1["stats"]["resistance"] < character2["stats"]["resistance"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
    

    # Finally, we compare the endurance of the characters
    if character1["stats"]["endurance"] > character2["stats"]["endurance"]:
        character1_points += 1
    elif character1["stats"]["endurance"] < character2["stats"]["endurance"]:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
    
    # We combine the weapon powers, if it is common the weapon power is 1
    # if it is uncommon the weapon power is 2, if it is rare or weird the weapon power is 3, if it is epic the weapon power is 4, if it is legendary the weapon power is 5, if it is divine the weapon power is 6
    weapon_power = {
        "Common": 1,
        "Uncommon": 2,
        "Rare": 3,
        "Weird": 3,
        "Epic": 4,
        "Legendary": 5,
        "Divine": 6
    }
    character1_weaponpoints=0
    character2_weaponpoints=0
    for weapon in character1["weapons"]:
        if weapon in Common_weapons:
            character1_weaponpoints += weapon_power["Common"]
        elif weapon in Uncommon_weapons:
            character1_weaponpoints += weapon_power["Uncommon"]
        elif weapon in Rare_weapons:
            character1_weaponpoints += weapon_power["Rare"]
        elif weapon in Weird_weapons:
            character1_points += weapon_power["Weird"]
        elif weapon in Epic_weapons:
            character1_weaponpoints += weapon_power["Epic"]
        elif weapon in Legendary_weapons:
            character1_weaponpoints += weapon_power["Legendary"]
        elif weapon in Divine_Weapons:
            character1_weaponpoints += weapon_power["Divine"]
    for weapon in character2["weapons"]:
        if weapon in Common_weapons:
            character2_weaponpoints += weapon_power["Common"]
        elif weapon in Uncommon_weapons:
            character2_weaponpoints += weapon_power["Uncommon"]
        elif weapon in Rare_weapons:
            character2_weaponpoints += weapon_power["Rare"]
        elif weapon in Weird_weapons:
            character2_weaponpoints += weapon_power["Weird"]
        elif weapon in Epic_weapons:
            character2_weaponpoints += weapon_power["Epic"]
        elif weapon in Legendary_weapons:
            character2_weaponpoints += weapon_power["Legendary"]
        elif weapon in Divine_Weapons:
            character2_weaponpoints += weapon_power["Divine"]
    
    # We compare the weapon points of the characters
    if character1_weaponpoints > character2_weaponpoints:
        character1_points += 1
    elif character1_weaponpoints < character2_weaponpoints:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1
    
    # Now we do the same for powers
    character1_powerpoints = 0
    character2_powerpoints = 0
    power_power = {
        "Common": 1,
        "Uncommon": 2,
        "Rare": 3,
        "Weird": 3,
        "Legendary": 4,
        "Divine": 5
    }
    for power in character1["powers"]:
        if power in Common_powers:
            character1_powerpoints += power_power["Common"]
        elif power in Uncommon_powers:
            character1_powerpoints += power_power["Uncommon"]
        elif power in Rare_powers:
            character1_powerpoints += power_power["Rare"]
        elif power in Weird_powers:
            character1_powerpoints += power_power["Weird"]
        elif power in Legendary_powers:
            character1_powerpoints += power_power["Legendary"]
        elif power in Divine_Powers:
            character1_powerpoints += power_power["Divine"]
    for power in character2["powers"]:
        if power in Common_powers:
            character2_powerpoints += power_power["Common"]
        elif power in Uncommon_powers:
            character2_powerpoints += power_power["Uncommon"]
        elif power in Rare_powers:
            character2_powerpoints += power_power["Rare"]
        elif power in Weird_powers:
            character2_powerpoints += power_power["Weird"]
        elif power in Legendary_powers:
            character2_powerpoints += power_power["Legendary"]
        elif power in Divine_Powers:
            character2_powerpoints += power_power["Divine"]
    # We compare the power points of the characters
    if character1_powerpoints > character2_powerpoints:
        character1_points += 1
    elif character1_powerpoints < character2_powerpoints:
        character2_points += 1
    else:
        # If one character has the berserker archetype, they get a bonus point
        if character1["archetype"] == "Berserker":
            character1_points += 1
        elif character2["archetype"] == "Berserker":
            character2_points += 1      
    
    if character1_points > character2_points:
        if character1_points - character2_points >= 6:
            return(f"{character1_name} wins decisively! Low Diff")
        elif character1_points - character2_points >= 3:
            return(f"{character1_name} wins with a significant advantage! Mid Diff")
        else:
            return(f"{character1_name} wins narrowly! High Diff")
    elif character1_points < character2_points:
        if character2_points - character1_points >= 6:
            return(f"{character2_name} wins decisively! Low Diff")
        elif character2_points - character1_points >= 3:
            return(f"{character2_name} wins with a significant advantage! Mid Diff")
        else:
            return(f"{character2_name} wins narrowly! High Diff")
    else:
        return("It's a draw!")
def simulate_battle_ui(char1_name, char2_name):
    """Return both characters' data, per-stat results, and final outcome for the UI."""
    characters = load_characters()
    char1 = next((c for c in characters if c["name"] == char1_name), None)
    char2 = next((c for c in characters if c["name"] == char2_name), None)
    if not char1 or not char2:
        return None
    # If one of the character has the Gambler archetype, they will either lower or increase each of their stats by 1 or 2 temporarily
    if char1 and char1["archetype"] == "Gambler":
        for stat in char1["stats"]:
            if random.choice([True, False]):
                char1["stats"][stat] += random.randint(1, 2)
            else:
                char1["stats"][stat] -= random.randint(1, 2)
    if char2 and char2["archetype"] == "Gambler":
        for stat in char2["stats"]:
            if random.choice([True, False]):
                char2["stats"][stat] += random.randint(1, 2)
            else:
                char2["stats"][stat] -= random.randint(1, 2)
    # If one of the characters has the joker archetype, they have a 50% chance to reverse everyone's stats and make them all negative
    if char1 and char1["archetype"] == "Joker":
        if random.choice([True, False]):
            for stat in char1["stats"]:
                char1["stats"][stat] = -abs(char1["stats"][stat])
    if char2 and char2["archetype"] == "Joker":
        if random.choice([True, False]):
            for stat in char2["stats"]:
                char2["stats"][stat] = -abs(char2["stats"][stat])

    stats_to_compare = [
        "strength", "agility", "endurance", "aether",
        "wisdom", "intelligence", "charisma", "resistance"
    ]

    comparison = {}
    points_c1 = 0
    points_c2 = 0

    for stat in stats_to_compare:
        if char1["stats"][stat] > char2["stats"][stat]:
            comparison[stat] = 1  # C1 wins
            points_c1 += 1
        elif char1["stats"][stat] < char2["stats"][stat]:
            comparison[stat] = 2  # C2 wins
            points_c2 += 1
        else:
            if char1["archetype"] == "Berserker" or char2["archetype"] == "Berserker":
                if char1["archetype"] == "Berserker":
                    points_c1 += 1
                    comparison[stat] = 1
                if char2["archetype"] == "Berserker":
                    points_c2 += 1
                    comparison[stat] = 2
            else:
                comparison[stat] = 0  # Tie

    # Add simple weapon/power points to total
    def power_score(powers):
        score_map = {
            "Common": 1, "Uncommon": 2, "Rare": 3,
            "Weird": 3, "Legendary": 4, "Divine": 5
        }
        total = 0
        for p in powers:
            if p in Common_powers: total += score_map["Common"]
            elif p in Uncommon_powers: total += score_map["Uncommon"]
            elif p in Rare_powers: total += score_map["Rare"]
            elif p in Weird_powers: total += score_map["Weird"]
            elif p in Legendary_powers: total += score_map["Legendary"]
            elif p in Divine_Powers: total += score_map["Divine"]
        return total

    def weapon_score(weapons):
        score_map = {
            "Common": 1, "Uncommon": 2, "Rare": 3,
            "Weird": 3, "Epic": 4, "Legendary": 5, "Divine": 6
        }
        total = 0
        for w in weapons:
            if w in Common_weapons: total += score_map["Common"]
            elif w in Uncommon_weapons: total += score_map["Uncommon"]
            elif w in Rare_weapons: total += score_map["Rare"]
            elif w in Weird_weapons: total += score_map["Weird"]
            elif w in Epic_weapons: total += score_map["Epic"]
            elif w in Legendary_weapons: total += score_map["Legendary"]
            elif w in Divine_Weapons: total += score_map["Divine"]
        return total

    c1_weapon_points = weapon_score(char1["weapons"])
    c2_weapon_points = weapon_score(char2["weapons"])
    c1_power_points = power_score(char1["powers"])
    c2_power_points = power_score(char2["powers"])
    
    if c1_weapon_points > c2_weapon_points:
        points_c1 += 1
        comparison["weapons"] = 1
    elif c1_weapon_points < c2_weapon_points:
        points_c2 += 1
        comparison["weapons"] = 2
    else:
        if char1["archetype"] == "Berserker":
            points_c1 += 1
            comparison["weapons"] = 1
        elif char2["archetype"] == "Berserker":
            points_c2 += 1
            comparison["weapons"] = 2
        else:
            comparison["weapons"] = 0
    
    if c1_power_points > c2_power_points:
        points_c1 += 1
        comparison["powers"] = 1
    elif c1_power_points < c2_power_points:
        points_c2 += 1
        comparison["powers"] = 2
    else:
        if char1["archetype"] == "Berserker":
            points_c1 += 1
            comparison["powers"] = 1
        elif char2["archetype"] == "Berserker":
            points_c2 += 1
            comparison["powers"] = 2
        else:
            comparison["powers"] = 0
    Diff=""
    if points_c1 > points_c2:
        winner = char1["name"]
        if points_c1-points_c2==10:
            Diff="SWEEP!"
        if points_c1 - points_c2 >= 4:
            Diff = "Low Diff"
        elif points_c1 - points_c2 >= 3:
            Diff = "Mid Diff"
        elif points_c1 - points_c2 > 1:
            Diff = "High Diff"
        else:
            Diff = "Extremely High Diff"
    elif points_c2 > points_c1:
        winner = char2["name"]
        if points_c2 - points_c1 == 10:
            Diff = "SWEEP!"
        if points_c2 - points_c1 >= 4:
            Diff = "Low Diff"
        elif points_c2 - points_c1 >= 3:
            Diff = "Mid Diff"
        elif points_c2 - points_c1 > 1:
            Diff = "High Diff"
        else:
            Diff = "Extremely High Diff"
    else:
        winner = "Draw"
        Diff = "It's a draw!"
        

    return {
        "char1": char1,
        "char2": char2,
        "comparison": comparison,
        "points": (points_c1, points_c2),
        "winner": winner,
        "diff": Diff
    }



