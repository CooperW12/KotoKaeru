from databaseManager import verbDB


def negForm(verb, vType):

    if vType == 'る':
        negVerb = verb[:len(verb) - 1] + 'ない'

    elif vType == 'う':
        lastChar = verb[len(verb) - 1]
        if lastChar == 'う':
            negVerb = verb[:len(verb) - 1] + 'わない'
        elif lastChar == 'く':
            negVerb = verb[:len(verb) - 1] + 'かない'
        elif lastChar == 'ぐ':
            negVerb = verb[:len(verb) - 1] + 'がない'
        elif lastChar == 'す':
            negVerb = verb[:len(verb) - 1] + 'さない'
        elif lastChar == 'つ':
            negVerb = verb[:len(verb) - 1] + 'たない'
        elif lastChar == 'ぬ':
            negVerb = verb[:len(verb) - 1] + 'なない'
        elif lastChar == 'む':
            negVerb = verb[:len(verb) - 1] + 'まない'
        elif lastChar == 'る':
            negVerb = verb[:len(verb) - 1] + 'らない'
            
    elif vType == 'irr':
        if verb == 'いく':
            negVerb = 'いかない'
        elif verb == 'くる':
            negVerb = 'こない'
        elif verb == 'する':
            negVerb = 'しない'
        
    return negVerb   

verb = input('input verb in Japanese: ')
    

vType = verbDB.loc[verbDB['VERB'] == verb, ' TYPE']


if not vType.empty:
    vType = vType.iloc[0].strip()
    print(verb, '-->', negForm(verb, vType))
else:
    print(f"Verb '{verb}' not found in database")
    
