from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

async def get_pythonorg():
    r = await asession.get('https://python.org')
    print(r.html.find('title', first=True).text)
    print("")


async def get_google():
    r = await asession.get('https://google.com')
    print(r.html.find('title', first=True).text)
    print("")


async def get_reddit():
    r = await asession.get('https://reddit.com')
    print(r.html.find('title', first=True).text)
    print("")



asession.run(get_pythonorg, get_google, get_reddit)