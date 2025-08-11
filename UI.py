import flet as ft
from Fantasygenerator import Character, get_random_weapon, load_characters,simulate_battle_ui,save_characters,get_random_divine_power,get_random_power
from Fantasygenerator import Common_weapons,Uncommon_weapons,Rare_weapons,Legendary_weapons,Weird_weapons,Divine_Weapons, Common_powers, Uncommon_powers, Rare_powers, Epic_powers, Legendary_powers, Divine_Powers, Weird_powers
from Fantasygenerator import No_archetypes, Common_archetypes, Uncommon_archetypes, Rare_archetypes,Epic_archetypes,Legendary_archetypes
import random
bestiary_data = {
    "Merkarians": {
        "description": "Small metal-skinned creatures that live in Mercury's harsh environment. They are known for their resilience and resourcefulness.",
        "subraces": {
            "Copper": "Common Merkarians — durable and practical. They are the backbone of Merkarian society, known for their hard work and reliability.(+1 Endurance)",
            "Iron": "Sturdy warriors forged for conflict. Most of mercury's military is made up of Iron Merkarians, known for their combat prowess and discipline.(+2 Strength)",
            "Silver": "Quick hunters and scouts of the depths. They're not as common as Copper or Iron, but they excel in reconnaissance and stealth operations.(+1 Resistance, Agility and Intelligence)",
            "Gold": "Charismatic leaders who command respect. They're the epitome of beauty and elegance among Merkarians.(+2 Charisma, +1 Resistance and Strength, +Midas Touch)",
            "Platinum": "Elite defenders with nearly impenetrable hide. Most generals and high-ranking officials are Platinum Merkarians, known for their strategic minds and leadership skills.(+2 Aether, Intelligence and Charisma, +4 Resistance, +Platinum Armor)"
        }
    },
    "Venusians": {
        "description": "Lush-world natives with strong ties to nature and flame. They are very resillient due to Venus' harsh environment.",
        "subraces": {
            "Amazon": "Natural warriors, protectors of groves and tribes. Most of them are feminine and can be found in the forests of Venus, known for their combat skills and connection to nature.(+2 Strength,+1 Agility and Charisma,+Nature's Grace)",
            "Cyclops": "Massive single-eyed fighters, slow but devastating. They are the enemies of the Amazons, known for their brute strength and resilience. (+3 Strength, +2 Endurance)",
            "Toxicbreather": "Tough survivors with poisonous breath. They are the reason why Venus is so toxic.(+1 Endurance and Resistance,+Toxic Breath)",
            "Cinderwalker": "Fire-touched, agile spell-walkers. They live inside volcanoes and love to relax in scorching hot springs.(+2 Wisdom, +1 Aether, +Fire Manipulation)",
            "Dragon": "Rare and ancient—powerful and majestic. They usually mind their own business, but when they do get involved, they are a force to be reckoned with.(+4 Strength,+3 Endurance,+2 Agility and Aether,+1 Wisdom, +Fire Manipulation,+Flight)"
        }
    },
    "Terrians": {
        "description": "Humans and related beings that live in Planet Earth. They are known for their adaptability and diversity.",
        "subraces": {
            "Human": "Beings found on the lands of Earth, known for their beauty and creativity. While not the strongest, they are versatile and can adapt to many situations. (+1 Charisma)",
            "Atlantean": "Similar to humans but are amphibious, able to live both on land and in water. They are found in the depths of the oceans and have a high fashion sense.(+1 Endurance, +Water Manipulation)",
            "Elven": "They prefer to live in the forests and tend to live for a long time. They practice different religions and are known for their wisdom and connection to nature.( +1 Aether and Wisdom,+Nature's Grace)",
            "Orc": "They used to be war-loving beings but have become a bit more peaceful. Nonetheless, they are the strongest of the Terrians and are known for their brute strength and combat skills.(+2 Strength and Endurance)",
            "Cloudstrider": "A rare subrace that lives in sky cities. They are very athletic and thrill-seeking, often engaging in extreme sports and aerial activities.(+3 Agility,+Storm Control,+Cloud Board)"
        }
    },
    "Lunarians": {
        "description": "Moon-touched folk with dreamlike powers.Silver hair and eyes and pale skin are common traits among them.",
        "subraces": {
            "Dreamwalker": "Walk the boundary between sleep and waking. They are tied to Humans and can affect their dreams.(+2 Wisdom and Aether, +Dream Manipulation)",
            "Nightstalker": "Silent hunters of the dark. They live in the dark side of the moon and do the dirty work of the Lunarians(+3 Agility, +2 Endurance,+Shadow Manipulation, +Night Vision)",
            "Moonshaper": "Molders of tides and subtle aether. Many of them are artists and musicians and they love to go on tours in Planet Earth.(+3 Wisdom, +2 Aether and Resistance, +Moon Brush)",
            "Starcaller": "Call down distant lights and knowledge. They are the scholars of the Lunarians and often publish their findings in the form of books and scrolls. (+4 Intelligence, +3 Aether, +2 Agility, +Light Manipulation)",
            "Eclipsian": "Ambiguous, master of moon and shadow. They are only born when the Earth and Moon align perfectly, and they are very rare. They have an insane inner power.(+2 Charisma and Wisdom, +1 everything else, +Darkness Manipulation, +Light Manipulation)"
        }
    },
    "Martians": {
        "description": "Tech-forward folk with mechanical augmentations who live in Mars. No one knows how they got so advanced, but they are the most technologically advanced race.",
        "subraces": {
            "Robot": "Constructed warriors of precise engineering. They are conscious despite common belief, and they are the most common subrace of Martians. (+3 Strength and Endurance, +1 Intelligence, +Mechanical Strength)",
            "Artificial Intelligence": "Sentient minds living in synthetic shells. They operate the Martian networks and are responsible for the maintenance of the Martian infrastructure.(+4 Intelligence, +3 Aether, +2 Charisma, +Hacking)",
            "Cyber Hivemind": "Collective intelligence across many bodies. They are the most advanced subrace of Martians. No one can replicate this level of technology.(+5 Intelligence, Aether and Charisma, +Mind Control, +Cyber Army)",
            "Bio Human": "Human-like with biotech enhancements. They're said to be humans from the future who traveled back in time to help the Martians. (+2 in all stats except Aether and resistance)",
            "Android": "Purpose-built humanoids, efficient and enduring. They resemble terrians but are made of metal and have a more robotic appearance. They are often used as soldiers or workers.(Endurance and Strength are set to 15)"
        }
    },
    "Jupitarians": {
        "description": "Gigantic, noble folk with high physical presence who live in Jupiter. Despite their size, they are very kind and gentle.",
        "subraces": {
            "Plebian": "Everyday folk of the giant cities. Nonetheless, they are highly educated and skilled in various trades.(+1 Strength and Charisma)",
            "Noble": "Educated and well-mannered elites. All of them have small castles and mansions, and they are known for their hospitality.(+2 Charisma and Intelligence)",
            "Aristocrat": "Powerful ruling class with privileged training. They are the ones who make the laws and govern the Jupitarian society.(+3 Intelligence and Charisma)",
            "Royal": "Leaders with both might and diplomacy. They're highly respected and often serve as ambassadors to other planets.(+4 Charisma and Intelligence, +2 Strength and Endurance)",
            "Imperial": "Rare rulers with near-absolute command. They even have power over some of the other planets due to their influence and wealth.(+5 Charisma and Intelligence, +3 Strength and Endurance)"
        }
    },
    "Saturnians": {
        "description": "Fast, altitude-adapted people who prize speed who live in Saturn. They travel on the Saturn Ring highways and love a good party.",
        "subraces": {
            "Kilometerian": "Long-distance marathoners of the skies. They're considered the slowest of the Saturnians, but they can run for miles without getting tired. (+3 Agility and Endurance)",
            "Milehigh": "Tall, powerful folk who stride mountains. They are very muscular as well especially their legs, and they can jump very high.(+2 Strength, Endurance and Agilty)",
            "Soundbreaker": "Harness sonic force to move and strike. They use echo-location to navigate and can create sonic booms with their movements.(+4 Strength and Agility, + Sound Manipulation)",
            "Machsprinter": "Blindingly fast warriors. Most of them are athletes and they love to compete.(+5 Agility, +3 Endurance, +Speed Boots)",
            "Lightyearian": "Rare speedsters nearing relativistic travel. They can almost travel at the speed of light and take the fastest lanes of the Saturn Ring highways.(+3 Strength, +10 Agility,+5 Endurance,+Light Manipulation, +Light Speed Travel)"
        }
    },
    "Uranians": {
        "description": "Avian-inspired people of Uranus. One of the best cooks in the solar system, they are known for their culinary skills and love for food.",
        "subraces": {
            "Rooster": "Vocal and proud fighters. They're also considered the best chefs in the solar system, known for their delicious dishes.(+3 Agility, +2 Endurance, +Flight, +Sound Manipulation)",
            "Owl": "Wise nocturnal sentinels. You can mostly find them in the libraries and schools of Uranus, teaching the young ones.(+3 Agility and Wisdom, +2 Aether, +Night Vision, +Flight)",
            "Eagle": "Majestic hunters with strong vision. They are the strongest of the Uranians and are often used as soldiers.(+4 Agility, +3 Endurance, +2 Strength, +Flight, +Night Vision, +Eagle Claws)",
            "Ostrich": "Powerful, ground-oriented runners. They are the fastest of the Uranians and love to migrate to Saturn during the summer.(+5 Agility and +5 Endurance, +3 Strength)",
            "Phoenix": "Legendary reborn beings of flame. They isolate themselves from the rest of the Uranians and are considered a myth by many. They are said to be immortal and can resurrect from their ashes.(+5 Agility, Endurance, Strength, Aether and Wisdom, +Fire Manipulation, +Flight )"
        }
    },
    "Neptunians": {
        "description": "Oceanic people who have the most beautiful architecture and infrastructure that decorate their home planet, Neptune. They value environmental harmony and cleanliness.",
        "subraces": {
            "Riverfolk": "Freshwater dwellers and agile swimmers. They're very organized and live in small communities along the rivers.(+3 Agility, +2 Endurance)",
            "Abyssal": "Deep-sea explorers and guardians. They live in light cities deep in the ocean's dark depths, and have a unique culture.(+4 Strength, +3 Endurance, +Night Vision)",
            "Oceanic": "Open-sea warriors, trident masters. They can stay focused for long periods of time and are known for their combat skills.(+3 Strength and Endurance, +Oceanic Trident)",
            "Neptunian": "Powerful sovereigns of the deep. They are the rulers of the Neptunian society and can be quite stoic.(+5 Strength and Endurance, +3 Agility, +Neptunian Spear)",
            "Swampwalker": "Adapted to bogs and murky waters. They prefer messiness and believe that Neptune's beauty lies in its chaos.(+5 Strength and Endurance, -1 Agility, Earth Manipulation)"
        }
    },
    "Plutonians": {
        "description": "Dark-world denizens tied to infernal or trickster magics that live in Pluto. Despite them being downright evil, they're considered number one in terms of entertainment and media.",
        "subraces": {
            "Imp": "Mischievous lesser fiends. Loves to play pranks and tricks on others, often causing chaos for their own amusement.(+1 Agility, Aether, Intelligence and Charisma, +Fire Manipulation)",
            "Demon": "Dangerous and strong beings that tempt mortals. They are often seen as the embodiment of evil and chaos, but they can also be quite charming.(+2 Strength, Endurance, Aether and Intelligence, +Fire Manipulation, +Shadow Manipulation)",
            "Devil": "Scheming, powerful, and charismatic villains. They will always break the rules to get what they want, and they are known for their cunning and manipulation.(+3 Strength, Endurance, Aether, Intelligence and Charisma, +Fire Manipulation, +Shadow Manipulation, +Mind Control)",
            "Hellspawn": "Brutal warriors born of darkness. They're the only ones that keep Plutonians in check due to their brute strength and combat skills.(+4 Strength, Endurance, Aether, Intelligence and Charisma, +Hellfire, +Flight, +Mind Control, +Shadow Manipulation)",
            "Infernal": "Near-legendary inferno-touched beings. Whenever an infernal is born, it is considered a miracle. They are said to be one of the most powerful beings in the solar system, and they are feared by many.(+5 Strength, Endurance, Aether, Intelligence and Charisma, +Hellfire, +Night Vision, +Flight, +Shadow Manipulation, +Mind Control)"
        }
    },
    "Solarians": {
        "description": "Sun-touched paragons and cosmic nobility. They live in the sun and are considered the most powerful beings in the solar system. They tend to isolate themselves from the rest of the solar system.",
        "subraces": {
            "Solar": "Sun-blessed guardians of light. They handle the sun's energy and are responsible for maintaining its balance.(+3 Strength, Endurance, Aether, Intelligence and Charisma, +Light Manipullation, +Solar Flare)",
            "Stellar": "Manipulators of starlight and rays. They keep the balance of the solar system and ensure that everything runs smoothly.(+4 Strength, Endurance, Aether, Intelligence and Charisma, +Stellar Manipulation, +Cosmic Ray)",
            "Galactic": "Rare beings with cosmic-scale powers. They're ambassadors of the solar system and often travel to other galaxies to maintain peace.(+5 Strength, Endurance, Aether, Intelligence and Charisma, +Galactic Manipullation, +Black Hole Creation)",
            "Cosmic": "Embodiments of wide-scale celestial force. They're part of the Milky Way's council and are responsible for maintaining the balance of the universe. (+6 Strength, Endurance, Aether, Intelligence and Charisma, +Cosmic Manipullation, +Supernova)",
            "Celestial": "Divine agents of balance and radiance. Selected by the multiverse itself, they are the most powerful beings in the solar system and are often seen as deities by many.(+7 Strength, Endurance, Aether, Intelligence and Charisma, +Celestial Manipulation, +Divine Light)"
        }
    },
    "Callistians": {
        "description": "Small, winged folk with insect-symbiosis. They live in Callisto and have a friendly relationship with the Jupitarians. They once went to war with the Ganymedeans.",
        "subraces": {
            "Moth": "Nocturnal flutterers and subtle spies. They love the light and are often seen fluttering around the Jupitarian cities.(+2 Agility, +1 Endurance, +Flight)",
            "Ladybug": "Lucky, protective little folk. They entertain the Jupitarians with their performances and are considered a symbol of good luck.(+3 Agility, +2 Charisma, +Flight, +High Fortune)",
            "Butterfly": "Delicate but influential migrators. Most of them are beauty enthusiasts and define the fashion trends of the Jupitarians.(+4 Agility, +3 Charisma, +Flight, +Pollination)",
            "Dragonfly": "Speedy, precise aerial hunters. They usually travel between Callisto and Jupiter, and they are known for their combat skills.(+5 Agility, +4 Charisma, +Flight, +Super Speed, +Heightened Senses)",
            "Royal Bee": "Hive-born leaders with swarm command. They live in the capital of Callisto: the Hive City, and they are the rulers of the Callistians.(+6 Agility, +5 Charisma , +Flight, +Bee Swarm, +Honey Manipulation, +Pollination)"
        }
    },
    "Ganymedean": {
        "description": "Reptilian folk, cunning and resilient. They love war and conflict, and they are known for their combat skills. They live in Ganymede and have a hostile relationship with the Callistians.",
        "subraces": {
            "Lizard": "Common ground-dwellers, pragmatic. The common troops of the Ganymedean army, known for their resilience and adaptability.(+2 Strength, +1 Wisdom)",
            "Gecko": "Clingers with keen senses. They handle the weapons and equipment of the Ganymedean army, and they are known for their agility and speed.(+3 Strength, +4 Wisdom, +Wall Climbing)",
            "Chameleon": "Masters of disguise and stealth. They are the spies and assassins of the Ganymedean army and gather intel on Callistian movements.(+4 Strength, +5 Wisdom, Camouflage, Invisiblity)",
            "Royal Cobra": "Venomous nobles with mind tricks. Their silver tongues can manipulate others, and they are often seen as the leaders of the Ganymedean society.(+5 Strength, +6 Wisdom, +4 Endurance, +Poison Manipulation, +Mind Control)",
            "Komodo Dragon": "Deadly predators with keen instincts. The tanks of the Ganymedean army, known for their brute strength and combat skills.(+6 Strength, +3 Wisdom, +4 Endurance, +Poison Manipulation, +Camouflage, +Wall Climbing)"
        }
    },
    "Tritonians": {
        "description": "Small shellfolk and cephalopod-intelligent species. They live in Triton, one of Neptune's moons, and are the smartest beings in the solar system. They have a friendly relationship with the Neptunians.",
        "subraces": {
            "Shrimp": "Small, quick workers with surprising intelligence. They have an IQ of 200 and are known for their problem-solving skills.(+1 Resistance, +2 Intelligence, +1 Endurance, +Water Manipulation)",
            "Crab": "Tough shells and clever pincers. They use their pincers to build complex structures and machines, and they are known for their engineering skills.(+2 Resistance, +3 Intelligence, +2 Endurance, +Crab Claws)",
            "Lobster": "Heavily armored brutes of the deep. They do the heavy lifting and are known for their brute strength and combat skills.(+3 Resistance, +4 Intelligence, +3 Strength, +Lobster Claws)",
            "Hermit Crab": "Defensive strategists with mobile armor. Their shells contains a database of all Tritonian knowledge, and they are known for their intelligence and wisdom.(+5 Resistance, +5 Intelligence, +4 Endurance, +Inner Fortress)",
            "Squid": "Highly intelligent, ink-wielding tacticians. They helped the Neptunians build their beautiful cities and are known for their creativity and artistic skills.(+8 Intelligence, +6 Wisdom, +5 Aether, +Ink Manipulation)"
        }
    },
    "Ionians": {
        "description": "The most energetic and vibrant beings in the solar system, known for their love of music and dance. They live in Io, one of Jupiter's moons. It should be noted that they are very powerful.",
        "subraces": {
            "Pepper": "Glowing dancers of the night. They are the entertainers of the Ionians and are known for their beautiful light shows.(+1 Aether and Strength, -1 Wisdom, +Fire Manipulation, +Rage)",
            "Ghost Pepper": "They energise everything they touch. They honor the Carolina Reaper and the celebration of life and death. (+3 Aether and Strength, -1 Wisdom, +Fire Manipulation, +Ghost form)",
            "Habanero": "Fiery, passionate souls with a zest for life. They love explosions and fireworks, and they are known for their love of life. (+4 Aether, +3 Strength, -1 Wisdom, +Fire Manipulation, +Habanero Bombs)",
            "Scotch Bonnet": "The edgy, rebellious spirits of Io. They are preferred by the younger generation and are known for their love of freedom and individuality.(+4 Aether and Strength, -1 Wisdom, +Fire Manipulation, +Supernova)",
            "Carolina Reaper": "The legendary, almost mythical pepper of Io. It is believed that they know the boundary between life and death, and they are revered by all Ionians.(+5 Strength and Aether, +Fire Manipulation, +Soul Siphon, +Carolina Scythe)"
        }
       
}}
# Colors for rarity tags
# Using hex color codes for better control over appearance
RARITY_COLORS = {


    "Common": "#9E9E9E",      # Grey
    "Uncommon": "#4CAF50",    # Green
    "Rare": "#2196F3",        # Blue
    "Epic": "#9C27B0",        # Purple
    "Legendary": "#FF9800",   # Orange
    "Divine": "#FFD700",      # Gold
    "Weird": "#FF0357"        # Pink
}

