from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/translate",methods=['GET','POST'])
def translate():
    if request.method == 'GET':
        return render_template("translate.html")
    else:
        print(request.form.get('english-text')) #user_input
        return render_template("translate.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)