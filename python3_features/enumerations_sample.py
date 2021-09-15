#!/usr/bin/env python3

from enum import Enum

lt = [1, 2, 3]
class Color(Enum):
    Red = lt
    Green = 2,
    Blue = 3

print(repr(Color.Red))
print(dir(Color.Red.value))

Color.Red.value.append(9)
print(repr(Color.Red))
print(f'list => {lt}')

print(Color.Green)

print(type(Color.Blue))

print(str(Color.Red))

print(repr(Color.Blue))