archetype_data = {
    "Warrior": {
        "description": "Frontline fighter who excels in melee combat and resilience.",
        "boon": "+1 Strength and +1 Endurance",
        "rarity": "Common"
    },
    "Mage":{
        "description": "Uses Aether to a whole new level to unlock master more than one power",
        "boon": "+1 Intelligence and +1 Aether, gets 2 powers",
        "rarity": "Common"
    },
    "Tank": {
        "description": "Durable protector who absorbs damage. However, their mobility is reduced.",
        "boon": "+4 Endurance and +2 Resistance. -2 Agility",
        "rarity": "Common"
    },

    "Wizard":{"description": "Master of arcane arts, capable of casting powerful spells.",
              "boon": "+2 Intelligence and +2 Aether, gets 3 powers",
              "rarity": "Uncommon"},
    "Assassin":{"description": "Stealthy killer who excels at taking down targets quickly.",
                "boon": "+3 Agility, +2 Strength and +1 Endurance; gets Stealth",
                "rarity": "Uncommon"},
    "Healer":{"description": "Supportive magic user who specializes in healing and protection.",
              "boon": "+2 Wisdom, +2 Charisma and +2 Aether, ;gets Healing Light",
              "rarity": "Uncommon"},
    "Summoner":{"description": "Gets a partner that can be summoned to aid in battle.",
                "boon": "Boon depends on partner's abilities",
                "rarity": "Rare"},
    "Rider":{"description": "Gets a mountable partner to aid in battle.",
             "boon": "Boon depends on partner's abilities",
             "rarity": "Rare"},
    "Dual Wielder":{"description": "Expert in wielding two weapons simultaneously.",
                    "boon": "gets 2 Weapons",
                    "rarity": "Rare"},
    "Berserker":{"description": "Frenzied warrior who can easily overwhelm foes.",
                 "boon": "+4 strength, +2 Agility, +4 Endurance; Will win if there is a stat tie between him and his opponent",
                 "rarity": "Rare"},
    "Archmage":{"description": "Supreme magic user with unparalleled knowledge and aether.",
                "boon": "+3 Intelligence, +3 Wisdom and +3 Aether, gets 4 powers",
                "rarity": "Epic"},
    "Siphoner":{"description": "Drains energy from others to fuel their own powers.",
                "boon": "+2 Intelligence and +2 Aether, will temporarily siphon 3 stat points from its foe's best stat.",
                "rarity": "Epic"},
    "Gambler":{"description": "Risk-taker who relies on chance and luck to turn the tide of battle.",
               "boon": "Will gamble all of their stats. They can either get +2, +1, -1 or -2",
               "rarity": "Epic"},
    "Joker":{"description": "Trickster who uses deception and chaos to gain the upper hand.",
             "boon": "Has a 50% chance to reverse their own stats",
             "rarity": "Epic"},
    "Legendary Hero":{"description": "A hero of unmatched skill and bravery.",
                      "boon": "+3 in all stats; gets a random divine weapon",
                      "rarity": "Legendary"},
    "Cosmic Guardian":{"description": "Protector of the cosmos with immense power.",
                      "boon": "+3 in all stats; gets a random legendary weapon and power",
                      "rarity": "Legendary"},
    "Chosen One":{"description": "Destined hero with a unique fate.",
                  "boon": "+3 to all stats, gets a random divine power",
                  "rarity": "Legendary"}
}

