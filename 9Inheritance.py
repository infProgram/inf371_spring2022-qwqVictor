#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

import random
# workaround for filename starts with number
Character = __import__("8Revision").Character

class MagicCharacter(Character):

    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.mana = intelligence * 30 + 50
        self.maxmana = self.mana

    def show_hitpoint_with_mana(self):
        self.show_hitpoint()
        print("My mana is %s!" % str(self.mana))
    
    def magic_missle(self):
        if self.mana >= 5:
            self.mana -= 5
            return random.randint(5, 10)
        else:
            return 0
    
    def fireball(self):
        if self.mana >= 10:
            self.mana -= 10
            return random.randint(10, 20)
        else:
            return 0
    
    def heal_mana(self, healed):
        self.mana = min(self.maxmana, self.mana + healed)

if __name__ == "__main__":
    a = MagicCharacter(strength=25, dexterity=10, constitution=12, intelligence=9, wisdom=18, charisma=11)
    b = MagicCharacter(strength=30, dexterity=6, constitution=17, intelligence=8, wisdom=16, charisma=15)
    print("\nA: ")
    a.show_stats()
    a.show_hitpoint_with_mana()
    print("\nB: ")
    b.show_stats()
    b.show_hitpoint_with_mana()

    print("\nA attack B with magic_missle!")
    b.defense(a.magic_missle())
    b.show_hitpoint_with_mana()

    print("\nB attack A with fireball!")
    a.defense(b.fireball())
    a.show_hitpoint_with_mana()

    print("\nB healed itself 4 mana!")
    b.heal_mana(4)
    b.show_hitpoint_with_mana()