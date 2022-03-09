#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

# workaround for filename starts with number
Character = __import__("8Revision").Character

class MagicCharacter(Character):

    def __init__(self):
        super()
        self.mana = self.intelligence * 30 + 50
    