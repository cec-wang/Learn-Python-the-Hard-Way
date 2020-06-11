class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The Gothons of planet Percal #25 has invaded your ship and destroyed your entire crew.
You mission is to get the bomb from the Weapons Armory, put it in the bridge, and blow
the ship up after escaping into an escape pod.

You are running down the central corridor to the Weapons Armory when a Gothon jumps out.
He is about to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
You told the Gothon a joke. The Gothon laughed and can't move, so you shoot the
Gothon. You got into the Weapon Armory room.

You found the neuron bomb container. There is a 3 digit code needed for the box
and you've got 10 tries.
""")

the_bridge= Room("The Bridge",
"""
You got the bomb. You grabbed and head towards the bridge.

At the bridge, you met 5 gothons and they havem't pulled their weapons out yet.
""")

escape_pod = Room("Escape Pod",
"""
You left the bomb on the floor and slowly moved away. You locked the door behind
you and moves towards the escape pod.
""")

the_end_winner = Room("The End",
"""
You jumped into pod and hit the eject bottom. You escaped and you won!
""")

the_end_loser = Room("The End",
"""
You jumped into the pod and ejected. But the pod exploded half-way, killing you.
""")

escape_pod.add_paths({'2': the_end_winner,
                      '*': the_end_loser})

generic_death = Room("death", "you died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key