# Determine rarity based on which list the item belongs to
from Fantasygenerator import (
    Common_weapons, Uncommon_weapons, Rare_weapons, Epic_weapons,
    Legendary_weapons, Divine_Weapons, Weird_weapons,
    Common_powers, Uncommon_powers, Rare_powers, Epic_powers,
    Legendary_powers, Divine_Powers, Weird_powers
)



def get_rarity(item):
    if item in Common_weapons or item in Common_powers:
        return "Common"
    elif item in Uncommon_weapons or item in Uncommon_powers:
        return "Uncommon"
    elif item in Rare_weapons or item in Rare_powers:
        return "Rare"
    elif item in Epic_weapons or item in Epic_powers:
        return "Epic"
    elif item in Legendary_weapons or item in Legendary_powers:
        return "Legendary"
    elif item in Divine_Weapons or item in Divine_Powers:
        return "Divine"
    elif item in Weird_weapons or item in Weird_powers:
        return "Weird"
    return "Common"

# Styled tag for rarity items
def rarity_tag(text):
    rarity = get_rarity(text)
    return ft.Container(
        content=ft.Text(text, color="white", size=12),
        bgcolor=RARITY_COLORS[rarity],
        padding=ft.padding.symmetric(horizontal=8, vertical=4),
        border_radius=8
    )

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


def assign_relationships():
    characters = load_characters()
    for char in characters:
        char["relationships"] = []

    for i, char1 in enumerate(characters):
        for j, char2 in enumerate(characters):
            if i >= j:
                continue
            sim = alignment_similarity(char1.get("alignment"), char2.get("alignment"))
            relation = pick_relationship(sim)
            char1["relationships"].append({"name": char2["name"], "type": relation})
            char2["relationships"].append({"name": char1["name"], "type": relation})

    save_characters(characters)
    print("Relationships assigned.")
    
def get_event_weight(event_name, event_data, char1, char2=None):
    weight = 1  # base chance

    # ===== Relationship-based weighting =====
    if char2:
        if "Rival" in event_data["desc"].lower():
            if any(r["name"] == char2["name"] and r["type"] in ["Rival", "Enemy"] for r in char1.get("relationships", [])):
                weight += 2
        if "Friend" in event_data["desc"] or "Ally" in event_data["desc"]:
            if any(r["type"] in ["Friend", "Ally"] for r in char1.get("relationships", [])):
                weight += 1

    # ===== Moral alignment weighting =====
    if char2:
        align1 = char1.get("moral_alignment")
        align2 = char2.get("moral_alignment")
        if align1 and align2:
            if align1.split()[1] == align2.split()[1]:  # same good/neutral/evil
                if "Friend" in event_data["desc"] or "Ally" in event_data["desc"]:
                    weight += 1
            elif "Betrayal" in event_name or "Enemy" in event_name:
                weight += 1

    # ===== Stat-based weighting =====
    if "Strength" in event_data["desc"] and char1.get("strength", 0) < 5:
        weight += 2
    if "Agility" in event_data["desc"] and char1.get("agility", 0) < 5:
        weight += 2

    # ===== Apply rare event story triggers =====
    weight *= rare_event_trigger(event_name, event_data, char1, char2)

    return weight

def rare_event_trigger(event_name, event_data, char1, char2=None):
    rarity = event_data.get("rarity", "").lower()
    multiplier = 1

    if rarity in ["very rare", "extremely rare"]:
        # === Positive rise-to-power triggers ===
        if "Divine Gift" in event_name or "Cosmic" in event_name:
            total_stats = sum(char1.get(stat, 0) for stat in ["strength", "agility", "endurance", "intelligence", "wisdom", "charisma", "resistance", "aether"])
            if total_stats >= 50:
                multiplier = 3
            else:
                multiplier = 0.2

        if "Betrayal" in event_name:
            if char2 and any(r["name"] == char2["name"] and r["type"] in ["Friend", "Ally"] for r in char1.get("relationships", [])):
                multiplier = 2
            else:
                multiplier = 0.1

        if "Legendary" in event_name:
            if char1.get("events_survived", 0) >= 10:
                multiplier = 2
            else:
                multiplier = 0.2

        # === Downward spiral triggers ===
        if "Catastrophic Failure" in event_name:
            avg_stat = sum(char1.get(stat, 0) for stat in ["strength", "agility", "endurance", "intelligence", "wisdom", "charisma", "resistance", "aether"]) / 8
            if avg_stat < 4:
                multiplier = 2.5
            else:
                multiplier = 0.5

        if "Joker's curse" in event_name:
            if random.random() < 0.1:  # still mostly rare
                multiplier = 1.5
            else:
                multiplier = 0.5

        if "Arm Injury" in event_name or "Leg Injury" in event_name or "Back Injury" in event_name:
            if char1.get("strength", 0) > 7 or char1.get("agility", 0) > 7:
                multiplier = 1.8  # injuries target the strong/agile more often

    return multiplier

