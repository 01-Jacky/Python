import requests
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html,'html.parser')
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'hklee310@gmail.com',
    'session_password':'Winter1!',
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)

html = client.get('https://www.linkedin.com/jobs/search/?keywords=software%20intern&location=United%20States&locationId=us%3A0').content
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())

with open('tmp_html','w') as f:
    f.write(str(soup.prettify(encoding='UTF-8')))

x = 1