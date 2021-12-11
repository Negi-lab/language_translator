from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    #Suchit's code starts
    result = translator.english_french(textToTranslate)
    return result
    #Suchit's code ends

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    #Suchit's code starts
    result = translator.french_english(textToTranslate)
    return result

@app.route("/")
def renderIndexPage():
    #Suchit's code starts
    return render_template('index.html')
    #suchit's code ends

if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host="0.0.0.0", port=8080)

