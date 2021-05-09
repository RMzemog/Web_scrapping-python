import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/gp/product/B07H28QRKN/ref=crt_ewc_title_dp_1?ie=UTF8&psc=1&smid=A394M999VAE9NW'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price =float(price[2:7].replace(',', ''))
    print("cpnverted price = ", converted_price)
    print(title.strip())
    
    if (converted_price < 4000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('priyanshu9161@gmail.com', 'caictrylgiplaolb')

    subject = 'Check the link RMZ'
    body = '''The price is down Yeeeeeee!!!!!!!!!!!
    Grab The Offer Just For You .
    https://www.amazon.in/gp/product/B07H28QRKN/ref=crt_ewc_title_dp_1?ie=UTF8&psc=1&smid=A394M999VAE9NW'''


    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'priyanshu9161@gmail.com',
        'priyanshu94156@gmail.com',
        msg
    )
    print('Hey email has been sent successfully')

    server.quit()
while(True):
    check_price()
    time.sleep(60 * 60 * 24 * 7)