from flask import Flask
import get_word

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello Flask"

@app.route("/about")
def about():
  return "About You"

if __name__ == '__main__':
  app.run()



