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
