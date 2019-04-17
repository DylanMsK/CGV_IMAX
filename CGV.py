import requests
from bs4 import BeautifulSoup
import random
import time
import smtplib
from email.mime.text import MIMEText

class Mail:
    def __init__(self, subject, content):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()      # say Hello
        smtp.starttls()  # TLS 사용시 필요

        email = ''
        password = ''
        smtp.login(email, password)

        to = ''
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['To'] = to
        smtp.sendmail(email, to, msg.as_string())
        smtp.quit()

url = 'http://www.cgv.co.kr/theaters/special/theater-line-up.aspx?regioncode=07'
headers = {
    'User-Agent': "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
cnt = 0
while 1:
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('div', class_='sect-lineup').find('sect-chart').find('ul')
    lis = ul.findAll('li')
    if len(lis) > 1 or '요로나' in ul.text or cnt == 3:
        Mail('ㄲㄲㄲㄲ', '?????')
        break
    if '요로나' in ul.text:
        print('요로나')
        break
    if cnt == 3:
        print('cnt')
        break
    cnt += 1
    time.sleep(3)