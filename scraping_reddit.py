from bs4 import BeautifulSoup as soup
from urllib import urlopen

URL_FRONTPAGE = 'https://www.reddit.com/.rss'
URL_SUB_NEWS = 'http://www.reddit.com/r/news/.rss'
URL_SUB_COMMENTS_MMA = 'https://www.reddit.com/r/mma/comments/' #All new comments in sub
URL_USER_ARNOLD = 'http://www.reddit.com/user/GovSchwarzenegger/.rss'
URL_MULTI_SPORTS = 'http://www.reddit.com/r/nba+nfl.rss'
URL_COMMENTS = 'https://www.reddit.com/r/instant_regret/comments/6v0f48/girl_drops_phone_from_car_driver_proceeds_to_run/.rss'


def print_scrape():
    client = urlopen(URL_SUB_NEWS)
    xml_page = client.read()
    client.close()

    soup_page = soup(xml_page, "xml")
    entry_list = soup_page.findAll("entry")

    for entry in entry_list:
        print(entry.title.text)
        print(entry.link.attrs['href'])
        # print(entry.updated.text)
        print("-" * 100)

print_scrape()
