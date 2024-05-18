import mapping

class Team():
    def __init__(self, team_index:int, character1:dict, character2:dict, character3:dict, character4:dict) -> None:
        self.team_index = team_index
        self.character1 = character1
        self.character2 = character2
        self.character3 = character3
        self.character4 = character4
        self.tasks = []
    
class TeamTask():
    def __init__(self, character, uuid, pos, tasktype) -> None:
        self.character = character
        self.uuid = uuid
        self.pos = pos
        self.tasktype = tasktype


class TeamTaskWeaponLevel(TeamTask):
    def __init__(self, character, uuid, pos, level) -> None:
        TeamTask.__init__(self, character, uuid, pos, "WeaponLevel")
        self.level = level


class TeamTaskLevel(TeamTask):
    def __init__(self, character, uuid, pos, level) -> None:
        TeamTask.__init__(self, character, uuid, pos, "Level")
        self.level = level


class TeamTaskAscensionTrace(TeamTask):
    def __init__(self, character, uuid, pos, trace) -> None:
        TeamTask.__init__(self, character, uuid, pos, "AscensionTrace")
        self.trace = trace
        

class TeamTaskLevelledTrace(TeamTask):
    def __init__(self, character, uuid, pos, trace, target) -> None:
        TeamTask.__init__(self, character, uuid, pos, "LevelledTrace")
        self.trace = trace
        self.target = target


class TeamTaskRelic(TeamTask):
    def __init__(self, character, uuid, pos, set, slot, mainstat, substats:list=[]) -> None:
        TeamTask.__init__(self, character, uuid, pos, "Relic")
        self.set = set
        self.slot = slot
        self.mainstat = mainstat
        self.substats = substats
        while len(self.substats) < 4:
            self.substats.append("")

characternames = [
    "Acheron",
    "Argenti",
    "Aventurine",
    "Bailu",
    "Black Swan",
    "Blade",
    "Boothill",
    "Bronya",
    "Clara",
    "Dan Heng IL",
    "Dr Ratio",
    "Firefly",
    "Fu Xuan",
    "Gepard",
    "Himeko",
    "Huohuo",
    "Jade",
    "Jing Yuan",
    "Jingliu",
    "Kafka",
    "Luocha",
    "Robin",
    "Ruan Mei",
    "Seele",
    "Silver Wolf",
    "Sparkle",
    "Topaz",
    "Welt",
    "Yanqing",
    "Arlan",
    "Asta",
    "Dan Heng",
    "Gallagher",
    "Guinaifen",
    "Hanya",
    "Herta",
    "Hook",
    "Luka",
    "Lynx",
    "March 7th",
    "Misha",
    "Natasha",
    "Pela",
    "Qingque",
    "Sampo",
    "Serval",
    "Sushang",
    "Tingyun",
    "Xueyi",
    "Yukong"
]

weaponnames = [
    "Night on the Milky Way",
    "In the Night",
    "Something Irreplaceable",
    "But the Battle Isn't Over",
    "In the Name of the World",
    "Moment of Victory",
    "Patience is All You Need",
    "Incessant Rain",
    "Echoes of the Coffin",
    "The Unreachable Side",
    "Before Dawn",
    "She Already Shut Her Eyes",
    "Sleep Like the Dead",
    "Time Waits for No One",
    "I Shall Be My Own Sword",
    "Brighter Than the Sun",
    "Worrisome, Blissful",
    "On the Fall of an Aeon",
    "Cruising in the Stellar Sea",
    "Texture of Memories",
    "Night of Fright",
    "An Instant Before A Gaze",
    "Past Self In Mirror",
    "Earthly Escapade",
    "Inherent Unjust Destiny",
    "Baptism of Pure Thought",
    "Solitary Healing",
    "Reforged Remembrance",
    "Eternal Calculus",
    "Along the Passing Shore",
    "Where Should Dreams Rest",
    "Yet Hope Is Priceless",
    "Sailing Towards a Second Life",
    "Flowing Nightglow",
    "A Secret Vow",
    "After the Charmony Fall",
    "Before the Tutorial Starts",
    "Boundless Choreo",
    "Carve the Moon",
    "Concert for Two",
    "Dance! Dance! Dance!",
    "Day One of My New Life",
    "Destiny's Threads Woven",
    "Dreamville Adventure",
    "Eyes of the Prey",
    "Fermata",
    "Final Victor",
    "Flames Afar",
    "For Tomorrow's Journey",
    "Geniuses' Repose",
    "Good Night and Sleep Well",
    "Hey, Over Here",
    "Indelible Promise",
    "It's Showtime",
    "Landau's Choice",
    "Make the World Clamor",
    "Memories of the Past",
    "Nowhere to Run",
    "Only Silence Remains",
    "Past and Future",
    "Perfect Timing",
    "Planetary Rendezvous",
    "Post-Op Conversation",
    "Quid Pro Quo",
    "Resolution Shines",
    "Return to Darkness",
    "River Flows in Spring",
    "Shared Feeling",
    "Subscribe for More!",
    "Swordplay",
    "The Birth of the Self",
    "The Day the Cosmos Fell",
    "The Moles Welcome You",
    "Seriousness of Breakfast",
    "This is Me!",
    "Today Another Peaceful Day",
    "Trend of Universal Market",
    "Under the Blue Sky",
    "Warmth Shortens Cold Nights",
    "We are Wildfire",
    "We Will Meet Again",
    "What is Real?",
    "Walk Time"
]

