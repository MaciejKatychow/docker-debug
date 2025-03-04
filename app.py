# OPTION 1:
import debugpy
debugpy.listen(("0.0.0.0", 5678))  # This is needed for option 1

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello, World!")
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)