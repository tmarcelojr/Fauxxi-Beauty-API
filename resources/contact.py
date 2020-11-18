from flask import Flask, request
from flask_mail import Mail, Message
import os
import smtplib

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def form():
    print('we made it here')
    # app.config['MAIL-SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL-PORT'] =  587
    # app.config['MAIL-SSL'] =  True
    # app.config.from_pyfile('config.cfg')
    
    # mail = Mail(app)
    # msg = Message('Whatever 1', sender='tmarcelojr@gmail.com', recipients='tmarcelojr@gmail.com')
    # mail.send(msg)
    # return 'Message sent!'

    # payload = request.get_json()
    # payload['name'] = payload['name']
    # payload['email'] = payload['email']
    # payload['phone'] = payload['phone']
    # payload['subject'] = payload['subject']
    # payload['message'] = payload['message']

    # # message = "Hello testing this out"

    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))
    # server.sendmail('tmarcelojr@gmail.com', payload['email'], payload['message'])

if __name__ == '__main__':
    app.run(debug=True)


