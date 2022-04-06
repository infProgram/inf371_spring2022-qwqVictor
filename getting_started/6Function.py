#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Victor Huang <2020215138@stu.cqupt.edu.cn>

def celcius2fahrenheit(celcius):
    return 1.8 * celcius + 32.0

if __name__ == "__main__":
    user_input = ""
    while user_input.lower() != "quit":
        user_input = input("Celcius? (or quit) ")
        celcius = float(user_input)
        print("Fahrenheit: %.2f" % (celcius2fahrenheit(celcius)))