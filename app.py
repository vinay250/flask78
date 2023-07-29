# save this as app.py
from flask import Flask

obj = Flask(__name__)

@obj.route("/")
def welcome():
    return "welcome to Flask"

print(__name__)

if __name__ == '__main__':
obj.run()