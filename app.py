from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, D!'


if __name__ == "__main__":
  print('im side the iff now')
  app.run(host='0.0.0.0', port=8080, debug=True)
