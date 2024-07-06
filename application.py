from flask import Flask, request, render_template
from src.pipeline.prediction import PredictPipeline

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/translate",methods=['GET','POST'])
def translate():
    if request.method == 'GET':
        return render_template("translate.html")
    else:
        inputText=request.form.get('english-text')
        obj=PredictPipeline()
        translatedText=obj.predict(inputText)
        return render_template('translate.html',output=translatedText)
        
if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)