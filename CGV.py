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
user_agent = [
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:64.0) Gecko/20100101 Firefox/64.0",
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15",
        "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; rv:11.0) like Gecko",
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
    ]

cnt = 0
while 1:
    random_idx = random.choice(range(len(user_agent)))
    headers = {'User-Agent': user_agent[random_idx]}
    try:
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find('div', class_='sect-lineup').find('ul')
        lis = ul.findAll('li')
        if len(lis) > 1 or '엔드게임' in str(ul):
            Mail('예매!!!!!!!!!!!!', '')
            break
        if cnt == 3:
            print('cnt')
            break
    except:
        user_agent.pop(random_idx)
        if len(user_agent) == 0:
            break
    cnt += 1
    time.sleep(random.randint(5, 10))