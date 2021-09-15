# asyncio - Python 3.4+

The asyncio module is the new way to write concurrent code using the async and await syntax.  
This approach allows for much more readable code and abstracts away many of the complexity inherent with concurrent programming.

More information about the asyncio module:
  - https://docs.python.org/3/library/asyncio.html
  - https://realpython.com/async-io-python/

```python
!/usr/bin/env python3

import asyncio

async def say(sleep_time):
    await asyncio.sleep(sleep_time)
    print("When I say IT'S GOING, you say DOWN!!")
    await asyncio.sleep(sleep_time)
    print("IT'S GOING - DOWN!!")
    await asyncio.sleep(sleep_time)
    print("IT'S GOING - DOWN!!")

async def hello():
    await asyncio.gather(say(1), say(3))

asyncio.run(hello())

# When I say IT'S GOING, you say DOWN!!
# IT'S GOING - DOWN!!
# When I say IT'S GOING, you say DOWN!!
# IT'S GOING - DOWN!!
# IT'S GOING - DOWN!!
# IT'S GOING - DOWN!!
```
