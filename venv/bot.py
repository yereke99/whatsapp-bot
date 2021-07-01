from flask import Flask
import requests

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    msg = resp.message()

    responded = False

    if 'Hi' in incoming_msg:
        hi = "Hi I am WhatsApp chat-bot"
        msg.body(hi)
        responded = True

    if 'дробилка' in incoming_msg:
        drobilka = "Қандай дробилка керек!"
        msg.body(drobilka)

    if not responded:
        UnResp = "'Дробилка' деп жазыңыз!"
        msg.body()

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)