def weighted_random_event(events_dict, char1, char2=None, debug=False):
    event_names = list(events_dict.keys())
    weights = []

    for name in event_names:
        w = get_event_weight(name, events_dict[name], char1, char2)
        weights.append(w)

    if debug:
        print("\n=== Weighted Event Chances ===")
        total_weight = sum(weights)
        for name, w in zip(event_names, weights):
            print(f"{name}: {round((w/total_weight)*100, 2)}% chance")

    # Weighted choice
    total = sum(weights)
    rand_val = random.uniform(0, total)
    current = 0
    for name, w in zip(event_names, weights):
        current += w
        if rand_val <= current:
            return name

# Character card
def character_card(data):
    return ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text(f"{data['name']} ({data['archetype']})", size=20, weight="bold"),
                ft.Text(f"Race: {data['race']} | Subrace: {data['subrace']}"),
                ft.Text(f"Moral Alignment: {data['moral_alignment']}"),
                ft.Divider(),
                ft.Text("Stats:", weight="bold"),
                ft.Row([ft.Text(f"{k.capitalize()}: {v}") for k, v in data["stats"].items()], wrap=True),
                ft.Divider(),
                ft.Text("Powers:", weight="bold"),
                ft.Row([rarity_tag(p) for p in data["powers"]], wrap=True),
                ft.Divider(),
                ft.Text("Weapons:", weight="bold"),
                ft.Row([rarity_tag(w) for w in data["weapons"]], wrap=True),
                ft.Divider(),
                ft.Text(f"Partner: {data['partner']}" if data["partner"] else "Partner: None"),
            ],
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True),
            padding=15
        )
    )

possible_duo_events = {
    "Blood Oath": {
        "desc": "A sacred vow between two characters. The two instantly become Close Friends and each gain 1 new power.",
        "rarity": "Very Rare",
        "effects": {
            "relationships": [{"type": "Close Friend", "target": "other"}],
            "powers": ["Power from event"]
        }
    },
    "Sworn enemies": {
        "desc": "Two characters meet and become enemies after an intense battle. They each get +1 Strength",
        "rarity": "Rare",
        "effects": {
            "relationships": [{"type": "Enemy", "target": "other"}],
            "stats": {"strength": 1}
        }
    },
    "Mentorship": {
        "desc": "The Solarian Sensei puts two characters together to teach the other and each gain +1 on the other's best stat.",
        "rarity": "Uncommon",
        "effects": {
            "special": "mentorship"
        }
    },
    "Betrayal": {
        "desc": "One character betrays the other, leading to both of them becoming enemies. The betrayed loses 1 charisma and the betrayer gains +1 wisdom.",
        "rarity": "Very Rare",
        "effects": {
            "relationships": [{"type": "Enemy", "target": "other"}],
            "special": "betrayal"  # handled in code
        }
    },
    "Birth of rivalry": {
        "desc": "During a tournament, two characters fight a fierce battle. Their relationship will become rivals. They each gain +1 Agility and +1 Strength.",
        "rarity": "Uncommon",
        "effects": {
            "relationships": [{"type": "Rival", "target": "other"}],
            "stats": {"agility": 1, "strength": 1}
        }
    },
    "Stat Trade": {
        "desc": "The characters agree to trade one of their stats. Each character gains +1 in the stat they receive and loses -1 in the stat they give.",
        "rarity": "Common",
        "effects": {
            "special": "stat_trade"
        }
    },
    "New Friend": {
        "desc": "Two characters hit it off well and become friends when they meet. +1 Charisma.",
        "rarity": "Uncommon",
        "effects": {
            "relationships": [{"type": "Friend", "target": "other"}],
            "stats": {"charisma": 1}
        }
    },
    "Cover my back": {
        "desc": "Two characters fight against a common enemy and win. They become friends and gain +2 Endurance.",
        "rarity": "Very Rare",
        "effects": {
            "relationships": [{"type": "Friend", "target": "other"}],
            "stats": {"endurance": 2}
        }
    },
    "Twin Blessing": {
        "desc": "Two characters gain a shared blessing, each receiving +1 to all of their stats.",
        "rarity": "Extremely Rare",
        "effects": {
            "special": "twin_blessing"
        }
    },
    "Weapon Trade": {
        "desc": "Two characters agree to trade weapons. They switch weapons permanently.",
        "rarity": "Very Rare",
        "effects": {
            "special": "weapon_trade"
        }
    },
    "Power Mentorship": {
        "desc": "Two characters will mentor each other, each learning one power from the other.",
        "rarity": "Very Rare",
        "effects": {
            "special": "power_mentorship"
        }
    },
    "Power Rivalry": {
        "desc": "Two characters will try to outdo each other, each gaining +1 in Endurance and Resistance.",
        "rarity": "Rare",
        "effects": {
            "stats": {"endurance": 1, "resistance": 1}
        }
    },
    "Aether Crusade": {
        "desc": "Two characters embark on a quest to harness the power of Aether. Each gains +1 Aether and a new power. They become Friends.",
        "rarity": "Very Rare",
        "effects": {
            "relationships": [{"type": "Friend", "target": "other"}],
            "stats": {"aether": 1},
            "powers": ["Power from event"]
        }
    }
}

