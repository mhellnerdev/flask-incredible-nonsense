from re import A
from weakref import getweakrefcount
from flask import Flask, render_template
import get_word

app = Flask(__name__)

@app.route("/")
def index():
  incredible_nonsense = get_word.format_sentence()  
  return render_template(
    "html/index.html",
    incredible_nonsense=incredible_nonsense
  )


@app.route("/randomsentence/")
def random_sentence():
  incredible_nonsense = get_word.format_sentence()
  return render_template(
    "html/index.html",
    incredible_nonsense=incredible_nonsense
  )


@app.route("/json/words/")
def json_words():
  return



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)