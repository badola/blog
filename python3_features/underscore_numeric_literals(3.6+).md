# Underscores in Numeric Literals - Python 3.6+

This one is a small, nice addition: you can use underscores in numeric literals for improved readability.  
This will shave off a few seconds every time you had to count how many digits a number had.

More information about underscores in numeric literals:
 - https://www.python.org/dev/peps/pep-0515/

```python
#!/usr/bin/env python3

x = 1_000_000
y = 1000000

print(x, y, x == y)
# 1000000 1000000 True
```

```python
# grouping decimal numbers by thousands
amount = 10_000_000.0

# grouping hexadecimal addresses by words
addr = 0xCAFE_F00D

# grouping bits into nibbles in a binary literal
flags = 0b_0011_1111_0100_1110

# same, for string conversions
flags = int('0b_1111_0000', 2)
```
