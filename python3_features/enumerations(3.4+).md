# Enumerations - Python 3.4+

Instead of cluttering your code with constants, you can create an enumeration using the Enum class.  
An enumeration is a set of symbolic names bound to unique, constant values.

More information about enumerations:
 - https://docs.python.org/3.4/library/enum.html
 - https://pythonspot.com/python-enum/


```python
#!/usr/bin/env python3

from enum import Enum

class Color(Enum):
    Red = 1,
    Green = 2,
    Blue = 3

print(repr(Color.Red))
# <Color.Red: (1,)>

print(Color.Green)
# Color.Green

print(type(Color.Blue))
# <enum 'Color'>

```

