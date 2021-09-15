# Walrus operator - Python 3.8+

Using assignment expressions (through the walrus operator :=) you can assign and return a value in the same expression.  
This operator makes certain constructs more convenient and helps communicate the intent of your code more clearly.

More information about the Walrus operator:
 - https://deepsource.io/blog/python-walrus-operator/
 - https://www.python.org/dev/peps/pep-0572/

```python
#!/usr/bin/env python3

# This is a regular while loop. Notice how we need to ask for a value twice.
value = input('Enter a value: ')
while value != '0':
    print(f'1st Loop : Value [{value}]')
    value = input('Enter a value: ')

# This is the same while loop, but now we are using the walrus operator
# to avoid having to ask for the value twice.
while (value := input('Enter a value: ')) != '0':
    print(f'2nd Loop : Value [{value}]')
```