charactermaterials = {
    "Acheron": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Argenti": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Aventurine": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Bailu": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Black Swan": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Blade": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Boothill": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Bronya": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Clara": {"LevelMat": "Teeth of Iron Wolf", "CommonMat": "Ancient", "TraceMat": "Blade", "WBMat": "Guardian Lament"},
    "Dan Heng IL": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Dr Ratio": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Firefly": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Fu Xuan": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Gepard": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Himeko": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Huohuo": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Jade": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Jing Yuan": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Jingliu": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Kafka": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Luocha": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Robin": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Ruan Mei": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Seele": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Silver Wolf": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Sparkle": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Topaz": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Welt": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Yanqing": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Arlan": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Asta": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Dan Heng": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Gallagher": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Guinaifen": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Hanya": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Herta": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Hook": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Luka": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Lynx": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "March 7th": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Misha": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Natasha": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Pela": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Qingque": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Sampo": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Serval": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Sushang": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Tingyun": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Xueyi": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""},
    "Yukong": {"LevelMat": "", "CommonMat": "", "TraceMat": "", "WBMat": ""}
}

weaponmaterials = {
    "Night on the Milky Way": {"CommonMat": "", "TraceMat": ""},
    "In the Night": {"CommonMat": "", "TraceMat": ""},
    "Something Irreplacable": {"CommonMat": "Ancient", "TraceMat": "Blade"},
    "But the Battle Isn't Over": {"CommonMat": "", "TraceMat": ""},
    "In the Name of the World": {"CommonMat": "", "TraceMat": ""},
    "Moment of Victory": {"CommonMat": "", "TraceMat": ""},
    "Patience is All You Need": {"CommonMat": "", "TraceMat": ""},
    "Incessant Rain": {"CommonMat": "", "TraceMat": ""},
    "Echoes of the Coffin": {"CommonMat": "", "TraceMat": ""},
    "The Unreachable Side": {"CommonMat": "", "TraceMat": ""},
    "Before Dawn": {"CommonMat": "", "TraceMat": ""},
    "She Already Shut Her Eyes": {"CommonMat": "", "TraceMat": ""},
    "Sleep Like the Dead": {"CommonMat": "", "TraceMat": ""},
    "Time Waits for No One": {"CommonMat": "", "TraceMat": ""},
    "I Shall Be My Own Sword": {"CommonMat": "", "TraceMat": ""},
    "Brighter Than the Sun": {"CommonMat": "", "TraceMat": ""},
    "Worrisome, Blissful": {"CommonMat": "", "TraceMat": ""},
    "On the Fall of an Aeon": {"CommonMat": "", "TraceMat": ""},
    "Cruising in the Stellar Sea": {"CommonMat": "", "TraceMat": ""},
    "Texture of Memories": {"CommonMat": "", "TraceMat": ""},
    "Night of Fright": {"CommonMat": "", "TraceMat": ""},
    "An Instant Before A Gaze": {"CommonMat": "", "TraceMat": ""},
    "Past Self In Mirror": {"CommonMat": "", "TraceMat": ""},
    "Earthly Escapade": {"CommonMat": "", "TraceMat": ""},
    "Inherent Unjust Destiny": {"CommonMat": "", "TraceMat": ""},
    "Baptism of Pure Thought": {"CommonMat": "", "TraceMat": ""},
    "Solitary Healing": {"CommonMat": "", "TraceMat": ""},
    "Reforged Remembrance": {"CommonMat": "", "TraceMat": ""},
    "Eternal Calculus": {"CommonMat": "", "TraceMat": ""},
    "Along the Passing Shore": {"CommonMat": "", "TraceMat": ""},
    "Where Should Dreams Rest": {"CommonMat": "", "TraceMat": ""},
    "Yet Hope Is Priceless": {"CommonMat": "", "TraceMat": ""},
    "Sailing Towards a Second Life": {"CommonMat": "", "TraceMat": ""},
    "Flowing Nightglow": {"CommonMat": "", "TraceMat": ""},
    "A Secret Vow": {"CommonMat": "", "TraceMat": ""},
    "After the Charmony Fall": {"CommonMat": "", "TraceMat": ""},
    "Before the Tutorial Starts": {"CommonMat": "", "TraceMat": ""},
    "Boundless Choreo": {"CommonMat": "", "TraceMat": ""},
    "Carve the Moon": {"CommonMat": "", "TraceMat": ""},
    "Concert for Two": {"CommonMat": "", "TraceMat": ""},
    "Dance! Dance! Dance!": {"CommonMat": "", "TraceMat": ""},
    "Day One of My New Life": {"CommonMat": "", "TraceMat": ""},
    "Destiny's Threads Woven": {"CommonMat": "", "TraceMat": ""},
    "Dreamville Adventure": {"CommonMat": "", "TraceMat": ""},
    "Eyes of the Prey": {"CommonMat": "", "TraceMat": ""},
    "Fermata": {"CommonMat": "", "TraceMat": ""},
    "Final Victor": {"CommonMat": "", "TraceMat": ""},
    "Flames Afar": {"CommonMat": "", "TraceMat": ""},
    "For Tomorrow's Journey": {"CommonMat": "", "TraceMat": ""},
    "Geniuses' Repose": {"CommonMat": "", "TraceMat": ""},
    "Good Night and Sleep Well": {"CommonMat": "", "TraceMat": ""},
    "Hey, Over Here": {"CommonMat": "", "TraceMat": ""},
    "Indelible Promise": {"CommonMat": "", "TraceMat": ""},
    "It's Showtime": {"CommonMat": "", "TraceMat": ""},
    "Landau's Choice": {"CommonMat": "", "TraceMat": ""},
    "Make the World Clamor": {"CommonMat": "", "TraceMat": ""},
    "Memories of the Past": {"CommonMat": "", "TraceMat": ""},
    "Nowhere to Run": {"CommonMat": "", "TraceMat": ""},
    "Only Silence Remains": {"CommonMat": "", "TraceMat": ""},
    "Past and Future": {"CommonMat": "", "TraceMat": ""},
    "Perfect Timing": {"CommonMat": "", "TraceMat": ""},
    "Planetary Rendezvous": {"CommonMat": "", "TraceMat": ""},
    "Post-Op Conversation": {"CommonMat": "", "TraceMat": ""},
    "Quid Pro Quo": {"CommonMat": "", "TraceMat": ""},
    "Resolution Shines": {"CommonMat": "", "TraceMat": ""},
    "Return to Darkness": {"CommonMat": "", "TraceMat": ""},
    "River Flows in Spring": {"CommonMat": "", "TraceMat": ""},
    "Shared Feeling": {"CommonMat": "", "TraceMat": ""},
    "Subscribe for More!": {"CommonMat": "", "TraceMat": ""},
    "Swordplay": {"CommonMat": "", "TraceMat": ""},
    "The Birth of the Self": {"CommonMat": "", "TraceMat": ""},
    "The Day the Cosmos Fell": {"CommonMat": "", "TraceMat": ""},
    "The Moles Welcome You": {"CommonMat": "", "TraceMat": ""},
    "Seriousness of Breakfast": {"CommonMat": "", "TraceMat": ""},
    "This is Me!": {"CommonMat": "", "TraceMat": ""},
    "Today Another Peaceful Day": {"CommonMat": "", "TraceMat": ""},
    "Trend of Universal Market": {"CommonMat": "", "TraceMat": ""},
    "Under the Blue Sky": {"CommonMat": "", "TraceMat": ""},
    "Warmth Shortens Cold Nights": {"CommonMat": "", "TraceMat": ""},
    "We are Wildfire": {"CommonMat": "", "TraceMat": ""},
    "We Will Meet Again": {"CommonMat": "", "TraceMat": ""},
    "What is Real?": {"CommonMat": "", "TraceMat": ""},
    "Walk Time": {"CommonMat": "", "TraceMat": ""},
}

