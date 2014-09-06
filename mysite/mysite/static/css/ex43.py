from random import randrange


class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        print " the scene_map is",scene_map
        self.scene_map = scene_map
        pass

    def play(self):

        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        print" there is a gothon in this room. tell a joke"
        joke= raw_input(">")
        a=randrange(10)
        if a <5:
             " good joke. you can place the bomb"
        else:
            goto Death()



class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
