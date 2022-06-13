from ImageSprite import MatricedImageSprite

# Note: same sized hp.png and hp_no.png is required.

class HPHeartFulfilled(MatricedImageSprite):
    def __init__(self, coordinate: tuple[int], margin: tuple[int]=(5, 2), base_offset: tuple[int]=(1, 10)):
        MatricedImageSprite.__init__(self, "hp.png", margin, base_offset)

class HPHeartLost(MatricedImageSprite):
    def __init__(self, coordinate: tuple[int], margin: tuple[int]=(5, 2), base_offset: tuple[int]=(1, 10)):
        MatricedImageSprite.__init__(self, "hp_no.png", margin, base_offset)