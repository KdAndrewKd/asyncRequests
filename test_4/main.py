import asyncio
import aiohttp
import requests
from time import time

# Ссылки на статью
# https://ru.stackoverflow.com/questions/1491356/python-%D0%90%D1%81%D0%B8%D0%BD%D1%85%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5-http-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B-%D0%BD%D0%B0-n-urls
# https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html



async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def fetch_pages_sync(links):
    """
    Последовательное скачивание с каждой ссылки
    (дожидаемся скачивания по ссылке, потом переходим к следующей)
    """
    async with aiohttp.ClientSession() as session:
        results = []

        for link in links:
            results.append(await fetch(link, session))
        
        return results


async def fetch_pages_parallel(links):
    """
    Параллельное скачивание с каждой ссылки
    (собираем awitable запросы в список, потом параллельно собираем результат через asyncio.gather)
    """
    async with aiohttp.ClientSession() as session:
        results = []

        for link in links:
            results.append(fetch(link, session))
        
        return await asyncio.gather(*results)


async def main():
    urls = [
        'https://google.com',
    ] * 40


    t = time()
    # print([text[:100] for text in await fetch_pages_sync(urls)])
    result = await fetch_pages_sync(urls)
    print(time() - t)

    t = time()
    # print([text[:100] for text in await fetch_pages_parallel(urls)])
    result = await fetch_pages_parallel(urls)
    print(time() - t)

    t = time()
    with requests.Session() as session:
        for url in urls:
            result = session.get(url).text
    print(time() - t)


asyncio.run(main())