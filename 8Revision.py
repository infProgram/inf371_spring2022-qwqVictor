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
        self.maxhitpoints = self.hitpoints
        self.death        = False

    def show_stats(self):
        for stat in self.__stats__:
            print("%s: %s" % (stat, str(self.__getattribute__(stat))))

    def show_hitpoint(self):
        print("My hitpoint is %s!" % (str(self.hitpoints)))
    
    def attack(self):
        if not self.death:
            return random.randint(int(0.4 * self.strength), self.strength)
    
    def defense(self, attacked):
        if random.randint(1, 20) < self.dexterity:
            pass
        else:
            if self.hitpoints < attacked:
                self.hitpoints = 0
                self.death = True
            else:
                self.hitpoints -= attacked


    def heal(self, healed):
        if not self.death:
            self.hitpoints = min(self.maxhitpoints, self.hitpoints + healed)

if __name__ == "__main__":
    a = Character(strength=25, dexterity=10, constitution=12, intelligence=9, wisdom=18, charisma=11)
    b = Character(strength=30, dexterity=6, constitution=17, intelligence=8, wisdom=16, charisma=15)
    print("\nA: ")
    a.show_stats()
    a.show_hitpoint()
    print("\nB: ")
    b.show_stats()
    b.show_hitpoint()

    print("\nA attack B!")
    b.defense(a.attack())
    b.show_hitpoint()

    print("\nB healed itself 20 HP!")
    b.heal(20)
    b.show_hitpoint()