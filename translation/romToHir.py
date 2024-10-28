

romajiIn = input('input romaji: ')

translations = {
'a' : 'あ', 'ka' : 'か', 'sa' : 'さ', 'ta' : 'た', 'na' : 'な', 'ha' : 'は', 'ma' : 'ま', 'ya' : 'や', 'ra' : 'ら', 'wa' : 'わ',
'i' : 'い', 'ki' : 'き', 'shi': 'し', 'chi': 'ち', 'ni' : 'に', 'fu' : 'ふ', 'mi' : 'み',              'ri' : 'り',
'u' : 'う', 'ku' : 'く', 'su' : 'す', 'tsu': 'つ', 'nu' : 'ぬ', 'hi' : 'ひ', 'mu' : 'む', 'yu' : 'ゆ', 'ru' : 'る', 'wo' : 'を',
'e' : 'え', 'ke' : 'け', 'se' : 'せ', 'te' : 'て', 'ne' : 'ね', 'he' : 'へ', 'me' : 'め',              're' : 'れ',
'o' : 'お', 'ko' : 'こ', 'so' : 'そ', 'to' : 'と', 'no' : 'の', 'ho' : 'ほ', 'mo' : 'も', 'yo' : 'よ', 'ro' : 'ろ', 'nn' : 'ん',

            'ga' : 'が', 'za' : 'ざ', 'da' : 'だ',       'ba' : 'ば', 'pa' : 'ぱ',
            'gi' : 'ぎ', 'ji' : 'じ', 'di' : 'ぢ',       'bi' : 'び', 'pi' : 'ぴ',
            'gu' : 'ぐ', 'zu' : 'ず', 'du' : 'づ',       'bu' : 'ぶ', 'pu' : 'ぷ',
            'ge' : 'げ', 'ze' : 'ぜ', 'de' : 'で',       'be' : 'べ', 'pe' : 'ぺ',
            'go' : 'ご', 'zo' : 'ぞ', 'do' : 'ど',       'bo' : 'ぼ', 'po' : 'ぽ',
            
'kya' : 'きゃ', 'sha' : 'しゃ', 'cha' : 'ちゃ', 'nya' : 'にゃ', 'hya' : 'ひゃ', 'mya' : 'みゃ', 'rya' : 'りゃ',
'kyu' : 'きゅ', 'shu' : 'しゅ', 'chu' : 'ちゅ', 'nyu' : 'にゅ', 'hyu' : 'ひゅ', 'myu' : 'みゅ', 'ryu' : 'りゅ',
'kyo' : 'きょ', 'sho' : 'しょ', 'cho' : 'ちょ', 'nyo' : 'にょ', 'hyo' : 'ひょ', 'myo' : 'みょ', 'ryo' : 'りょ',
'gya' : 'ぎゃ', 'jya' : 'じゃ', 'dya' : 'ぢゃ',         'bya' : 'びゃ', 'pya' : 'ぴゃ',
'gyu' : 'ぎゅ', 'jyu' : 'じゅ', 'dyu' : 'ぢゅ',         'byu' : 'びゅ', 'pyu' : 'ぴゅ',
'gyo' : 'ぎょ', 'jyo' : 'じょ', 'dyo' : 'ぢょ',         'byo' : 'びょ', 'pyo' : 'ぴょ'
}

oneCharTranslations = {'a' : 'あ', 'i' : 'い', 'u' : 'う', 'e' : 'え', 'o' : 'お'}

twoCharTranslations = {
'ka' : 'か', 'sa' : 'さ', 'ta' : 'た', 'na' : 'な', 'ha' : 'は', 'ma' : 'ま', 'ya' : 'や', 'ra' : 'ら', 'wa' : 'わ',
'ki' : 'き', 'shi': 'し', 'chi': 'ち', 'ni' : 'に', 'fu' : 'ふ', 'mi' : 'み',              'ri' : 'り',
'ku' : 'く', 'su' : 'す', 'tsu': 'つ', 'nu' : 'ぬ', 'hi' : 'ひ', 'mu' : 'む', 'yu' : 'ゆ', 'ru' : 'る', 'wo' : 'を',
'ke' : 'け', 'se' : 'せ', 'te' : 'て', 'ne' : 'ね', 'he' : 'へ', 'me' : 'め',              're' : 'れ',
'ko' : 'こ', 'so' : 'そ', 'to' : 'と', 'no' : 'の', 'ho' : 'ほ', 'mo' : 'も', 'yo' : 'よ', 'ro' : 'ろ', 'nn' : 'ん',

            'ga' : 'が', 'za' : 'ざ', 'da' : 'だ',       'ba' : 'ば', 'pa' : 'ぱ',
            'gi' : 'ぎ', 'ji' : 'じ', 'di' : 'ぢ',       'bi' : 'び', 'pi' : 'ぴ',
            'gu' : 'ぐ', 'zu' : 'ず', 'du' : 'づ',       'bu' : 'ぶ', 'pu' : 'ぷ',
            'ge' : 'げ', 'ze' : 'ぜ', 'de' : 'で',       'be' : 'べ', 'pe' : 'ぺ',
            'go' : 'ご', 'zo' : 'ぞ', 'do' : 'ど',       'bo' : 'ぼ', 'po' : 'ぽ'}

threeCharTranslations = {
'kya' : 'きゃ', 'sha' : 'しゃ', 'cha' : 'ちゃ', 'nya' : 'にゃ', 'hya' : 'ひゃ', 'mya' : 'みゃ', 'rya' : 'りゃ',
'kyu' : 'きゅ', 'shu' : 'しゅ', 'chu' : 'ちゅ', 'nyu' : 'にゅ', 'hyu' : 'ひゅ', 'myu' : 'みゅ', 'ryu' : 'りゅ',
'kyo' : 'きょ', 'sho' : 'しょ', 'cho' : 'ちょ', 'nyo' : 'にょ', 'hyo' : 'ひょ', 'myo' : 'みょ', 'ryo' : 'りょ',
'gya' : 'ぎゃ', 'jya' : 'じゃ', 'dya' : 'ぢゃ',         'bya' : 'びゃ', 'pya' : 'ぴゃ',
'gyu' : 'ぎゅ', 'jyu' : 'じゅ', 'dyu' : 'ぢゅ',         'byu' : 'びゅ', 'pyu' : 'ぴゅ',
'gyo' : 'ぎょ', 'jyo' : 'じょ', 'dyo' : 'ぢょ',         'byo' : 'びょ', 'pyo' : 'ぴょ'
}

done = False
lookingAtIndex = 0
currentTrans = []
lookingAt = ''
for i in range(len(romajiIn)):
    lookingAt = lookingAt + romajiIn[i]
    if lookingAt in oneCharTranslations.keys():
        currentTrans.append(translations[lookingAt])
        lookingAt = ''
    elif lookingAt in twoCharTranslations.keys():
        currentTrans.append(translations[lookingAt])
        lookingAt = ''
    elif lookingAt in threeCharTranslations.keys():
        currentTrans.append(translations[lookingAt])
        lookingAt = ''
    else:
        pass
        
    done = True
      
finalTrans = ''
for hira in currentTrans:
    finalTrans = finalTrans + hira
    
print(finalTrans)  