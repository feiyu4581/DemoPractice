import asyncio
import datetime


async def slow():
    print ('[X] corotinue Started')
    await asyncio.sleep(1)
    print ('[X] corotinue Ended')


slow()
