class Mapmanager():
    def __inti__(self):
        self.model = "block"
        self.texture = "block.png"
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (1, 1, 1, 1,),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0, 1),
        ]
        self.startNew()

    def starNew(self):
        self.land = render.attachNewNode("Land")

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors)-1]

    def addBlock(self, position):
        self.block = loader.loadModel(self, model)
        self.block.setTexture(loader.loadTexture(self, self.texture))
        self.block.setPos(position)
        self.color = self.get.Color(int(position[2]))
        self.block.detColor(self.color)
        self.block.reparentTo(self.land)


    def clear(self):
        self.land.removeNone()
        self.startNew()

    def loadLand(self, filename):
        self.clear()

        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split("")
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z))




















