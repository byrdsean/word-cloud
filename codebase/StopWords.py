import json

class StopWords:

    # Variables
    _StopWordList = set()
    _LimitOnLength = False
    _InputData = None

    def __init__(self, InputData, LimitOnLength):
        self._InputData = InputData
        self._LimitOnLength = LimitOnLength

        # Load the stop words from package.json
        with open(self._InputData.Stopwords) as f:
            eof = False
            while(eof == False):
                word = f.readline()
                if(word):
                    word = word.strip()

                    #Set variable to know if we should check the length of the work
                    ValidLength = True
                    if(self._LimitOnLength):
                        ValidLength = len(word) <= self._InputData.MaxStopwordLength

                    # Insert the data if there is a valid length
                    if(ValidLength):
                        self._StopWordList.add(word.lower())
                else:
                    eof = True

    # Check if a word is a stopword
    def IsStopWord(self, value):
        CheckValue = value.lower()
        return True if CheckValue in self._StopWordList else False