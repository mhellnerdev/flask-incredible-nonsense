from weakref import getweakrefcount
from flask import Flask
import get_word

app = Flask(__name__)

@app.route("/")
def index():
  return get_word.index_page()


@app.route("/json")
def about():
  return get_word.json_output()



if __name__ == '__main__':
  app.run()



