from flask import Flask,request
import sys
import json


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World2!"


@app.route("/test", methods = ['POST'])
def test():
#    if request.method == 'POST':
#        json_data = json.loads(str(request.body, encoding='utf-8'))
#        print(json_data, file = sys.stderr)
    print(request.data, file=sys.stderr)
    #theJson = json.loads(request.data)
    #print("SESSION: " + theJson.session, file=sys.stderr)
        
    with open('test.json') as f:
        data = json.load(f)
    
    return json.dumps(data)
    
@app.route("/webSubmit", methods = ['POST'])
def submitWeb():
#    if request.method == 'POST':
#        json_data = json.loads(str(request.body, encoding='utf-8'))
#        print(json_data, file = sys.stderr)
    #print(request.data, file=sys.stderr)
    jsonStr = request.data.decode('utf-8')
    jsonObj = json.loads(jsonStr)
    print("=====RECEIVED SYMPTOMS=====", file=sys.stderr)
    for v in jsonObj:
        print(v, file=sys.stderr)
     #theJson = json.loads(request.data)
    #print("SESSION: " + theJson.session, file=sys.stderr)

    
    return "Hi james"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    print("test", file=sys.stderr)
