""" Opens top x links from reddit all as tabs in your browser """

from bs4 import BeautifulSoup as soup
import urllib.request
import webbrowser


URL_FRONTPAGE = 'https://www.reddit.com/r/all/.rss'
MAX_BROWSERS_TO_OPEN = 5


def main():
    with urllib.request.urlopen(URL_FRONTPAGE) as response:
        html = response.read()

    soup_page = soup(html, "xml")
    entry_list = soup_page.findAll("entry")

    if len(entry_list) > MAX_BROWSERS_TO_OPEN:
        entry_list = entry_list[:MAX_BROWSERS_TO_OPEN]

    for entry in entry_list:
        print(entry.title.text)
        print(entry.link.attrs['href'])
        # print(entry.updated.text)
        print("-" * 100)
        webbrowser.open(entry.link.attrs['href'])

if __name__ == '__main__':
    main()
