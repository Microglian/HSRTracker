import mapping


class Team:
    def __init__(
        self,
        team_index: int,
        character1: dict,
        character2: dict,
        character3: dict,
        character4: dict,
    ) -> None:
        self.team_index = team_index
        self.character1 = character1
        self.character2 = character2
        self.character3 = character3
        self.character4 = character4
        self.tasks = []


class TeamTask:
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
    def __init__(
        self, character, uuid, pos, set, slot, mainstat, substats: list = []
    ) -> None:
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
    "Yukong",
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
    "Worrisome Blissful",
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
    "Hey Over Here",
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
    "Walk Time",
]

charactermaterials = {
    "Acheron": {
        "LevelMat": "Lightning Staff",
        "CommonMat": "Dream",
        "TraceMat": "Fire",
        "WBMat": "Past Evils",
    },
    "Argenti": {
        "LevelMat": "Netherworld Token",
        "CommonMat": "Core",
        "TraceMat": "Key",
        "WBMat": "Regret Ochema",
    },
    "Aventurine": {
        "LevelMat": "Suppressing Edict",
        "CommonMat": "Thought",
        "TraceMat": "Stardust",
        "WBMat": "Past Evils",
    },
    "Bailu": {
        "LevelMat": "Lightning Crown",
        "CommonMat": "Core",
        "TraceMat": "Seed",
        "WBMat": "Guardian Lament",
    },
    "Black Swan": {
        "LevelMat": "Ascendant Debris",
        "CommonMat": "Cpre",
        "TraceMat": "Fire",
        "WBMat": "Past Evils",
    },
    "Blade": {
        "LevelMat": "Ascendant Debris",
        "CommonMat": "Immortal",
        "TraceMat": "Blade",
        "WBMat": "Regret Ochema",
    },
    "Boothill": {
        "LevelMat": "IPC Work Permit",
        "CommonMat": "Thought",
        "TraceMat": "Bullet",
        "WBMat": "Lost Echo",
    },
    "Bronya": {
        "LevelMat": "Storm Eye",
        "CommonMat": "Silvermane",
        "TraceMat": "Tune",
        "WBMat": "Guardian Lament",
    },
    "Clara": {
        "LevelMat": "Teeth of Iron Wolf",
        "CommonMat": "Ancient",
        "TraceMat": "Blade",
        "WBMat": "Guardian Lament",
    },
    "Dan Heng IL": {
        "LevelMat": "Suppressing Edict",
        "CommonMat": "Immortal",
        "TraceMat": "Blade",
        "WBMat": "Regret Ochema",
    },
    "Dr Ratio": {
        "LevelMat": "Suppressing Edict",
        "CommonMat": "Thief",
        "TraceMat": "Arrow",
        "WBMat": "Past Evils",
    },
    "Firefly": {
        "LevelMat": "Raging Heart",
        "CommonMat": "Thought",
        "TraceMat": "Teeth",
        "WBMat": "Lost Echo",
    },
    "Fu Xuan": {
        "LevelMat": "Nail of the Ape",
        "CommonMat": "Artifex",
        "TraceMat": "Endurance",
        "WBMat": "Regret Ochema",
    },
    "Gepard": {
        "LevelMat": "Horn of Snow",
        "CommonMat": "Silvermane",
        "TraceMat": "Endurance",
        "WBMat": "Guardian Lament",
    },
    "Himeko": {
        "LevelMat": "Endotherm Chitin",
        "CommonMat": "Core",
        "TraceMat": "Key",
        "WBMat": "Destroyer Road",
    },
    "Huohuo": {
        "LevelMat": "Ascendant Debris",
        "CommonMat": "Immortal",
        "TraceMat": "Seed",
        "WBMat": "Regret Ochema",
    },
    "Jade": {
        "LevelMat": "Dream Flamer",
        "CommonMat": "Dream",
        "TraceMat": "Sketch",
        "WBMat": "Lost Echo",
    },
    "Jing Yuan": {
        "LevelMat": "Lightning Staff",
        "CommonMat": "Immortal",
        "TraceMat": "Key",
        "WBMat": "Destroyer Road",
    },
    "Jingliu": {
        "LevelMat": "Gelid Chitin",
        "CommonMat": "Immortal",
        "TraceMat": "Blade",
        "WBMat": "Regret Ochema",
    },
    "Kafka": {
        "LevelMat": "Lightning Staff",
        "CommonMat": "Thief",
        "TraceMat": "Obsidian",
        "WBMat": "Regret Ochema",
    },
    "Luocha": {
        "LevelMat": "Golden Crown",
        "CommonMat": "Artifex",
        "TraceMat": "Seed",
        "WBMat": "Guardian Lament",
    },
    "Robin": {
        "LevelMat": "IPC Work Permit",
        "CommonMat": "Dream",
        "TraceMat": "Note",
        "WBMat": "Past Evils",
    },
    "Ruan Mei": {
        "LevelMat": "Gelid Chitin",
        "CommonMat": "Immortal",
        "TraceMat": "Tune",
        "WBMat": "Past Evils",
    },
    "Seele": {
        "LevelMat": "Void Cast Iron",
        "CommonMat": "Thief",
        "TraceMat": "Arrow",
        "WBMat": "Guardian Lament",
    },
    "Silver Wolf": {
        "LevelMat": "Void Cast Iron",
        "CommonMat": "Ancient",
        "TraceMat": "Obsidian",
        "WBMat": "Destroyer Road",
    },
    "Sparkle": {
        "LevelMat": "Dream Flamer",
        "CommonMat": "Thought",
        "TraceMat": "Note",
        "WBMat": "Past Evils",
    },
    "Topaz": {
        "LevelMat": "Searing Steel",
        "CommonMat": "Silvermane",
        "TraceMat": "Arrow",
        "WBMat": "Regret Ochema",
    },
    "Welt": {
        "LevelMat": "Golden Crown",
        "CommonMat": "Silvermane",
        "TraceMat": "Obsidian",
        "WBMat": "Destroyer Road",
    },
    "Yanqing": {
        "LevelMat": "Gelid Chitin",
        "CommonMat": "Thief",
        "TraceMat": "Arrow",
        "WBMat": "Guardian Lament",
    },
    "Arlan": {
        "LevelMat": "Lightning Crown",
        "CommonMat": "Core",
        "TraceMat": "Blade",
        "WBMat": "Destroyer Road",
    },
    "Asta": {
        "LevelMat": "Endotherm Chitin",
        "CommonMat": "Silvermane",
        "TraceMat": "Tune",
        "WBMat": "Destroyer Road",
    },
    "Dan Heng": {
        "LevelMat": "Storm Eye",
        "CommonMat": "Core",
        "TraceMat": "Arrow",
        "WBMat": "Destroyer Road",
    },
    "Gallagher": {
        "LevelMat": "Raging Heart",
        "CommonMat": "Dream",
        "TraceMat": "Alien",
        "WBMat": "Past Evils",
    },
    "Guinaifen": {
        "LevelMat": "Searing Steel",
        "CommonMat": "Artifex",
        "TraceMat": "Obsidian",
        "WBMat": "Regret Ochema",
    },
    "Hanya": {
        "LevelMat": "Netherworld Token",
        "CommonMat": "Artifex",
        "TraceMat": "Tune",
        "WBMat": "Regret Ochema",
    },
    "Herta": {
        "LevelMat": "Horn of Snow",
        "CommonMat": "Core",
        "TraceMat": "Key",
        "WBMat": "Destroyer Road",
    },
    "Hook": {
        "LevelMat": "Endotherm Chitin",
        "CommonMat": "Ancient",
        "TraceMat": "Blade",
        "WBMat": "Guardian Lament",
    },
    "Luka": {
        "LevelMat": "Teeth of Iron Wolf",
        "CommonMat": "Ancient",
        "TraceMat": "Obsidian",
        "WBMat": "Regret Ochema",
    },
    "Lynx": {
        "LevelMat": "Nail of the Ape",
        "CommonMat": "Core",
        "TraceMat": "Seed",
        "WBMat": "Regret Ochema",
    },
    "March 7th": {
        "LevelMat": "Horn of Snow",
        "CommonMat": "Thief",
        "TraceMat": "Endurance",
        "WBMat": "Destroyer Road",
    },
    "Misha": {
        "LevelMat": "Dream Fridge",
        "CommonMat": "Dream",
        "TraceMat": "Teeth",
        "WBMat": "Past Evils",
    },
    "Natasha": {
        "LevelMat": "Teeth of Iron Wolf",
        "CommonMat": "Ancient",
        "TraceMat": "Seed",
        "WBMat": "Guardian Lament",
    },
    "Pela": {
        "LevelMat": "Horn of Snow",
        "CommonMat": "Core",
        "TraceMat": "Obsidian",
        "WBMat": "Guardian Lament",
    },
    "Qingque": {
        "LevelMat": "Void Cast Iron",
        "CommonMat": "Thief",
        "TraceMat": "Key",
        "WBMat": "Guardian Lament",
    },
    "Sampo": {
        "LevelMat": "Storm Eye",
        "CommonMat": "Ancient",
        "TraceMat": "Obsidian",
        "WBMat": "Guardian Lament",
    },
    "Serval": {
        "LevelMat": "Lightning Crown",
        "CommonMat": "Silvermane",
        "TraceMat": "Key",
        "WBMat": "Guardian Lament",
    },
    "Sushang": {
        "LevelMat": "Teeth of Iron Wolf",
        "CommonMat": "Artifex",
        "TraceMat": "Arrow",
        "WBMat": "Guardian Lament",
    },
    "Tingyun": {
        "LevelMat": "Lightning Crown",
        "CommonMat": "Immortal",
        "TraceMat": "Tune",
        "WBMat": "Destroyer Road",
    },
    "Xueyi": {
        "LevelMat": "Nail of the Ape",
        "CommonMat": "Core",
        "TraceMat": "Blade",
        "WBMat": "Past Evils",
    },
    "Yukong": {
        "LevelMat": "Golden Crown",
        "CommonMat": "Artifex",
        "TraceMat": "Tune",
        "WBMat": "Destroyer Road",
    },
}

