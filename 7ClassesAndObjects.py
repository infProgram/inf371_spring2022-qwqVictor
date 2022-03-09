#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

import random

class Character:
    __stats__  = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    strength     = 8
    dexterity    = 10
    constitution = 12
    intelligence = 9
    wisdom       = 18
    charisma     = 11

    hitpoints = constitution * 30 + 50

    def __init__(self):
        pass

    def show_stats(self):
        for stat in self.__stats__:
            print("%s: %s" % (stat, str(self.__getattribute__(stat))))

    def show_hitpoint(self):
        print("My hitpoint is %s!" % (str(self.hitpoints)))
    
    def attack(self):
        return random.randint(1, self.strength)
    
    def defense(self, attacked):
        if random.randint(1, 20) < self.dexterity:
            pass
        else:
            self.hitpoints -= attacked

    def heal(self, healed):
        self.hitpoints += healed