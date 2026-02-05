import asyncio
import httpx
from time import time

start = time()
base_url = "https://pokeapi.co/api/v2/pokemon/"


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [client.get(base_url + str(i)) for i in range(20)]
        await asyncio.gather(*tasks)


asyncio.run(main())
print("Time to run:", round(time() - start, 2))
