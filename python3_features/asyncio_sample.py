#!/usr/bin/env python3

import asyncio

async def say(sleep_time):
    await asyncio.sleep(sleep_time)
    print("When I say IT'S GOING, you say DOWN!!")
    await asyncio.sleep(sleep_time)
    print("IT'S GOING - DOWN!!")
    await asyncio.sleep(sleep_time)
    print("IT'S GOING - DOWN!!")

async def hello():
    await asyncio.gather(say(1), say(1))

asyncio.run(hello())

# When I say IT'S GOING, you say DOWN!!
# IT'S GOING - DOWN!!
# When I say IT'S GOING, you say DOWN!!
# IT'S GOING - DOWN!!
# IT'S GOING - DOWN!!
# IT'S GOING - DOWN!!
