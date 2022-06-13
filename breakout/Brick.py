from ImageSprite import MatricedImageSprite

class Brick(MatricedImageSprite):
    def __init__(self, coordinate: tuple[int], margin: tuple[int]=(5, 2), base_offset: tuple[int]=(40, 50)):
        MatricedImageSprite.__init__(self, "brick.png", coordinate, margin, base_offset)
