# Literal String Interpolation (f-strings) - Python 3.6+

Instead of having to use the `.format()` method to print your strings, you can use f-strings for a much more convenient way to replace values in your strings. 
f-strings are much more readable, concise, and easier to maintain.

More information about f-strings:
 - https://realpython.com/python-f-strings/
 - https://www.python.org/dev/peps/pep-0498/

```python
#!/usr/bin/env python3

x = 2
y = 3

# compare this statement:
print('x = {} and y = {}'.format(x, y))
# x = 2 and y = 3

# with this statement:
print(f'x = {x} and y = {y}')
# x = 2 and y = 3
```
