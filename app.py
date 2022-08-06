from re import A
from weakref import getweakrefcount
from flask import Flask, render_template
import get_word

app = Flask(__name__)

@app.route("/")
def index():
  return render_template(
    "jinja.html",
    name = "Mark Hellner",
    template_name = __name__ + ".py"
  )

@app.route("/expressions/")
def hello_expressions():

  # variables for expressions.html
  color = "green"
  animal_one = "marmalade meatball"
  animal_two = "bridgeton baffoon"
  orange_amount = 40
  apple_amount = 30
  donate_amount = 25
  first_name = "Mark"
  last_name = "Hellner"


  # dict stores variables above into key word arguments
  kwargs = {
    "color": color,
    "animal_one": animal_one,
    "animal_two": animal_two,
    "orange_amount": orange_amount,
    "apple_amount": apple_amount,
    "donate_amount": donate_amount,
    "first_name": first_name,
    "last_name": last_name,
  }

  # return html file and dict keys to pass into jinja templates {{ var }}
  return render_template(
    "expressions.html", **kwargs,
    # # below can map keyword args to jinja templates, otherwise use all keywords in dict with **kwargs argument above.
    # color=color, 
    # animal_one=animal_one, 
    # animal_two=animal_two, 
    # orange_amount=orange_amount,
    # apple_amount=apple_amount,
    # donate_amount=donate_amount,
    # first_name=first_name,
    # last_name=last_name,
    
    )
  

@app.route("/json/words")
def json_words():
  return



if __name__ == '__main__':
  app.run()



