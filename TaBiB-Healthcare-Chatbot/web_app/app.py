from distutils.log import debug
from flask import Flask,render_template,request
import requests

app=Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    msg = request.args.get('msg')
    r=requests.post('http://localhost:5002/webhooks/rest/webhook',json={"message":msg})
    print('Bot says, ',end=' ')
    response=''
    for i in r.json():
        response+=i['text']
    return response

if __name__ == '__main__':
    app.run(debug=True)