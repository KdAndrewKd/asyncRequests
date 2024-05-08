from requests_html import HTMLSession

session = HTMLSession()


r = session.get('https://www.iwannabechef.ru')
r.html.render()

titles = r.html.find('.post-title.entry-title')
  
for title in titles:
    print(title.text, ':', title.absolute_links.pop())
