class Verb:
    
    def __init__(self, hiragana, kanji, vType, translation):
        self.hiragana = str(hiragana)
        self.kanji = str(kanji)
        self.vType = str(vType)
        self.translation = str(translation)
        
    def teForm(self):

        if self.vType == 'る':
            teVerb = self.hiragana[:len(self.hiragana) - 1] + 'て'

        elif self.vType == 'う':
            lastChar = self.hiragana[len(self.hiragana) - 1]
            if lastChar in ['う', 'つ', 'る']:
                teVerb = self.hiragana[:len(self.hiragana) - 1] + 'って'
            elif lastChar in ['む', 'ぬ', 'ぶ']:
                teVerb = self.hiragana[:len(self.hiragana) - 1] + 'んで'
            elif lastChar == 'く':
                teVerb = self.hiragana[:len(self.hiragana) - 1] + 'いて'
            elif lastChar == 'ぐ':
                teVerb = self.hiragana[:len(self.hiragana) - 1] + 'いで'
            elif lastChar == 'す':
                teVerb = self.hiragana[:len(self.hiragana) - 1] + 'して'
                
        elif self.vType == 'irr':
            if self.hiragana == 'いく':
                teVerb = 'いって'
            elif self.hiragana == 'くる':
                teVerb = 'きて'
            elif self.hiragana == 'する':
                teVerb = 'して'
            
        return teVerb   
    
    def negForm(self):
        if self.vType == 'る':
            negVerb = self.hiragana[:len(self.hiragana) - 1] + 'ない'

        elif self.vType == 'う':
            lastChar = self.hiragana[len(self.hiragana) - 1]
            if lastChar == 'う':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'わない'
            elif lastChar == 'く':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'かない'
            elif lastChar == 'ぐ':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'がない'
            elif lastChar == 'す':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'さない'
            elif lastChar == 'つ':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'たない'
            elif lastChar == 'ぬ':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'なない'
            elif lastChar == 'ぶ':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'ばない'
            elif lastChar == 'む':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'まない'
            elif lastChar == 'る':
                negVerb = self.hiragana[:len(self.hiragana) - 1] + 'らない'
            
        elif self.vType == 'irr':
            if self.hiragana == 'いく':
                negVerb = 'いかない'
            elif self.hiragana == 'くる':
                negVerb = 'こない'
            elif self.hiragana == 'する':
                negVerb = 'しない'
        
        return negVerb 
        
    
    
    