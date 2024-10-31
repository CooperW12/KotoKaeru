from flask import Flask, render_template, request, jsonify
from verbFunctions.verb import Verb
from verbFunctions.databaseManager import verbDB
from translation.romToHir import convRomToHir



app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('mainpage.html')

@app.route("/verbdatabase")
def verbdatabase():
    return render_template('verbdatabase.html')

@app.route("/playground", methods=['GET', 'POST'])
def playground():
    teVerb = 'NONE'
    pastVerb = 'NONE'
    negVerb = 'NONE'
    pastNegVerb = 'NONE'
    
    romToHir = 'NONE'

    if request.method == 'POST':
        formType = request.form.get('formType')
        
        try:
            
            if formType =='verbForm':
                inVerb = str(request.form['verb'])
                kanji = verbDB.loc[verbDB['VERB'] == inVerb, ' KANJI']
                vType = verbDB.loc[verbDB['VERB'] == inVerb, ' TYPE']
                translation = verbDB.loc[verbDB['VERB'] == inVerb, ' TRANSLATION']
                if not vType.empty:
                    kanji = kanji.iloc[0].strip()
                    vType = vType.iloc[0].strip()
                    translation = translation.iloc[0].strip()
                    
                    verb = Verb(inVerb, kanji, vType, translation)
                    teVerb = verb.teForm()
                    pastVerb = verb.pastForm()
                    negVerb = verb.negForm()
                    pastNegVerb = verb.pastNegForm()
                    
                else:
                    teVerb = 'Verb not found in database'
                    pastVerb = ''
                    negVerb = ''
                    pastNegVerb = ''
                    
            elif formType == 'romajiForm':
                romIn = str(request.form['romIn'])
                romToHir = convRomToHir(romIn)
        
            
        except:
            teVerb = '?'
            pastVerb = '?'
            negVerb = '?'
            pastNegVerb = '?'
            
            romToHir = '?'
            
    return render_template('playground.html', 
                           teVerb = teVerb, pastVerb = pastVerb, negVerb = negVerb, pastNegVerb = pastNegVerb,
                           romToHir = romToHir)
    
    
@app.route("/getInput", methods=['POST'])
def getInput():
    data = request.get_json() 
    currentText = data.get('currentText', '')
    
    
    filtered = verbDB[verbDB['VERB'].str.startswith(currentText)]
    if not filtered.empty:
        output = filtered.to_dict(orient="records")
        results = []
        results.append(output[0]['VERB'])
        results.append(output[0][' KANJI'].strip())
        results.append(output[0][' TYPE'].strip())
        results.append(output[0][' TRANSLATION'].strip())
        
        
    else:
        results = "No results found"
    
    return jsonify({"processedText": results})    



if __name__ == "__main__":
    app.run(debug=True)