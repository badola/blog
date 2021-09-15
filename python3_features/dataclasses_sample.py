#!/usr/bin/env python3
from dataclasses import dataclass

# Compare this class, using the conventional implementation

class Rectangle1:
    def __init__(self
                ,color: str
                ,width: float
                ,height: float) -> None:
        self.color = color
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

@dataclass
class Rectangle2:
    color: str
    width: float
    height: float
 
    def area(self) -> float:
        return self.width * self.height

rectangle1 = Rectangle1("Blue", 2, 3)
rectangle2 = Rectangle2("Blue", 2, 3)

print(rectangle1)
# <__main__.Rectangle1 object at 0x10f313510>

print(rectangle2)
# Rectangle2(color='Blue', width=2, height=3)

print(rectangle1.area())
# 6

print(rectangle2.area())
# 6

