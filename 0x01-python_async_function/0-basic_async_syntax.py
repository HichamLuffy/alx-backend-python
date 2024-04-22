#!/usr/bin/python3


import asyncio

async def task(id):
    print(f'Task {id} started')
    await asyncio.sleep(1)  # Non-blocking sleep
    print(f'Task {id} finished')

async def main():
    await asyncio.gather(task(1), task(2), task(3))

# This is how you run the asyncio event loop
asyncio.run(main())
