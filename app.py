from flask import Flask, request
from twilio.rest import Client


app = Flask(__name__)


@app.route('/sendwhatsappmsg', methods=['GET','POST'])
def sendwhatsappmsg():
    print(request.get_data())
    mobile=request.form['From'].split('+')[1]
    msg=request.form['Body']
    if msg:
        msg='Thank you for your message! A member of our team will be in touch with you soon.'
    print(msg)
    sid='AC3c568069b22bad55d2b3daee6750000c'  # Generated from the twilio new account setup
    authToken='251ce062c0dd25aafd6c9554a7a9c93a' # Generated from the twilio new account setup
    client=Client(sid,authToken)

    message = client.messages.create(from_='whatsapp:+14155238886',body=msg,to=f'whatsapp:+{mobile}')
    print(message.sid)

    return 'Success'


if __name__=='__main__':
    app.run()