# 5-star: A2 is always 3 Tracemat green, A4 is always 5 Tracemat blue, A6 is always 8 Tracemat purple
# 4-star: A2 is always 2 Tracemat green, A4 is always 4 Tracemat blue, A6 is always 6 Tracemat purple

# wbmat, tracemat[green,blue,purple], commonmat[green,blue,purple]
basicmaterials5 = {
    2: [[3,0,0],[6,0,0]],
    3: [[0,3,0],[0,3,0]],
    4: [[0,5,0],[0,4,0]],
    5: [[0,0,3],[0,0,3]],
    6: [[0,0,8],[0,0,4]]
}

basicmaterials4 = {
    2: [[2,0,0],[4,0,0]],
    3: [[0,3,0],[0,3,0]],
    4: [[0,4,0],[0,3,0]],
    5: [[0,0,2],[0,0,2]],
    6: [[0,0,6],[0,0,3]]
}

# Tracks of Destiny, wbmat, tracemat[green,blue,purple], commonmat[green,blue,purple]
tracematerials5 = {
    2: [0,0,[0,0,0],[3,0,0]],
    3: [0,0,[3,0,0],[6,0,0]],
    4: [0,0,[0,3,0],[0,3,0]],
    5: [0,0,[0,5,0],[0,4,0]],
    6: [0,0,[0,7,0],[0,6,0]],
    7: [0,0,[0,0,3],[0,0,3]],
    8: [0,1,[0,0,5],[0,0,4]],
    9: [1,1,[0,0,8],[0,0,0]],
    10:[1,1,[0,0,14],[0,0,0]]
}

