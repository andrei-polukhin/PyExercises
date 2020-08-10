import asyncio
import aiohttp


async def fetch_page(session, url):
    async with session.get(url) as response:
        return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


if __name__ == '__main__':
    def main():
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'http://tecladocode.com/blog'
        ]
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        for page in pages:
            print(page)
        loop.close()
    print(main())