weaponmaterials = {
    "Night on the Milky Way": {"CommonMat": "Core", "TraceMat": "Key"},
    "In the Night": {"CommonMat": "Thief", "TraceMat": "Arrow"},
    "Something Irreplacable": {"CommonMat": "Ancient", "TraceMat": "Blade"},
    "But the Battle Isn't Over": {"CommonMat": "Silvermane", "TraceMat": "Tune"},
    "In the Name of the World": {"CommonMat": "Silvermane", "TraceMat": "Obsidian"},
    "Moment of Victory": {"CommonMat": "Silvermane", "TraceMat": "Endurance"},
    "Patience is All You Need": {"CommonMat": "Core", "TraceMat": "Obsidian"},
    "Incessant Rain": {"CommonMat": "Ancient", "TraceMat": "Obsidian"},
    "Echoes of the Coffin": {"CommonMat": "Artifex", "TraceMat": "Seed"},
    "The Unreachable Side": {"CommonMat": "Immortal", "TraceMat": "Blade"},
    "Before Dawn": {"CommonMat": "Immortal", "TraceMat": "Key"},
    "She Already Shut Her Eyes": {"CommonMat": "Artifex", "TraceMat": "Endurance"},
    "Sleep Like the Dead": {"CommonMat": "Thief", "TraceMat": "Arrow"},
    "Time Waits for No One": {"CommonMat": "Core", "TraceMat": "Seed"},
    "I Shall Be My Own Sword": {"CommonMat": "Immortal", "TraceMat": "Blade"},
    "Brighter Than the Sun": {"CommonMat": "Immortal", "TraceMat": "Blade"},
    "Worrisome, Blissful": {"CommonMat": "Silvermane", "TraceMat": "Arrow"},
    "On the Fall of an Aeon": {"CommonMat": "Core", "TraceMat": "Blade"},
    "Cruising in the Stellar Sea": {"CommonMat": "Core", "TraceMat": "Arrow"},
    "Texture of Memories": {"CommonMat": "Core", "TraceMat": "Endurance"},
    "Night of Fright": {"CommonMat": "Immortal", "TraceMat": "Seed"},
    "An Instant Before A Gaze": {"CommonMat": "Core", "TraceMat": "Key"},
    "Past Self In Mirror": {"CommonMat": "Immortal", "TraceMat": "Tune"},
    "Earthly Escapade": {"CommonMat": "Thought", "TraceMat": "Note"},
    "Inherent Unjust Destiny": {"CommonMat": "Thought", "TraceMat": "Stardust"},
    "Baptism of Pure Thought": {"CommonMat": "Thief", "TraceMat": "Arrow"},
    "Solitary Healing": {"CommonMat": "Core", "TraceMat": "Obsidian"},
    "Reforged Remembrance": {"CommonMat": "Core", "TraceMat": "Fire"},
    "Eternal Calculus": {"CommonMat": "Core", "TraceMat": "Sketch"},
    "Along the Passing Shore": {"CommonMat": "Dream", "TraceMat": "Fire"},
    "Where Should Dreams Rest": {"CommonMat": "Thought", "TraceMat": "Teeth"},
    "Yet Hope Is Priceless": {"CommonMat": "Dream", "TraceMat": "Sketch"},
    "Sailing Towards a Second Life": {"CommonMat": "Thought", "TraceMat": "Bullet"},
    "Flowing Nightglow": {"CommonMat": "Dream", "TraceMat": "Note"},
    "A Secret Vow": {"CommonMat": "Silvermane", "TraceMat": "Blade"},
    "After the Charmony Fall": {"CommonMat": "Thought", "TraceMat": "Sketch"},
    "Before the Tutorial Starts": {"CommonMat": "Core", "TraceMat": "Obsidian"},
    "Boundless Choreo": {"CommonMat": "Thought", "TraceMat": "Fire"},
    "Carve the Moon": {"CommonMat": "Thief", "TraceMat": "Tune"},
    "Concert for Two": {"CommonMat": "Thought", "TraceMat": "Stardust"},
    "Dance! Dance! Dance!": {"CommonMat": "Artifex", "TraceMat": "Tune"},
    "Day One of My New Life": {"CommonMat": "Core", "TraceMat": "Endurance"},
    "Destiny's Threads Woven": {"CommonMat": "Thought", "TraceMat": "Endurance"},
    "Dreamville Adventure": {"CommonMat": "Dream", "TraceMat": "Note"},
    "Eyes of the Prey": {"CommonMat": "Ancient", "TraceMat": "Obsidian"},
    "Fermata": {"CommonMat": "Silvermane", "TraceMat": "Obsidian"},
    "Final Victor": {"CommonMat": "Thought", "TraceMat": "Arrow"},
    "Flames Afar": {"CommonMat": "Dream", "TraceMat": "Teeth"},
    "For Tomorrow's Journey": {"CommonMat": "Dream", "TraceMat": "Note"},
    "Geniuses' Repose": {"CommonMat": "Immortal", "TraceMat": "Key"},
    "Good Night and Sleep Well": {"CommonMat": "Silvermane", "TraceMat": "Obsidian"},
    "Hey, Over Here": {"CommonMat": "Immortal", "TraceMat": "Seed"},
    "Indelible Promise": {"CommonMat": "Dream", "TraceMat": "Teeth"},
    "It's Showtime": {"CommonMat": "Core", "TraceMat": "Fire"},
    "Landau's Choice": {"CommonMat": "Core", "TraceMat": "Endurance"},
    "Make the World Clamor": {"CommonMat": "Ancient", "TraceMat": "Key"},
    "Memories of the Past": {"CommonMat": "Silvermane", "TraceMat": "Tune"},
    "Nowhere to Run": {"CommonMat": "Silvermane", "TraceMat": "Blade"},
    "Only Silence Remains": {"CommonMat": "Silvermane", "TraceMat": "Arrow"},
    "Past and Future": {"CommonMat": "Core", "TraceMat": "Tune"},
    "Perfect Timing": {"CommonMat": "Artifex", "TraceMat": "Seed"},
    "Planetary Rendezvous": {"CommonMat": "Thief", "TraceMat": "Tune"},
    "Post-Op Conversation": {"CommonMat": "Core", "TraceMat": "Seed"},
    "Quid Pro Quo": {"CommonMat": "Silvermane", "TraceMat": "Seed"},
    "Resolution Shines": {"CommonMat": "Artifex", "TraceMat": "Obsidian"},
    "Return to Darkness": {"CommonMat": "Immortal", "TraceMat": "Arrow"},
    "River Flows in Spring": {"CommonMat": "Ancient", "TraceMat": "Arrow"},
    "Shared Feeling": {"CommonMat": "Artifex", "TraceMat": "Seed"},
    "Subscribe for More!": {"CommonMat": "Artifex", "TraceMat": "Arrow"},
    "Swordplay": {"CommonMat": "Core", "TraceMat": "Arrow"},
    "The Birth of the Self": {"CommonMat": "Ancient", "TraceMat": "Key"},
    "The Day the Cosmos Fell": {"CommonMat": "Dream", "TraceMat": "Key"},
    "The Moles Welcome You": {"CommonMat": "Thief", "TraceMat": "Blade"},
    "Seriousness of Breakfast": {"CommonMat": "Core", "TraceMat": "Key"},
    "This is Me!": {"CommonMat": "Thief", "TraceMat": "Endurance"},
    "Today Another Peaceful Day": {"CommonMat": "Immortal", "TraceMat": "Key"},
    "Trend of Universal Market": {"CommonMat": "Immortal", "TraceMat": "Endurance"},
    "Under the Blue Sky": {"CommonMat": "Immortal", "TraceMat": "Blade"},
    "Warmth Shortens Cold Nights": {"CommonMat": "Core", "TraceMat": "Seed"},
    "We are Wildfire": {"CommonMat": "Ancient", "TraceMat": "Endurance"},
    "We Will Meet Again": {"CommonMat": "Ancient", "TraceMat": "Obsidian"},
    "What is Real?": {"CommonMat": "Dream", "TraceMat": "Seed"},
    "Walk Time": {"CommonMat": "Core", "TraceMat": "Blade"},
}

