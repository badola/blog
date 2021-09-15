# Extended Iterable Unpacking - Python 3.0+

Using this trick, while unpacking an iterable, you can specify a "catch-all" variable that will be assigned a list of the items not assigned to a regular variable.  
Simple, but very convenient to keep the code concise.

More information about Extended Iterable Unpacking:
 - https://www.python.org/dev/peps/pep-3132/
 - https://www.rfk.id.au/blog/entry/extended-iterable-unpacking/

```python
#!/usr/bin/env python3

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head, *body, tail = items

print(head, body, tail)
# 1 [2, 3, 4, 5, 6, 7, 8] 9

body[0]=99

print(body)
print(items)
```
