#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

import random

l = []

for i in range(0, 9+1):
    l.append(random.randint(0, 2**31-1))

print(l)