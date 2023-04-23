from characters import Pig
from polygon import Polygon


class Level():
    def __init__(self, pigs, columns, beams, space):
        self.pigs = pigs
        self.columns = columns
        self.beams = beams
        self.space = space
        self.number = 0
        self.number_of_birds = 4
        # lower limit
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000
        self.bool_space = False

    def open_flat(self, x, y, n):
        """Create a open flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*100
            p = (x, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+50)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def closed_flat(self, x, y, n):
        """Create a closed flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*125
            p = (x+1, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+70)
            self.beams.append(Polygon(p, 85, 20, self.space))
            p = (x+30, y-30)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def horizontal_pile(self, x, y, n):
        """Create a horizontal pile"""
        y += 70
        for i in range(n):
            p = (x, y+i*20)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def vertical_pile(self, x, y, n):
        """Create a vertical pile"""
        y += 10
        for i in range(n):
            p = (x, y+85+i*85)
            self.columns.append(Polygon(p, 20, 85, self.space))

    def build_0(self):
        """level 0"""
        pig1 = Pig(980, 30, self.space)
        pig2 = Pig(985, -20, self.space)
        self.pigs.append(pig1)
        self.pigs.append(pig2)
        p = (980, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 60)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 60)
        self.columns.append(Polygon(p, 20, 85, self.space))

        p = (980, 20)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, -20)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, -20)
        self.columns.append(Polygon(p, 20, 85, self.space))

        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000

    def build_1(self):
        """level 1"""
        pig = Pig(1000, 100, self.space)
        self.pigs.append(pig)
        p = (900, 30)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850,30)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, -40)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1050, -40)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1105, -40)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_2(self):
        """level 2"""
        pig1 = Pig(880, 60, self.space)
        self.pigs.append(pig1)
        pig2 = Pig(1000, 150, self.space)
        self.pigs.append(pig2)
        p = (880, 10)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (880, -40)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1000, 90)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 0)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, -40)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_3(self):
        """level 4"""
        pig = Pig(900, 300, self.space)
        self.pigs.append(pig)
        pig = Pig(1000, 500, self.space)
        self.pigs.append(pig)
        pig = Pig(1100, 400, self.space)
        self.pigs.append(pig)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    

    def build_4(self):
        """level 7"""
        pig = Pig(978, 180, self.space)
        pig.life = 30
        self.pigs.append(pig)
        pig = Pig(978, 280, self.space)
        pig.life = 30
        self.pigs.append(pig)
        pig = Pig(978, 80, self.space)
        pig.life = 30
        self.pigs.append(pig)
        self.open_flat(950, 0, 3)
        self.vertical_pile(850, 0, 3)
        self.vertical_pile(830, 0, 3)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

  

    def load_level(self):
        try:
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
