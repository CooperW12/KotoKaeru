from flask import Flask, render_template, request
from verbFunctions.verb import Verb
from verbFunctions.databaseManager import verbDB

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('mainpage.html')

@app.route("/playground", methods=['GET', 'POST'])
def playground():
    teVerb = 'NONE'
    if request.method == 'POST':
        try:
            
            inVerb = str(request.form['verb'])
            kanji = verbDB.loc[verbDB['VERB'] == inVerb, ' KANJI']
            vType = verbDB.loc[verbDB['VERB'] == inVerb, ' TYPE']
            translation = verbDB.loc[verbDB['VERB'] == inVerb, ' TRANSLATION']

            
            verb = Verb(inVerb, kanji, vType, translation)
            
            if not vType.empty:
                kanji = kanji.iloc[0].strip()
                vType = vType.iloc[0].strip()
                translation = translation.iloc[0].strip()
    
                verb = Verb(inVerb, kanji, vType, translation)
    
                teVerb = verb.teForm()
            else:
                teVerb = 'ERROR'
            
        except:
            teVerb = 'error'
            
    return render_template('playground.html', teVerb = teVerb)
    



if __name__ == "__main__":
    app.run(debug=True)