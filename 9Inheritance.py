#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

import random
# workaround for filename starts with number
Character = __import__("8Revision").Character

class MagicCharacter(Character):

    def __init__(self):
        super()
        self.mana = self.intelligence * 30 + 50

    def show_hitpoint_with_mana(self):
        self.show_hitpoint()
        print("My mana is %s!" % str(self.mana))
    
    def magic_missle(self):
        self.mana -= 5
        return random.randint(5, 10)
    
    def fireball(self):
        self.mana -= 10
        return random.randint(10, 20)
    
    def heal_mana(self, healed):
        self.mana += healed
