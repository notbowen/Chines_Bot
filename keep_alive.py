# keep_alive.py
# To host the bot

from flask import Flask
from threading import Thread

import logging

app = Flask('')

# Disable some flask logging
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/')
def home():
    return 'Alive'

def run():
  app.run(host='0.0.0.0',port=6969)

def keep_alive():  
    t = Thread(target=run)
    t.daemon = True
    t.start()