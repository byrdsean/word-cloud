import json

class StopWords:

    # Variables
    _MaxStopwordLen = 3
    _StopWordList = set()
    _LimitOnLength = False

    def __init__(self, LimitOnLength):
        self._LimitOnLength = LimitOnLength

        # Load the stop words from package.json
        with open('package.json') as p:
            PackageDict = json.load(p)

            # Add the stopwords to the list
            for word in PackageDict["stopwords"]:
                word = word.strip()

                #Set variable to know if we should check the length of the work
                ValidLength = True
                if(self._LimitOnLength):
                    ValidLength = len(word) <= self._MaxStopwordLen

                # Insert the data if there is a valid length
                if(ValidLength):
                    self._StopWordList.add(word.lower())

    # Check if a word is a stopword
    def IsStopWord(self, value):
        CheckValue = value.lower()
        return True if CheckValue in self._StopWordList else False