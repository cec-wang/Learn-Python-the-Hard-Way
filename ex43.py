from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scenes
        current_scene.enter()

class Death(Scene):
    quips = ['You died.', 'You lost.','A puppy is better than this']
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)



class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""The Gothons have invaded your ship.
        Get neutron destruct bomb from the Weapons Armory,
        put it in the bridge,
        blow ship up and get into an escape pod.

        Now you have encountered a Gothons and he is ready to attack you.
        """))

        action = input("> ")

        if action == 'shoot!':
            print(dedent('''
            It does not work.
            '''))

            return 'death'
        elif action == 'dodge!':
            print(dedent('''
            Does not work!
            '''))
            return 'death'

        elif action == 'tell a joke':
            print(dedent('''
            It works!
            '''))
            return 'laser_weapon_armory'
        else:
            print("Does not read.")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent('''
        Use a 3 digit code to open the weapon box.
        You have 10 tries.
        '''))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses <10:
            print("BZZZZZED!")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            print(dedent('''
            You opened the box.
            You got the bomb and now you are running towards the bridge...
            '''))

            return 'the_bridge'

        else:
            print(dedent('''
            The mechanism is fused together and you no longer can get the bomb
            '''))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent('''
        More Gothons.
        What will you do?
        '''))

        action = input("> ")

        if action == 'throw the bomb':
            print(dedent('''
            You slipped.
            You hit your head and get caught.
            '''))

            return 'death'

        elif action =='slowly place the bomb':
            print(dedent('''
            You managed to do it successfully.
            Now you are heading towards the escape pod.
            '''))

            return 'escape_pod'
        else:
            print("Does not compute!")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent('''
        Only one escape pod is good.
        Pick one.
        '''))

        guess = input("[pod #]> ")
        good_pod = randint(1,5)

        if int(guess) != good_pod:
            print(dedent('''
            You jumped into pod {guess} and ejection failed.
            '''))

            return 'death'
        else:
            print(dedent('''
            Correct pod!
            You escaped the ship!
            '''))

            return ' finished'

class Finished(Scene):
    def enter(self):
        print('You won! Good job!')
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
