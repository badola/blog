#!/usr/bin/env python3

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

r = Rectangle(1.5, 1.7)
print(r.area())
# 2.55

r = Rectangle("abcd", 3)
print(r.area())
