import requests
from bs4 import BeautifulSoup
import smtplib
import time

print("Your MSG")
print('')

# for example the url can be https://wwww.amazon.com

URL = 'URL that you will use'

# This is my user agent but you can also use yours!!

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    # this code is written for Indian Websites but will change according to your country!!
    converted_price = price[2:7]
    final_converted_price = ''  
    for i in converted_price:
        if(i == ','):
            continue
        else:
            final_converted_price = final_converted_price + i

    if float(final_converted_price) < 'price you want to check': # the price will be an int
        send_mail()

def send_mail():
    # For this to work please go to your gmail settings and allow access to low secured apps
    email = 'Your Email'
    password = 'Email password'
    receiver = 'Receiver email'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)

    subject = 'price fell down'
    body = 'check the amazon link, (pls remove this paranthesis and paste your link) '
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(email,receiver,msg)
    print('Hey EMAIL HAS BEEN SENT!')
    server.quit()

while(True):
    check_price()
    time_check = 60*60 #this code will run after a particular interval of time!!
    time.sleep(time_check)
