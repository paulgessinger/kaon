from flask import Flask

from .types import VR

app = Flask(__name__)


@app.route("/")
def hello_world() -> VR:
    return "Hello Worldw!"


# if __name__ == '__main__':
#     app.run()
