from direct.showbase.ShowBase import ShowBase
from mapmanagerii import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__()
        self.land = Mapmanager()
        base.camLens.setFor(90)

game = Game()
geme.run()