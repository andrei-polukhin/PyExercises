import aiohttp
import asyncio


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status


loop = asyncio.get_event_loop()
tasks = [fetch_page("https://google.com") for i in range(1000)]
print(loop.run_until_complete(asyncio.gather(*tasks)))
