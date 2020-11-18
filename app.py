from flask import Flask
from flask_mail import Mail, Message
import smtplib
import os

# If error, page will display error details
DEBUG = True
# Server port
PORT = 8000
# Constructor - route() function - param for URL binding
app = Flask(__name__)

# ========== ROUTES ==========

# Index
@app.route('/')
def index():
  return 'Hello, Fauxxi Beauty API!'

@app.route('/contact', methods=['POST'])
def form():

    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] =  587
    # app.config['MAIL_TLS'] =  True
    # app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
    # app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')

    # mail = Mail(app)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.environ.get('EMAIL'), os.environ.get('PASSWORD'))
    server.sendmail('example@gmail.com', 'tmarcelojr@gmail.com', 'how are you')
    server.quit()
    # server.close()
    # print('Email sent!')
    # msg = "whaaattttt"
    # smtplib.SMTP().starttls()
    # mail = Mail(app)
    # message = Message('Whatever 1', sender='tmarcelojr@gmail.com', recipients=['tmarcelojr@gmail.com'])
    # message.body = msg
    # mail.send(message)
  
    return 'Message sent!'

# ========= Connection to server ==========
if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)