#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

characterA = {
    "strength": 8,
    "dexterity": 10,
    "constitution": 12,
    "intelligence": 9,
    "wisdom": 18,
    "charisma": 11
}

for key in characterA:
    print("'%s' => %s" % (key, str(characterA[key])))

if "strength" in characterA:
    print("Found %s with value %s" % ("strength", str(characterA["strength"])))
else:
    print("%s not found." % "strength")

if "speed" in characterA:
    print("Found %s with value %s" % ("speed", str(characterA["speed"])))
else:
    print("%s not found." % "speed")