# Type hints - Python 3.5+

You can use type hints to indicate the type of a value in your code. For example, you can use it to annotate the arguments of a function and its return type.
These hints make your code more readable, and help tools understand it better.

More information about type hints:
 - https://veekaybee.github.io/2019/07/08/python-type-hints/
 - https://docs.python.org/3/library/typing.html

```python
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
```
