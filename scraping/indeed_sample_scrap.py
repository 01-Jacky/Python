import urllib.request
from bs4 import BeautifulSoup   # pip install beautifulsoup4

def get_html(url):
    """ Returns the html of url if status code 200, else None """
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Python Learning Program',    # Specify your own agent here
            'From': 'hklee310@gmail.com'
        }
    )
    resp = urllib.request.urlopen(req)  # Response object contains a lot of useful data not just html
    if resp.code == 200:
        return resp.read()              # returns the html document
    else:
        return None


# Get soup from HTML
if __name__ == '__main__':
    url = 'https://www.indeed.com/jobs?q=computer+science+intern&l=United+States&sort=date&start=0'

    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    # Pretty html
    pretty = soup.prettify()
    # print(pretty)

    # Find all the span tags with class company
    companies_span_tags = soup.find_all('span', {'class': 'company'})
    for company_span in companies_span_tags:
        print(company_span.text.strip())

