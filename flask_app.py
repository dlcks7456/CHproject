from flask import Flask, request, make_response



app = Flask(__name__)



@app.route('/')

def home():

    return 'Hello, World! Hi, Git !'



if __name__ == '__main__':

    app.run()