# 5-star: A2 is always 3 Tracemat green, A4 is always 5 Tracemat blue, A6 is always 8 Tracemat purple
# 4-star: A2 is always 2 Tracemat green, A4 is always 4 Tracemat blue, A6 is always 6 Tracemat purple

# wbmat, tracemat[green,blue,purple], commonmat[green,blue,purple]
basicmaterials5 = {
    2: [[3, 0, 0], [6, 0, 0]],
    3: [[0, 3, 0], [0, 3, 0]],
    4: [[0, 5, 0], [0, 4, 0]],
    5: [[0, 0, 3], [0, 0, 3]],
    6: [[0, 0, 8], [0, 0, 4]],
}

basicmaterials4 = {
    2: [[2, 0, 0], [4, 0, 0]],
    3: [[0, 3, 0], [0, 3, 0]],
    4: [[0, 4, 0], [0, 3, 0]],
    5: [[0, 0, 2], [0, 0, 2]],
    6: [[0, 0, 6], [0, 0, 3]],
}

# Tracks of Destiny, wbmat, tracemat[green,blue,purple], commonmat[green,blue,purple]
tracematerials5 = {
    2: [0, 0, [0, 0, 0], [3, 0, 0]],
    3: [0, 0, [3, 0, 0], [6, 0, 0]],
    4: [0, 0, [0, 3, 0], [0, 3, 0]],
    5: [0, 0, [0, 5, 0], [0, 4, 0]],
    6: [0, 0, [0, 7, 0], [0, 6, 0]],
    7: [0, 0, [0, 0, 3], [0, 0, 3]],
    8: [0, 1, [0, 0, 5], [0, 0, 4]],
    9: [1, 1, [0, 0, 8], [0, 0, 0]],
    10: [1, 1, [0, 0, 14], [0, 0, 0]],
}

