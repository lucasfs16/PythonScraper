import  requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com.br/Echo-Show-Smart-Speaker-Alexa-Branco/dp/B07KD7TD31/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=alexa&qid=1571319396&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = (price[2:8])

    if(converted_price < 350):
        send_mail()


    print(converted_price)
    print(title.strip())
    if(converted_price < 350):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('lucasfs16051998@gmail.com', 'Touro98#19')

    subject = 'Price fell down'
    body = 'Check the amazon Link https://www.amazon.com.br/Echo-Show-Smart-Speaker-Alexa-Branco/dp/B07KD7TD31/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=alexa&qid=1571319396&sr=8-2'

    msg = "Subject: {}\n\n{}".format(subject, body)

    server.sendmail(
        'lucasfs16051998@gmail.com',
        'lucas_fs16@icloud.com',
        msg

    )

    print('Hey the email was sent!')

    server.quit()

while(True):

    check_price()
    time.sleep(3600)
