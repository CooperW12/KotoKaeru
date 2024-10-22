from databaseManager import verbDB

def teForm(verb, vType):
    
    if vType == 'る':
        teVerb = verb[:len(verb) - 1] + 'て'

    elif vType == 'う':
        lastChar = verb[len(verb) - 1]
        if lastChar in ['う', 'つ', 'る']:
            teVerb = verb[:len(verb) - 1] + 'って'
        elif lastChar in ['む', 'ぬ', 'ぶ']:
            teVerb = verb[:len(verb) - 1] + 'んで'
        elif lastChar == 'く':
            teVerb = verb[:len(verb) - 1] + 'いて'
        elif lastChar == 'ぐ':
            teVerb = verb[:len(verb) - 1] + 'いで'
        elif lastChar == 'す':
            teVerb = verb[:len(verb) - 1] + 'して'
            
    elif vType == 'irr':
        if verb == 'いく':
            teVerb = 'いって'
        elif verb == 'くる':
            teVerb = 'きて'
        elif verb == 'する':
            teVerb = 'して'
        
    return teVerb   

verb = input('input verb in Japanese: ')
    

vType = verbDB.loc[verbDB['VERB'] == verb, ' TYPE']


if not vType.empty:
    vType = vType.iloc[0].strip()
    print(verb, '-->', teForm(verb, vType))
else:
    print(f"Verb '{verb}' not found in database")
    
    