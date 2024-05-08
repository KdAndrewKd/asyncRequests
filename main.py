import asyncio
import aiohttp
from time import time
from bs4 import BeautifulSoup
from url import *


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def fetch_pages_parallel(links):
    
    async with aiohttp.ClientSession() as session:
        results = []

        for link in links:
            results.append(fetch(link, session))
        
        return await asyncio.gather(*results)

async def main(urls):

    


    t = time()
    result = await fetch_pages_parallel(urls)

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

        print(fullCaseNumber,date_receipts,category_parties,judge,date_solutions,solution,date_force)
        # print(linkCaseNumber)
    

    print("\nВремя выполнения:",time() - t)


asyncio.run(main(urls))