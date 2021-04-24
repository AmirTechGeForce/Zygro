from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Yo, I'm here! :D"

def launch():
  app.run(host = '0.0.0.0', port = 8080)

def revive_stamina():
  t = Thread(target = launch)
  t.start()
