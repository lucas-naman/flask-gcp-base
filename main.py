from flask import Flask, Blueprint, request

# init app
app = Flask(__name__)

@app.route('/')
def root():
    return "Rest Api with google app engine, Google Firebase and Flask use this url and /scrap/canada to store the 10 first images of canada on wikipedia"

# Run server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080,debug=True)
