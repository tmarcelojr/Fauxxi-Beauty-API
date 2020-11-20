from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS
# from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os

# If error, page will display error details
DEBUG = True
# Server port
PORT = 8000
# Constructor - route() function - param for URL binding
app = Flask(__name__)
# CORS
CORS(app)

# ========== ROUTES ==========

# Index
@app.route('/')
def index():
  return 'Hello, Fauxxi Beauty API!'

# Contact form to send email to user
@app.route('/contact', methods=['POST'])
def form():
    print('did we get called')
    payload = request.get_json()
    print(payload)
    name = payload['name']
    email = payload['email']
    phone = payload['phone']
    subject = payload['subject']
    message = payload['message']

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = 'tmarcelojr@gmail.com'
    body = """\
    <html>
      <head></head>
      <body>
        <h4>From: """+str(email)+""" </h4>
        <h4>Name: """+str(name)+""" </h4>
        <h4>Phone: """+str(phone)+""" </h4>
        <h4>Message:</h4>
        <blockquote>"""+str(message)+"""</blockquote>
      </body>
    </html>
    """

    msg.attach(MIMEText(body, 'html'))
    text = msg.as_string()

    # Using TLS is not secure. Gmail account requires 2-step verification to be disabled
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Email and password saved in local environment
    server.login(os.environ.get('EMAIL'), os.environ.get('PASSWORD'))

    # Sendign email
    server.sendmail(email, 'fauxxilashes@gmail.com', text)
    server.quit()
    return 'Message sent!'

# ========= Connection to server ==========
if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)