import asyncio
import aiohttp
import requests
from time import time
from bs4 import BeautifulSoup

from fun_randomHeaders import random_headers


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

async def main(urls):

    t = time()

    boolV1 = None
    boolV2 = None
    boolV3 = None

    # result = await fetch_pages_sync(urls)
    # boolV1 = True

    # result = await fetch_pages_parallel(urls)
    # boolV2 = True

    headers = random_headers()
    with requests.Session() as session:
        for url in urls:
            result = session.get(url).content.decode("utf-8")
    # boolV3 = True

    print(result)


    if boolV1 == True or boolV2 == True:

        soup = BeautifulSoup(str(result),'html.parser')
        result = soup.find(id='tablcont').find_all('tr')

        for row in result[1:(len(result))]:
        
            fullCaseNumber = str(row.find_all_next('td')[0].text.strip())

            date_receipts = str(row.find_all_next('td')[1].text.strip())
            date_receipts = date_receipts.split()
            date_receipts = str(date_receipts[1]).split("\\")
            date_receipts = date_receipts[0]
            category_parties = str(row.find_all_next('td')[2].text.strip()).split("\\t")
            category_parties = category_parties[5]
            judge = str(row.find_all_next('td')[3].text.strip()).split("\\t")
            judge = judge[5]
            date_solutions = str(row.find_all_next('td')[4].text.strip()).split("\\t")
            date_solutions = date_solutions[5]
            solution = str(row.find_all_next('td')[5]).split("\\t")
            solution = solution[5]
            date_force = str(row.find_all_next('td')[6].text.strip())
            linkCaseNumber = str(row.find_all_next('td')[0].find_all('a'))

            # print(fullCaseNumber,date_receipts,category_parties,judge,date_solutions,solution,date_force)
            print(fullCaseNumber)
            # print(linkCaseNumber)

    if boolV3 == True:

        soup = BeautifulSoup(str(result),'html.parser')
        result = soup.find(id='tablcont').find_all('tr')
        # print(result)

        for row in result[1:(len(result))]:
        
            fullCaseNumber = str(row.find_all_next('td')[0].text.strip())
            date_receipts = str(row.find_all_next('td')[1].text.strip())
            category_parties = str(row.find_all_next('td')[2].text.strip()).split("\\t")
            judge = str(row.find_all_next('td')[3].text.strip()).split("\\t")
            date_solutions = str(row.find_all_next('td')[4].text.strip()).split("\\t")
            solution = str(row.find_all_next('td')[5]).split("\\t")
            date_force = str(row.find_all_next('td')[6].text.strip())
            linkCaseNumber = str(row.find_all_next('td')[0].find_all('a'))

            # print(fullCaseNumber,date_receipts,category_parties,judge,date_solutions,solution,date_force)
            print(fullCaseNumber)

            print("-" * 150)

    print("\nВремя выполнения:",time() - t)




with open("testlistUrls_40.txt", "r", encoding="utf-8")as f_content:
    listUrls = f_content.readlines()
    urls = []
    for line in listUrls:
        line = line.replace(" \n" , "")
        urls.append(line)

asyncio.run(main(urls))




"""
344.55430364608765
28.46130633354187
115.43825316429138

406.4700462818146
28.962684392929077
126.32013320922852
"""