tracematerials4 = {
    2: [0,0,[0,0,0],[2,0,0]],
    3: [0,0,[2,0,0],[4,0,0]],
    4: [0,0,[0,2,0],[0,2,0]],
    5: [0,0,[0,4,0],[0,3,0]],
    6: [0,0,[0,6,0],[0,5,0]],
    7: [0,0,[0,0,2],[0,0,2]],
    8: [0,1,[0,0,4],[0,0,3]],
    9: [0,1,[0,0,6],[0,0,0]],
    10:[1,1,[0,0,11],[0,0,0]]
}

# bossmat, commonmat[green,blue,purple]
levelmaterials5 = {
    30: [0,[5,0,0]],
    40: [0,[10,0,0]],
    50: [3,[0,6,0]],
    60: [7,[0,9,0]],
    70: [20,[0,0,6]],
    80: [35,[0,0,9]]
}

levelmaterials4 = {
    30: [0,[4,0,0]],
    40: [0,[8,0,0]],
    50: [2,[0,5,0]],
    60: [5,[0,8,0]],
    70: [15,[0,0,5]],
    80: [28,[0,0,7]]
}

# commonmat, tracemat
weaponmaterials5 = {
    30: [[8,0,0],[0,0,0]],
    40: [[12,0,0],[4,0,0]],
    50: [[0,8,0],[0,4,0]],
    60: [[0,12,0],[0,8,0]],
    70: [[0,0,6],[0,0,5]],
    80: [[0,0,8],[0,0,10]]
}

weaponmaterials4 = {
    30: [[5,0,0],[0,0,0]],
    40: [[10,0,0],[3,0,0]],
    50: [[0,6,0],[0,3,0]],
    60: [[0,9,0],[0,6,0]],
    70: [[0,0,5],[0,0,4]],
    80: [[0,0,7],[0,0,8]]
}

