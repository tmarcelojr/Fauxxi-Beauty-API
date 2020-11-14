from flask import Flask

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

# ========= Connection to server ==========
if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)