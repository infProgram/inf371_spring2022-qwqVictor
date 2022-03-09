#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

import random

class Character:
    __stats__  = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength     = strength
        self.dexterity    = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom       = wisdom
        self.charisma     = charisma
        self.hitpoints    = constitution * 30 + 50

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