relicsets = [
    "Wandering Cloud",
    "Wild Wheat",
    "Purity Palace",
    "Glacial Forest",
    "Streetwise Boxing",
    "Wuthering Snow",
    "Lava-Forging",
    "Brilliant Stars",
    "Sizzling Thunder",
    "Twilight Line",
    "Shooting Meteor",
    "Banditry Desert",
    "Longevous Disciple",
    "Hackerspace",
    "Grand Duke",
    "Deep Confinement",
    "Dead Waters",
    "Dream Machinations",
    "Iron Cavalry",
    "Valourous",
    "Space Sealing",
    "Fleet of Ageless",
    "Cosmic Enterprise",
    "Belobog of Architects",
    "Differentiator",
    "Inert Salsotto",
    "Kingdom of Banditry",
    "Sprightly Vonwacq",
    "Rutilant Arena",
    "Broken Keel",
    "Firmament Frontline",
    "Penacony",
    "Sigonia",
    "Izumo Gensei",
    "Duran Dynasty",
    "Kalpagni Lantern"
]

relicpieces = {
    "Wandering Cloud": ["Head", "Hand", "Torso", "Feet"],
    "Wild Wheat": ["Head", "Hand", "Torso", "Feet"],
    "Purity Palace": ["Head", "Hand", "Torso", "Feet"],
    "Glacial Forest": ["Head", "Hand", "Torso", "Feet"],
    "Streetwise Boxing": ["Head", "Hand", "Torso", "Feet"],
    "Wuthering Snow": ["Head", "Hand", "Torso", "Feet"],
    "Lava-Forging": ["Head", "Hand", "Torso", "Feet"],
    "Brilliant Stars": ["Head", "Hand", "Torso", "Feet"],
    "Sizzling Thunder": ["Head", "Hand", "Torso", "Feet"],
    "Twilight Line": ["Head", "Hand", "Torso", "Feet"],
    "Shooting Meteor": ["Head", "Hand", "Torso", "Feet"],
    "Banditry Desert": ["Head", "Hand", "Torso", "Feet"],
    "Longevous Disciple": ["Head", "Hand", "Torso", "Feet"],
    "Hackerspace": ["Head", "Hand", "Torso", "Feet"],
    "Grand Duke": ["Head", "Hand", "Torso", "Feet"],
    "Deep Confinement": ["Head", "Hand", "Torso", "Feet"],
    "Dead Waters": ["Head", "Hand", "Torso", "Feet"],
    "Dream Machinations": ["Head", "Hand", "Torso", "Feet"],
    "Iron Cavalry": ["Head", "Hand", "Torso", "Feet"],
    "Valourous": ["Head", "Hand", "Torso", "Feet"],
    "Space Sealing": ["Orb", "Rope"],
    "Fleet of Ageless": ["Orb", "Rope"],
    "Cosmic Enterprise": ["Orb", "Rope"],
    "Belobog of Architects": ["Orb", "Rope"],
    "Differentiator": ["Orb", "Rope"],
    "Inert Salsotto": ["Orb", "Rope"],
    "Kingdom of Banditry": ["Orb", "Rope"],
    "Sprightly Vonwacq": ["Orb", "Rope"],
    "Rutilant Arena": ["Orb", "Rope"],
    "Broken Keel": ["Orb", "Rope"],
    "Firmament Frontline": ["Orb", "Rope"],
    "Penacony": ["Orb", "Rope"],
    "Sigonia": ["Orb", "Rope"],
    "Izumo Gensei": ["Orb", "Rope"],
    "Duran Dynasty": ["Orb", "Rope"],
    "Kalpagni Lantern": ["Orb", "Rope"] 
}

relicmainstats = {
    "Head": ["HP"],
    "Hand": ["Atk"],
    "Torso": ["HP%", "Atk%", "Def%", "CR%", "CD%", "Heal%", "EHR%"],
    "Feet": ["HP%", "Atk%", "Def%", "Spd"],
    "Orb": ["HP%", "Atk%", "Def%", "Phys%", "Fire%", "Ice%", "Elec%", "Wind%", "Qua%", "Ima%"],
    "Rope": ["BE%", "ERR%", "HP%", "Atk%", "Def%"]
}

relicsubstats = ["HP%", "Atk%", "Def%", "Spd", "CR%", "CD%", "EHR%", "Res%", "BE%"]