possible_single_event = {
    "Merkarian Boulder Lifting": {
        "desc": "The character trains using the Merkarian technique to lift heavy boulders, gaining +2 Strength.",
        "rarity": "Common",
        "effects": {"stats": {"strength": 2}}
    },
    "Saturnian Aerobatics": {
        "desc": "The character learns incredible Saturn-style aerial maneuvers, gaining +2 Agility.",
        "rarity": "Common",
        "effects": {"stats": {"agility": 2}}
    },
    "Neptune Waterfall Focus": {
        "desc": "The character focuses on the cascading waters of Neptune, gaining +2 Endurance.",
        "rarity": "Common",
        "effects": {"stats": {"endurance": 2}}
    },
    "Lunar Aether Dance": {
        "desc": "The character learns to harness the power of the moon, gaining +2 Aether.",
        "rarity": "Common",
        "effects": {"stats": {"aether": 2}}
    },
    "Jupiter Library Study": {
        "desc": "The character studies ancient texts in the Jupiter Library, gaining +2 Intelligence.",
        "rarity": "Common",
        "effects": {"stats": {"intelligence": 2}}
    },
    "Mars Wisdom Program": {
        "desc": "The character participates in the Mars Wisdom Program, gaining +2 Wisdom.",
        "rarity": "Common",
        "effects": {"stats": {"wisdom": 2}}
    },
    "Watch a Plutonian movie": {
        "desc": "The character watches a classic Plutonian film, gaining +2 Charisma.",
        "rarity": "Common",
        "effects": {"stats": {"charisma": 2}}
    },
    "Venus Lava Trial": {
        "desc": "The character undergoes the Venus Lava Trial, gaining +2 Resistance.",
        "rarity": "Common",
        "effects": {"stats": {"resistance": 2}}
    },
    "All-around Earth Training": {
        "desc": "The character engages in a comprehensive training regimen on Earth, gaining +1 to all stats.",
        "rarity": "Rare",
        "effects": {"stats": {s: 1 for s in ["strength","agility","endurance","intelligence","wisdom","charisma","resistance","aether"]}}
    },
    "Arm Injury": {
        "desc": "The character sustains an arm injury, resulting in -1 Strength and -1 Agility.",
        "rarity": "Uncommon",
        "effects": {"stats": {"strength": -1, "agility": -1}}
    },
    "Leg Injury": {
        "desc": "The character sustains a leg injury, resulting in -1 Agility and -1 Endurance.",
        "rarity": "Uncommon",
        "effects": {"stats": {"agility": -1, "endurance": -1}}
    },
    "Back Injury": {
        "desc": "The character sustains a back injury, resulting in -1 Strength and -1 Endurance.",
        "rarity": "Uncommon",
        "effects": {"stats": {"strength": -1, "endurance": -1}}
    },
    "Ionian Dancing Class": {
        "desc": "The character takes a dancing class, gaining +1 Agility and +1 Charisma.",
        "rarity": "Uncommon",
        "effects": {"stats": {"agility": 1, "charisma": 1}}
    },
    "Meditation Retreat": {
        "desc": "The character attends a meditation retreat, gaining +1 Wisdom and +1 Aether.",
        "rarity": "Uncommon",
        "effects": {"stats": {"wisdom": 1, "aether": 1}}
    },
    "Tritonian Chess Boxing": {
        "desc": "The character participates in chess boxing, gaining +1 Strength and +1 Intelligence.",
        "rarity": "Uncommon",
        "effects": {"stats": {"strength": 1, "intelligence": 1}}
    },
    "Ganymedan Mental Fortitude Training": {
        "desc": "The character undergoes rigorous mental training, gaining +1 Wisdom and +1 Intelligence.",
        "rarity": "Uncommon",
        "effects": {"stats": {"wisdom": 1, "intelligence": 1}}
    },
    "Chronic Headache": {
        "desc": "The character suffers from a chronic headache, resulting in -1 Intelligence and -1 Wisdom.",
        "rarity": "Uncommon",
        "effects": {"stats": {"intelligence": -1, "wisdom": -1}}
    },
    "Romantic Rejection": {
        "desc": "The character experiences a romantic rejection, resulting in -1 Charisma and -1 Aether.",
        "rarity": "Uncommon",
        "effects": {"stats": {"charisma": -1, "aether": -1}}
    },
    "Food Poisoning": {
        "desc": "The character suffers from food poisoning, resulting in -1 Endurance and -1 Resistance.",
        "rarity": "Uncommon",
        "effects": {"stats": {"endurance": -1, "resistance": -1}}
    },
    "Power Awakening": {
        "desc": "The character undergoes a power awakening, gaining a new power.",
        "rarity": "Rare",
        "effects": {"powers": ["Power from event"]}
    },
    "Cosmic Meditation": {
        "desc": "The character meditates under the stars, gaining +1 Charisma, +1 Intelligence, +1 Aether, and +1 Wisdom.",
        "rarity": "Rare",
        "effects": {"stats": {"charisma": 1, "intelligence": 1, "aether": 1, "wisdom": 1}}
    },
    "Cosmic Physical Training": {
        "desc": "The character trains under cosmic rays, gaining +1 Strength, +1 Resistance, +1 Agility, and +1 Endurance.",
        "rarity": "Rare",
        "effects": {"stats": {"strength": 1, "resistance": 1, "agility": 1, "endurance": 1}}
    },
    "Double Trouble": {
        "desc": "The character finds a second weapon and changes the archetype to Dual Wielder.",
        "rarity": "Very Rare",
        "effects": {"weapons": ["Second Weapon from event"], "archetype": "Dual Wielder"}
    },
    "Catastrophic Failure": {
        "desc": "The character experiences a catastrophic failure, resulting in -2 to all stats.",
        "rarity": "Very Rare",
        "effects": {"stats": {s: -2 for s in ["strength","agility","endurance","intelligence","wisdom","charisma","resistance","aether"]}}
    },
    "Lone Wolf bargain": {
        "desc": "The character embraces solitude. Loses all relationship but gains +3 in all stats.",
        "rarity": "Very Rare",
        "effects": {"clear_relationships": True, "stats": {s: 3 for s in ["strength","agility","endurance","intelligence","wisdom","charisma","resistance","aether"]}}
    },
    "I have no enemies": {
        "desc": "The character has no enemies, removes all bad relationships.",
        "rarity": "Very Rare",
        "effects": {"remove_bad_relationships": True}
    },
    "Joker's curse": {
        "desc": "The character is cursed by the Joker, causing all of their stats to be reversed.",
        "rarity": "Very Rare",
        "effects": {"special": "reverse_stats"}
    },
    "Change of Morals": {
        "desc": "The character undergoes a significant change in morals, randomly changes their moral alignment.",
        "rarity": "Very Rare",
        "effects": {"alignment": "random"}
    },
    "Alice in Wonderland?": {
        "desc": "The character drinks a mysterious potion, completely changing their height.",
        "rarity": "Very Rare",
        "effects": {"special": "change_height"}
    },
    "Cosmic Blessing": {
        "desc": "The character receives a cosmic blessing, gaining +2 to all stats and a new Legendary power.",
        "rarity": "Extremely Rare",
        "effects": {"stats": {s: 2 for s in ["strength","agility","endurance","intelligence","wisdom","charisma","resistance","aether"]}, "powers": ["Legendary Power from event"]}
    },
    "Divine Gift": {
        "desc": "The character receives a divine gift, a new Divine power.",
        "rarity": "Extremely Rare",
        "effects": {"powers": ["Divine Power from event"]}
    }
}
# Weighted rarity for event picking
RARITY_WEIGHTS = {
    "Common": 50,
    "Uncommon": 30,
    "Rare": 15,
    "Very Rare": 5,
    "Extremely Rare": 1
}

# Valid stats
STAT_NAMES = ["strength", "agility", "endurance", "intelligence", "wisdom", "charisma", "resistance", "aether"]
def pick_random_event(events_dict):
    """Pick a random event from a dict based on rarity."""
    pool = []
    for name, data in events_dict.items():
        weight = RARITY_WEIGHTS.get(data["rarity"].strip(), 1)
        pool.extend([name] * weight)
    return random.choice(pool)

def apply_effects(char, effects, other_char=None):
    message=""
    # Apply stat changes
    if "stats" in effects:
        for stat, change in effects["stats"].items():
            char.get("stats", {})[stat] += change
            message+=f"{char['name']}'s {stat}: has changed by {change}.\n"
            message+=f"{char['name']}'s {stat}: is now {char.get('stats', {})[stat]}.\n"

    # Add powers
    if "powers" in effects:
        # We pick a random power from all the lists and we make sure that the character does not already have that power
        if effects["powers"] == "Power from event":
            new_power = get_random_power()
            while new_power in char.get("powers", []):
                new_power = get_random_power()
            char.setdefault("powers", []).append(new_power)
        elif effects["powers"] == "Divine Power from event":
            new_power = get_random_divine_power()
            while new_power in char.get("powers", []):
                new_power = get_random_divine_power()
            char.setdefault("powers", []).append(new_power)
        message+=f"{char['name']}'s powers: has gotten the powers: {new_power}.\n"

    # Add weapons
    if "weapons" in effects:
        # We pick a random weapon from all the lists
        if effects["weapons"] == "Second Weapon from event":
            new_weapon = get_random_weapon()
            char.setdefault("weapons", []).append(new_weapon)
        message+=f"{char['name']}'s weapons: has gotten the weapons: {new_weapon}.\n"
        

    # Change archetype
    if "archetype" in effects:
        char["archetype"] = effects["archetype"]
        message+=f"{char['name']}'s archetype: has changed to {effects['archetype']}.\n"
        

    # Change alignment
    if "alignment" in effects:
        if effects["alignment"] == "random":
            char["moral_alignment"] = random.choice([
                "Lawful Good", "Neutral Good", "Chaotic Good",
                "Lawful Neutral", "True Neutral", "Chaotic Neutral",
                "Lawful Evil", "Neutral Evil", "Chaotic Evil"
            ])
            message+=f"{char['name']}'s moral alignment: has changed to {char['moral_alignment']}.\n"
        else:
            char["moral_alignment"] = effects["alignment"]
            message+=f"{char['name']}'s moral alignment: has changed to {char['moral_alignment']}.\n"
            

    # Relationships
    if "relationships" in effects and other_char:
        char.setdefault("relationships", [])

        for rel in effects["relationships"]:
            existing_rel = None
            for r in char["relationships"]:
                if r["name"] == other_char["name"]:
                    existing_rel = r["type"]
                    break

            # Friend/Close Friend restriction
            if rel["type"] in ["Friend", "Close Friend"]:
                if existing_rel in ["Friend", "Close Friend"]:
                    message+=f"{char['name']}'s relationships: already has a friendly relationship with {other_char['name']}.\n"
                    continue  # Already friendly, skip adding
                

            # Rival restriction
            if rel["type"] == "Rival":
                if existing_rel in ["Rival", "Enemy"]:
                    message+=f"{char['name']}'s relationships: already has a rival or enemy relationship with {other_char['name']}.\n"
                    continue  # Already bad, skip adding

            # Enemy restriction
            if rel["type"] == "Enemy":
                if existing_rel == "Enemy":
                    message+=f"{char['name']}'s relationships: already has an enemy relationship with {other_char['name']}.\n"
                    continue  # Already enemy, skip adding

            # If no restriction blocks it, set/update relationship
            # Remove old entry if exists
            char["relationships"] = [r for r in char["relationships"] if r["name"] != other_char["name"]]
            # Add new one
            char["relationships"].append({
                "name": other_char["name"],
                "type": rel["type"]
            })

            message+=f"{char['name']}'s relationships: has gotten the relationship: {rel['type']}.\n"
    # Clear all relationships
    if effects.get("clear_relationships"):
        # We make all relationship values are equal to not met
        for rel in char.get("relationships", []):
            rel["type"] = "Have not met"
        message+=f"{char['name']}'s relationships: has cleared all relationships.\n"

    # Remove only bad relationships
    if effects.get("remove_bad_relationships") and "relationships" in char:
        # We change all "Enemy" and "Rival" relationships to "Have not met"
        for rel in char["relationships"]:
            if rel["type"] in ["Enemy", "Rival"]:
                rel["type"] = "Have not met"
        message+=f"{char['name']}'s relationships: has removed bad relationships.\n"  
    if "special" in effects:
        if effects["special"] == "mentorship" and other_char:
            # We make a new list of stats besides the height
            new_stats = {k: v for k, v in char.get("stats", {}).items() if k != "height"}
            best_stat = max(new_stats, key=new_stats.get, default=None)
            if isinstance(other_char.get("stats", {}).get(best_stat), int):
                char.get("stats", {})[best_stat] += 1
                message+=f"{char['name']}'s {best_stat}: has increased by 1 due to mentorship.\n"

        elif effects["special"] == "betrayal" and other_char:
            # First character is betrayed
            char.get("stats", {})["charisma"] -= 1
            # Second character (betrayer) gets wisdom
            other_char.get("stats", {})["wisdom"] += 1
            message+=f"{char['name']}'s charisma: has decreased by 1 due to betrayal.\n"
            message+=f"{char['name']}'s wisdom is now {char.get('stats', {})['wisdom']}.\n"
            message+=f"{other_char['name']}'s wisdom: has increased by 1 due to betrayal.\n"
            message+=f"{other_char['name']}'s wisdom is now {other_char.get('stats', {})['wisdom']}.\n"

        elif effects["special"] == "stat_trade" and other_char:
            victor, loser = (char, other_char) if random.random() < 0.5 else (other_char, char)
            stat = random.choice(["strength","agility","endurance","intelligence","wisdom","charisma","resistance","aether"])
            victor.get("stats", {})[stat] += 1
            loser.get("stats", {})[stat] -= 1
            message+=f"{victor['name']}'s {stat}: has increased by 1 due to enemy victory.\n"
            message+=f"{victor['name']}'s {stat}: is now {victor.get('stats', {})[stat]}.\n"
            message+=f"{loser['name']}'s {stat}: has decreased by 1 due to enemy victory.\n"
            message+=f"{loser['name']}'s {stat}: is now {loser.get('stats', {})[stat]}.\n"

        elif effects["special"] == "twin_blessing" and other_char:
            for stat in ["strength","agility","endurance","intelligence","wisdom","charisma","resistance","aether"]:
                char.get("stats", {})[stat] += 1
                other_char.get("stats", {})[stat] += 1
                message+=f"{char['name']}'s {stat}: has increased by 1 due to twin blessing.\n"
                message+=f"{other_char['name']}'s {stat}: has increased by 1 due to twin blessing.\n"
            message+=f"{char['name']}'s stats: {char.get('stats', {})}\n"
            message+=f"{other_char['name']}'s stats: {other_char.get('stats', {})}\n"

        elif effects["special"] == "weapon_trade" and other_char:
            char["weapons"], other_char["weapons"] = other_char.get("weapons", []), char.get("weapons", [])
            message+=f"{char['name']}'s weapons: has traded with {other_char['name']}'s weapons.\n"
            message+=f"{char['name']}'s weapons: {char.get('weapons', [])}\n"
            message+=f"{other_char['name']}'s weapons: {other_char.get('weapons', [])}\n"


        elif effects["special"] == "power_mentorship" and other_char:
            if char.get("powers") and other_char.get("powers"):
                char["powers"].append(random.choice(other_char["powers"]))
                other_char["powers"].append(random.choice(char["powers"]))
                message+=f"{char['name']}'s powers: has learned a power from {other_char['name']}: {char['powers'][-1]}\n"
                message+=f"{other_char['name']}'s powers: has learned a power from {char['name']}: {other_char['powers'][-1]}\n"

        elif effects["special"] == "reverse_stats":
            for stat in ["strength","agility","endurance","intelligence","wisdom","charisma","resistance","aether"]:
                char.get("stats", {})[stat] = 15-char.get("stats", {})[stat]
                message+=f"{char['name']}'s {stat}: has been reversed.\n"
                message+=f"{char['name']}'s {stat}: is now {char.get('stats', {})[stat]}.\n"

        elif effects["special"] == "change_height":
            char["height"] = random.randint(0, 500)
            message+=f"{char['name']}'s height: has been changed to {char.get('height', 'unknown')} cm.\n"
    return message

