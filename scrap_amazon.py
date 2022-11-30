from bs4 import BeautifulSoup
import requests
import smtplib
import time

url = input('Enter URL: ')

rate = float(input('Enter Your Price: '))

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


def check_price():

    title = soup.find(id="productTitle").get_text()

    price = float(soup.find('span', {'class': 'a-price-whole'}).get_text().replace('.', '').replace(',', '').strip())

    if (price < rate):
        send_to_telegram(title + " is priced at " + str(price) + "\n Check this link: " + url)
            
    else:
        print(f"Given Price {price}")
        loop_func()
        



def send_to_telegram(message):

    apiToken = ''
    chatID = ''
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'


    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(Message Send)

    except Exception as e:
        print(e)


def loop_func():
    print(f"Price You Want : {rate}")
    time.sleep(300)
    check_price()
    

check_price()