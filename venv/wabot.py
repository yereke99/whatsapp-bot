from flask  import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import urllib.request
from image_recognation import download
from pdf_2_image_ocr import pdf_2_image
from time import sleep
from SQLite import conn, cursor
from image_recognation import download
import datetime

bot = Flask(__name__)

@bot.route('/sms', methods=['GET', 'POST'])
def wabot():
    msg = MessagingResponse()
    num = request.form.get('From').replace("whatsapp:", "")
    msg_text = request.form.get('Body')
    file_count = int(request.form.get('NumMedia'))

    if file_count > 0:

        url = request.form.get('MediaUrl0')

        print(url)
        # cursor.execute("INSERT INTO Link (link, client_number) VALUES(%s, %s)", (url, num, ) )
        d_t = datetime.datetime.today()
        da_t = str(d_t)
        number = ''.join(num)
        ldt = (url, da_t, number)

        cursor.execute("""
                           INSERT INTO links (link, date_and_time, tele_number) VALUES(?, ?, ?)
            """, ldt)

        conn.commit()
        download(url, num)
        msg_text = msg.message(
            f"Сіздің сұранымыңыз сәтті қабылданды😉!\nМал дәрігері алдағы 30 минутта хабарласады👌\nСіздің whatsapp номеріңіз :{num}")

    else:
        msg_text = msg.message(f"Каспий банктің түбіртегін ғана жіберіңіз!\nСіздің whatsapp номеріңіз :{num}")

    return str(msg)


if __name__ == "__main__":
    bot.run(port=5000)