#!/usr/bin/env python3

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head, *body, tail = items

print(head, body, tail)
# 1 [2, 3, 4, 5, 6, 7, 8] 9

body[0]=99

print(body)
print(items)