tracematerials4 = {
    2: [0, 0, [0, 0, 0], [2, 0, 0]],
    3: [0, 0, [2, 0, 0], [4, 0, 0]],
    4: [0, 0, [0, 2, 0], [0, 2, 0]],
    5: [0, 0, [0, 4, 0], [0, 3, 0]],
    6: [0, 0, [0, 6, 0], [0, 5, 0]],
    7: [0, 0, [0, 0, 2], [0, 0, 2]],
    8: [0, 1, [0, 0, 4], [0, 0, 3]],
    9: [0, 1, [0, 0, 6], [0, 0, 0]],
    10: [1, 1, [0, 0, 11], [0, 0, 0]],
}

# bossmat, commonmat[green,blue,purple]
levelmaterials5 = {
    30: [0, [5, 0, 0]],
    40: [0, [10, 0, 0]],
    50: [3, [0, 6, 0]],
    60: [7, [0, 9, 0]],
    70: [20, [0, 0, 6]],
    80: [35, [0, 0, 9]],
}

levelmaterials4 = {
    30: [0, [4, 0, 0]],
    40: [0, [8, 0, 0]],
    50: [2, [0, 5, 0]],
    60: [5, [0, 8, 0]],
    70: [15, [0, 0, 5]],
    80: [28, [0, 0, 7]],
}

