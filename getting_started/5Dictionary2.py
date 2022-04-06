#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

import random

keys = ["dexterity", "constitution", "intelligence", "wisdom", "charisma"]

dictionary = {}

for key in keys:
    dictionary[key] = random.randint(1, 20)

for key in dictionary:
    print("%s: %s" % (key, str(dictionary[key])))