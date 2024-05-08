import asyncio
import aiohttp
import requests
from time import time


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def fetch_pages_parallel(links):
    async with aiohttp.ClientSession() as session:
        results = []

        for link in links:
            results.append(fetch(link, session))
        
        return await asyncio.gather(*results)


async def main():

    urls = []
    with open("testlistUrls_229.txt", "r", encoding="utf-8")as content:
        listUrls = content.readlines()
        for line in listUrls:
            resLine = line.replace("\n", "")
            urls.append(resLine)

    t = time()
    # print([text[:100] for text in await fetch_pages_parallel(urls)])
    result = await fetch_pages_parallel(urls)
    # print(result)
    print(time() - t)

    


asyncio.run(main())