from verb import Verb
from databaseManager import verbDB

inVerb = input('input verb in Japanese: ')

kanji = verbDB.loc[verbDB['VERB'] == inVerb, ' KANJI']
vType = verbDB.loc[verbDB['VERB'] == inVerb, ' TYPE']
translation = verbDB.loc[verbDB['VERB'] == inVerb, ' TRANSLATION']

verb = Verb(inVerb, kanji, vType, translation)


if not vType.empty:
    kanji = kanji.iloc[0].strip()
    vType = vType.iloc[0].strip()
    translation = translation.iloc[0].strip()
    
    verb = Verb(inVerb, kanji, vType, translation)
    
    print(verb.hiragana, '-->', verb.negForm())
else:
    print(f"Verb '{inVerb}' not found in database")