# commonmat, tracemat
weaponmaterials5 = {
    30: [[8, 0, 0], [0, 0, 0]],
    40: [[12, 0, 0], [4, 0, 0]],
    50: [[0, 8, 0], [0, 4, 0]],
    60: [[0, 12, 0], [0, 8, 0]],
    70: [[0, 0, 6], [0, 0, 5]],
    80: [[0, 0, 8], [0, 0, 10]],
}

weaponmaterials4 = {
    30: [[5, 0, 0], [0, 0, 0]],
    40: [[10, 0, 0], [3, 0, 0]],
    50: [[0, 6, 0], [0, 3, 0]],
    60: [[0, 9, 0], [0, 6, 0]],
    70: [[0, 0, 5], [0, 0, 4]],
    80: [[0, 0, 7], [0, 0, 8]],
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
    "Kalpagni Lantern",
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
    "Kalpagni Lantern": ["Orb", "Rope"],
}

relicmainstats = {
    "Head": ["HP"],
    "Hand": ["Atk"],
    "Torso": ["HP%", "Atk%", "Def%", "CR%", "CD%", "Heal%", "EHR%"],
    "Feet": ["HP%", "Atk%", "Def%", "Spd"],
    "Orb": [
        "HP%",
        "Atk%",
        "Def%",
        "Phys%",
        "Fire%",
        "Ice%",
        "Elec%",
        "Wind%",
        "Qua%",
        "Ima%",
    ],
    "Rope": ["BE%", "ERR%", "HP%", "Atk%", "Def%"],
}

relicsubstats = ["HP%", "Atk%", "Def%", "Spd", "CR%", "CD%", "EHR%", "Res%", "BE%"]
