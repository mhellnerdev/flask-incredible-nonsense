from weakref import getweakrefcount
from flask import Flask, render_template
import get_word

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("first_page.html")





@app.route("/json")
def json_words():
  return get_word.json_output()



if __name__ == '__main__':
  app.run()



