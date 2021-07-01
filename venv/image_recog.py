from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from tags import get_relevant_tags

app = Flask(__name__)


@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    resp = MessagingResponse()

    if request.form['NumMedia'] != 0:

        image_url = request.form['MediaUrl0']
        relevant_tags = get_relevant_tags(image_url)

        resp.message('n'.join(relevant_tags))

    else:
        resp.message('Please send photo!')

    return str(resp)


if __name__ == "__main__":
    app.run()