def trigger_random_event(debug=False):
    characters = load_characters()
    if not characters:
        return "No characters available."

    if len(characters) >= 2 and random.random() < 0.4:
        char1, char2 = random.sample(characters, 2)
        event_name = weighted_random_event(possible_duo_events, char1, char2, debug=debug)
        event_data = possible_duo_events[event_name]
        message1=apply_effects(char1, event_data["effects"], char2)
        message2=apply_effects(char2, event_data["effects"], char1)
        save_characters(characters)
        return message1,message2,f"Duo Event: {event_name}\n{event_data['desc']}\n Character 1: {char1['name']}\n Character 2: {char2['name']}"
    else:
        char = random.choice(characters)
        event_name = weighted_random_event(possible_single_event, char,debug=debug)
        event_data = possible_single_event[event_name]
        message=apply_effects(char, event_data["effects"])
        save_characters(characters)
        return message,"",f"Single Event: {event_name}\n{event_data['desc']}"




# Flet main UI
def main(page: ft.Page):
    page.title = "Fantasy Character Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_maximized = True
    page.theme_mode = ft.ThemeMode.DARK

    # Create character tab
    name_field = ft.TextField(label="Character Name", width=300)
    create_output = ft.Column()

    def create_character(e):
        if not name_field.value.strip():
            create_output.controls = [ft.Text("Please enter a name!", color="red")]
        else:
            c = Character(name_field.value.strip())
            data = c.create_character()
            create_output.controls = [character_card(data)]
        page.update()

    create_tab = ft.Column([
        ft.Row([name_field, ft.ElevatedButton("Generate", on_click=create_character)]),
        create_output
    ])
    def build_leaderboards():
        characters = load_characters()
        if not characters:
            return ft.Text("No characters saved yet.")

        stats = ["strength", "agility", "endurance", "aether", "wisdom", "intelligence", "charisma", "resistance"]
        leaderboard_controls = []
        
        medal_colors = {
            1: "#FFD700",
            2: "#C0C0C0",
            3: "#F0B377"
        }

        for stat in stats:
            sorted_chars = sorted(characters, key=lambda c: c["stats"][stat], reverse=True)[:3]
            leaderboard_controls.append(ft.Text(stat.capitalize(), size=16, weight="bold"))
            for i, char in enumerate(sorted_chars, start=1):
                leaderboard_controls.append(
                    ft.Text(f"{i}. {char['name']} - {char['stats'][stat]}", color=medal_colors.get(i))
                )
            leaderboard_controls.append(ft.Divider())

        return ft.Column(leaderboard_controls, scroll="auto")
    
    reset_leaderboard = ft.ElevatedButton("Reset Leaderboards", on_click=build_leaderboards)


    leaderboard_tab = ft.Column([reset_leaderboard, build_leaderboards()], scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def build_alignment_grid():
        chars = load_characters()
        alignment_colors = {
            "Lawful Good": "#4CAF50",      # Green
            "Neutral Good": "#8BC34A",     # Light Green
            "Chaotic Good": "#CDDC39",     # Lime
            "Lawful Neutral": "#FFEB3B",   # Yellow
            "True Neutral": "#FFC107",     # Amber
            "Chaotic Neutral": "#FF9800",  # Orange
            "Lawful Evil": "#F44336",      # Red
            "Neutral Evil": "#E91E63",     # Pink
            "Chaotic Evil": "#9C27B0"       # Purple
        }
        alignments_order = [
            ["Lawful Good", "Neutral Good", "Chaotic Good"],
            ["Lawful Neutral", "True Neutral", "Chaotic Neutral"],
            ["Lawful Evil", "Neutral Evil", "Chaotic Evil"]
        ]

        grid_rows = []

        for row in alignments_order:
            row_cells = []
            for alignment in row:
                aligned_chars = [c["name"] for c in chars if c["moral_alignment"] == alignment]
                if aligned_chars:
                    char_list = ft.Column([ft.Text(name, color="black") for name in aligned_chars], scroll="auto")
                else:
                    char_list = ft.Text("None", italic=True, color="black")
                
                cell = ft.Container(
                    content=ft.Column([
                        ft.Text(alignment, weight="bold", size=14,color="black"),
                        char_list
                    ]),
                    border=ft.border.all(1, "black"),
                    padding=10,
                    width=200,
                    height=200,
                    bgcolor=alignment_colors.get(alignment, "#FFFFFF"),
                )
                row_cells.append(cell)
            grid_rows.append(ft.Row(row_cells, alignment="spaceAround"))

        return ft.Column(grid_rows, scroll="auto")

    reset_moral_alignment = ft.ElevatedButton("Reset Moral Alignment", on_click=lambda e: build_alignment_grid())
    alignment_tab = ft.Column([
        ft.Text("Moral Alignment Distribution", size=20, weight="bold"),
        build_alignment_grid(),
        reset_moral_alignment
    ])

  # View characters tab
    view_output = ft.Column()

    def load_characters_view(e=None):
        chars = load_characters()
        if not chars:
            view_output.controls = [ft.Text("No characters saved yet.")]
        else:
            view_output.controls = [character_card(c) for c in chars]
        page.update()

    view_tab = ft.Column([
        ft.ElevatedButton("Refresh List", on_click=load_characters_view),
        view_output
    ],
    scroll=ft.ScrollMode.ALWAYS,
        expand=True)

    # Battle simulator tab
    chars_list = load_characters()
    names = [c["name"] for c in chars_list]

    dropdown1 = ft.Dropdown(label="Character 1", options=[ft.dropdown.Option(n) for n in names], width=200)
    dropdown2 = ft.Dropdown(label="Character 2", options=[ft.dropdown.Option(n) for n in names], width=200)
    # this will show the battle results
    battle_result = ft.Column(scroll=ft.ScrollMode.ALWAYS)



    # Function to run the battle simulation
    def run_battle(e):
        result = simulate_battle_ui(dropdown1.value, dropdown2.value)
        if not result:
            battle_result.controls = [ft.Text("One or both characters not found.", color="red")]
            page.update()
            return

        char1 = result["char1"]
        char2 = result["char2"]
        comparison = result["comparison"]

        # Build stats comparison table
        stats_table = []
        for stat, winner in comparison.items():
            c1_color = "green" if winner == 1 else "orange" if winner == 0 else None
            c2_color = "green" if winner == 2 else "orange" if winner == 0 else None
            c1_text_color="black" if winner ==1 else "white"
            c2_text_color="black" if winner ==2 else "white"
            if stat == "powers" or stat == "weapons":

                stats_table.append(
                    ft.Row([
                        ft.Container(ft.Text(str(char1[stat]),color=c1_text_color), bgcolor=c1_color, padding=5, width=300),
                        ft.Text(stat.capitalize(), weight="bold",width=80),
                        ft.Container(ft.Text(str(char2[stat]),color=c2_text_color), bgcolor=c2_color, padding=5, width=300)
                    ])
                )
            else:
                
                stats_table.append(
                    ft.Row([
                        ft.Container(ft.Text(str(char1["stats"][stat]),color=c1_text_color), bgcolor=c1_color, padding=5, width=300),
                        ft.Text(stat.capitalize(), weight="bold",width=80),
                        ft.Container(ft.Text(str(char2["stats"][stat]),color=c2_text_color), bgcolor=c2_color, padding=5, width=300)
                    ])
                )

        battle_result.controls = [
            ft.Text(f"{char1['name']} vs {char2['name']}", size=18, weight="bold"),
            ft.Row([ft.Text(f"Points: {result['points'][0]}"), ft.Text(f"Points: {result['points'][1]}")]),
            ft.Row([
                ft.Column([ft.Text(char1["name"], weight="bold")]),
                ft.Column(stats_table),
                ft.Column([ft.Text(char2["name"], weight="bold")])
            ]),
            ft.Text(f"Winner: {result['winner']}", size=20, weight="bold", color="green" if result['winner'] != "Draw" else "yellow"),
            ft.Text(f"Diff: {result['diff']}", size=16, weight="bold", color="blue"),
        ]
        page.update()
        
    battle_tab = ft.Column([
        ft.Row([dropdown1, dropdown2],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("Fight!", on_click=run_battle)],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([battle_result],alignment=ft.MainAxisAlignment.CENTER)
    ],
        scroll=ft.ScrollMode.ALWAYS,
        expand=True,
    )
    
    def build_bestiary_tab(page: ft.Page):

        search_field = ft.TextField(label="Search races or subraces...", width=500)
        content_column = ft.Column(scroll="auto", expand=True)

        # small helper to create a nice avatar for race (initials)
        def race_avatar(name):
            initials = "".join([p[0].upper() for p in name.split()[:2]])
            return ft.CircleAvatar(content=ft.Text(initials, weight="bold"), bgcolor=ft.colors.PRIMARY_CONTAINER, radius=28)

        # Build single race expander
        def build_race_expander(race_name, race_info, characters):
            # header row (avatar + name + short desc)
            header = ft.Row([
                race_avatar(race_name),
                ft.Column([
                    ft.Text(race_name, size=18, weight="bold"),
                    ft.Text(race_info.get("description", ""), size=12, color=ft.colors.ON_SURFACE_VARIANT)
                ], tight=True)
            ], alignment="start", spacing=12)

            # subraces area: a grid/list of cards
            subrace_controls = []
            for subrace_name, subrace_desc in race_info.get("subraces", {}).items():
                # find known members for this subrace
                known = [c for c in characters if c["race"] == race_name and c["subrace"] == subrace_name]
                # small member chips
                if known:
                    members_row = ft.Row([ft.Container(ft.Text(m["name"], size=12), padding=ft.padding.symmetric(8,4), border_radius=8, bgcolor="#222") for m in known], wrap=True)
                else:
                    members_row = ft.Text("No known members yet.", italic=True, color="grey")

                card = ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(subrace_name, weight="bold"),
                            ft.Text(subrace_desc, size=12),
                            ft.Divider(),
                            ft.Text("Known Members:", size=12, weight="bold"),
                            members_row
                        ]),
                        padding=10
                    ),
                    margin=ft.margin.all(6),
                    elevation=2
                )
                subrace_controls.append(card)

            # layout: subraces on a horizontal scroll area (wrap)
            subraces_layout = ft.Container(
                content=ft.Row(subrace_controls, wrap=True),
                padding=ft.padding.only(top=8, bottom=8)
            )

            # assemble expander
            exp = ft.ExpansionTile(
                title=header,
                controls=[subraces_layout],
                expand=False,
            )
            return exp

        # refresh function to rebuild content based on search filter
        def refresh_bestiary(e=None):
            q = (search_field.value or "").strip().lower()
            characters = load_characters()
            content_column.controls.clear()

            # sort races alphabetically for stable UI
            for race_name in bestiary_data.keys():
                race_info = bestiary_data[race_name]
                # filter by race or any subrace if query present
                if q:
                    # check race name or any subrace name/desc contains q
                    match = q in race_name.lower() or any(q in sr.lower() for sr, desc in race_info.get("subraces", {}).items())
                    if not match:
                        continue

                exp = build_race_expander(race_name, race_info, characters)
                content_column.controls.append(exp)

            if not content_column.controls:
                content_column.controls.append(ft.Text("No races match your search.", italic=True))
            page.update()

        # initial build
        refresh_bestiary()

        # wire search to refresh on change/enter
        search_field.on_change = refresh_bestiary
        search_field.on_submit = refresh_bestiary

        # top row: search + refresh button + optional legend
        top_row = ft.Row([
            search_field,
            ft.ElevatedButton("Refresh Known Members", on_click=refresh_bestiary),
            ft.Text("Bestiary", size=16, weight="bold", color=ft.colors.ON_SURFACE_VARIANT)
        ], alignment="spaceBetween", vertical_alignment="center")

        return ft.Column([top_row, ft.Divider(), content_column], expand=True)
    


    def build_weapon_power_tab():
        characters = load_characters()

        # Rarity order and color mapping
        rarities_order = ["Common", "Uncommon", "Rare", "Weird", "Epic", "Legendary", "Divine"]
        rarity_colors = {
            "Common": "#A0A0A0",
            "Uncommon": "#2ECC71",
            "Rare": "#3498DB",
            "Weird": "#9B59B6",
            "Epic": "#F1C40F",
            "Legendary": "#E67E22",
            "Divine": "#E74C3C"
        }

        # Map rarity to weapon and power lists from generator
        weapon_rarity_map = {
            "Common": Common_weapons,
            "Uncommon": Uncommon_weapons,
            "Rare": Rare_weapons,
            "Weird": Weird_weapons,
            "Epic": Epic_weapons,
            "Legendary": Legendary_weapons,
            "Divine": Divine_Weapons
        }

        power_rarity_map = {
            "Common": Common_powers,
            "Uncommon": Uncommon_powers,
            "Rare": Rare_powers,
            "Weird": Weird_powers,
            "Epic": Epic_powers,
            "Legendary": Legendary_powers,
            "Divine": Divine_Powers
        }

        # Build dictionary with all items + known members
        weapons_by_rarity = {r: {w: [] for w in sorted(weapon_rarity_map[r])} for r in rarities_order}
        powers_by_rarity = {r: {p: [] for p in sorted(power_rarity_map[r])} for r in rarities_order}

        # We get the weapon of the character and add them to the weapon's known users
        for char in characters:
            for weapon in char.get("weapons", []):
                weapon_rarity=[key for key, val in weapon_rarity_map.items() if weapon in val][0]
                if weapon in weapons_by_rarity[weapon_rarity]:
                    weapons_by_rarity[weapon_rarity][weapon].append(char["name"])

            for power in char.get("powers", []):
                rarity = [key for key, val in power_rarity_map.items() if power in val][0]
                if power in powers_by_rarity[rarity]:
                    powers_by_rarity[rarity][power].append(char["name"])
            
        def get_color_based_on_user_count(count):
            if count==0:
                return ft.colors.WHITE
            else:
                return ft.colors.BLACK

        # Helper to build a rarity section
        def build_section(title, data_dict):
            rarity_cards = []
            for rarity in rarities_order:
                items = data_dict[rarity]
                cards = []
                for item_name, users in items.items():
                    cards.append(
                        ft.Container(
                            content=ft.Column([
                                ft.Text(item_name, weight="bold"),
                                ft.Text(
                                    f"Used by: {', '.join(users)}" if users else "No known users yet",
                                    size=12, color=get_color_based_on_user_count(len(users))
                                )
                            ]),
                            padding=10,
                            bgcolor="#222",
                            border_radius=8,
                            margin=ft.margin.all(4)
                        )
                    )
                rarity_cards.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(rarity, size=16, weight="bold", color="white"),
                            ft.Row(cards, wrap=True)
                        ]),
                        bgcolor=rarity_colors[rarity],
                        border_radius=10,
                        padding=10,
                        margin=ft.margin.only(bottom=10),
                        width=1000,
                    )
                )
            
            return ft.Column([ft.Text(title, size=20, weight="bold")] + rarity_cards, scroll="auto")

        # Layout: two columns (Weapons | Powers)
        return ft.Column([
            ft.ElevatedButton("Refresh", on_click=build_weapon_power_tab),
            ft.Row([
                ft.Container(content=build_section("Weapons by Rarity", weapons_by_rarity), expand=True, padding=10),
                ft.Container(content=build_section("Powers by Rarity", powers_by_rarity), expand=True, padding=10)
            ], expand=True)])
    def build_archetype_tab():
        characters = load_characters()
        archetypes = archetype_data.keys()
        rarity_color_dictionary = {
            "Common": ft.colors.GREY,
            "Uncommon": ft.colors.GREEN,
            "Rare": ft.colors.BLUE,
            "Epic": ft.colors.PURPLE,
            "Legendary": ft.colors.ORANGE
        }
        archetype_boons = {arch: archetype_data[arch]["boon"] for arch in archetypes}
        archetype_rarities = {arch: archetype_data[arch]["rarity"] for arch in archetypes}
        archetype_descriptions = {arch: archetype_data[arch]["description"] for arch in archetypes}
        for arch in archetypes:
            boon = archetype_boons.get(arch, "No boon info yet")
            description = archetype_descriptions.get(arch, "No description available.")
            archetype_data[arch] = {"description": description, "boon": boon}

        content = []
        for name, info in archetype_data.items():
            # Find known members with this archetype
            members = [c["name"] for c in characters if c.get("archetype") == name]
            members_text = ", ".join(members) if members else "No known members yet"

            tile = ft.ExpansionTile(
                title=ft.Column([
                    ft.Text(name, size=18, weight="bold", color=rarity_color_dictionary[archetype_rarities[name]]),
                    ft.Text(f"Boon: {info['boon']}", size=12, color=ft.colors.ON_SURFACE_VARIANT)
                ], spacing=2),
                controls=[
                    ft.Text(info["description"], size=14),
                    ft.Divider(),
                    ft.Text(f"Rarity: {archetype_rarities[name]}", size=12, color=rarity_color_dictionary[archetype_rarities[name]]),
                    ft.Divider(),
                    ft.Text(f"Known Members: {members_text}", size=12, italic=True)
                ],
                initially_expanded=False
            )
            content.append(tile)

        return ft.Column(content, scroll="auto", expand=True)
    
    def build_tournament_tab():
        characters = load_characters()
        selected_names = []

        # Dropdown for selecting characters
        char_checkboxes = []
        for char in characters:
            cb = ft.Checkbox(label=char["name"], value=False)
            char_checkboxes.append(cb)

        select_all_checkbox = ft.Checkbox(label="Select All", value=False)

        def toggle_select_all(e):
            for cb in char_checkboxes:
                cb.value = select_all_checkbox.value
            page.update()

        select_all_checkbox.on_change = toggle_select_all

        results_display = ft.Column(scroll="auto", expand=True)

        def run_tournament(e):
            chosen = [cb.label for cb in char_checkboxes if cb.value]
            if len(chosen) < 2:
                results_display.controls = [ft.Text("Select at least 2 characters!", color="red")]
                page.update()
                return

            round_num = 1
            participants = chosen[:]
            round_results = []

            while len(participants) > 1:
                random.shuffle(participants)
                next_round = []
                round_log = [ft.Text(f"--- Round {round_num} ---", weight="bold")]

                for i in range(0, len(participants), 2):
                    if i + 1 >= len(participants):
                        # Odd one out gets a bye
                        winner = participants[i]
                        round_log.append(ft.Text(f"{winner} gets a bye"))
                        next_round.append(winner)
                    else:
                        p1, p2 = participants[i], participants[i+1]
                        winner = simulate_battle_ui(p1, p2)['winner']
                        if winner==None or winner == "Draw":
                            # We choose a random winner
                            winner = random.choice([p1, p2])
                            # We alert the tie and
                            round_log.append(ft.Text(f"{p1} vs {p2} → It's a tie! Choosing randomly: The winner is {winner}"))
                        else:
                            round_log.append(ft.Text(f"{p1} vs {p2} → Winner: {winner}"))
                        next_round.append(winner)

                round_results.append(ft.Column(round_log, spacing=2))
                participants = next_round
                round_num += 1

            # Final winner
            final_winner = participants[0]
            round_results.append(ft.Text(f"🏆 Champion: {final_winner} 🏆", size=18, weight="bold", color="gold"))

            results_display.controls = round_results
            page.update()

        start_button = ft.ElevatedButton("Start Tournament", on_click=run_tournament)
    

        return ft.Column([
            ft.Text("Select Participants:", size=16, weight="bold"),
            select_all_checkbox,
            ft.Column(char_checkboxes, scroll="auto", height=200),
            start_button,
            ft.Divider(),
            ft.Text("Tournament Results:", size=16, weight="bold"),
            results_display
        ], scroll="auto", expand=True)
    
    def build_relationships_tab(page):
        characters = load_characters()
        char_lookup = {c["name"]: c for c in characters}

        relationship_colors = {
            "Close Friend": "blue",
            "Friend": "lightgreen",
            "Rival": "orange",
            "Enemy": "red",
            "Have not met": "white"
        }

        details_display = ft.Column(scroll="auto", expand=True)

        def show_character_details(char_name):
            char = char_lookup[char_name]
            dialog = ft.AlertDialog(
                title=ft.Text(char["name"], size=20, weight="bold"),
                content=ft.Column([
                    ft.Text(f"Race: {char.get('race', 'Unknown')}"),
                    ft.Text(f"Subrace: {char.get('subrace', 'Unknown')}"),
                    ft.Text(f"Archetype: {char.get('archetype', 'Unknown')}"),
                    ft.Text(f"Alignment: {char.get('moral_alignment', 'Unknown')}"),
                    ft.Text(f"Weapons: {', '.join(char.get('weapons', []))}"),
                    ft.Text(f"Powers: {', '.join(char.get('powers', []))}"),
                ]),
                on_dismiss=lambda e: None
            )
            page.dialog = dialog
            dialog.open = True
            page.update()

        def load_relationships(e):
            selected_name = dropdown.value
            if not selected_name:
                return
            char = char_lookup[selected_name]
            details_display.controls.clear()

            for rel in char.get("relationships", []):
                rel_type = rel["type"]
                rel_name = rel["name"]
                details_display.controls.append(
                    ft.TextButton(
                        content=ft.Text(
                            f"{rel_name} ({rel_type})",
                            color=relationship_colors.get(rel_type, "white"),
                            weight="bold"
                        ),
                        on_click=lambda _, name=rel_name: show_character_details(name)
                    )
                )
            page.update()

        dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(c["name"]) for c in characters],
            label="Select Character",
            on_change=load_relationships
        )

        return ft.Column([
            ft.Text("Character Relationships", size=18, weight="bold"),
            ft.ElevatedButton("Update Relationships", on_click=load_relationships),
            dropdown,
            ft.Divider(),
            details_display
        ], scroll="auto", expand=True)

    def build_event_tab(page):
        log_display = ft.Column(scroll="auto", expand=True)

        def trigger_event_click(e):
            message1,message2,result = trigger_random_event()
            log_display.controls.insert(0, ft.Text(result, color="lightblue"))
            log_display.controls.insert(1, ft.Text(message1, color="lightgreen"))
            log_display.controls.insert(2, ft.Text(message2, color="lightgreen"))
            page.update()

        return ft.Column([
            ft.Text("Simulate Event", size=18, weight="bold"),
            ft.ElevatedButton("Trigger Random Event", on_click=trigger_event_click),
            ft.Divider(),
            log_display
        ], expand=True)
    # Tabs
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Create Character", content=create_tab),
            ft.Tab(text="View Characters", content=view_tab),
            ft.Tab(text="Battle Simulator", content=battle_tab),
            ft.Tab(text="Leaderboards", content=leaderboard_tab),
            ft.Tab(text="Moral Alignment", content=alignment_tab),
            ft.Tab(text="Bestiary", content=build_bestiary_tab(page)),
            ft.Tab(text="Weapons and Powers", content=build_weapon_power_tab()),
            ft.Tab(text="Archetypes", content=build_archetype_tab()),
            ft.Tab(text="Tournament Mode", content=build_tournament_tab()),
            ft.Tab(text="Relationships", content=build_relationships_tab(page)),
            ft.Tab(text="Events", content=build_event_tab(page))
        ],
        expand=1
    )

    page.add(tabs)
    load_characters_view()  # Load on startup

ft.app(target=main)
