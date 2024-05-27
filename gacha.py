"""
Gacha tab has a header and three columns based on priority:
High     Medium      Low

Each task within a column is something to pull.
A task is either a Character task or a Lightcone task.
"""


class Gacha:
    def __init__(self) -> None:
        self.tasks = []


class GachaTask:
    def __init__(self, uuid, priority, pos, objectname, target) -> None:
        self.uuid = uuid
        self.priority = priority
        self.pos = pos
        self.objectname = objectname
        self.target = target


objectnames = [
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
]

targets = ["E0", "E1", "E2", "E3", "E4", "E5", "E6"]
