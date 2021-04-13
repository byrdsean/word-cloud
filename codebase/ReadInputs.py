import json
import os

from models.UserInput import UserInput

class ReadInputs:

    #Model to contain the input data
    _Inputs = None

    #Variables to contain the name of the source properties
    _source = 'source'
    _html = 'html'
    _css = 'css'
    _outputLocation = 'outputLocation'
    _stopwords = 'stopwords'
    _maxWordsInCloud = 'MaxWordsInCloud'
    _maxStopwordLen = 'MaxStopwordLen'

    def __init__(self):
        self._Inputs = UserInput()

    # Get source location from package.json
    def ReadInputs(self):
        with open('package.json') as f:
            ConfigData = json.load(f)

            if('assests' in ConfigData.keys()):
                AssestsDict = ConfigData["assests"]

                #Set the variables
                self._Inputs.SourceLocation = AssestsDict[self._source] if self._source in AssestsDict.keys() else None
                self._Inputs.HtmlTemplate = AssestsDict[self._html] if self._html in AssestsDict.keys() else None
                self._Inputs.CssLocation = AssestsDict[self._css] if self._css in AssestsDict.keys() else None
                self._Inputs.OutputLocation = AssestsDict[self._outputLocation] if self._outputLocation in AssestsDict.keys() else None
                self._Inputs.Stopwords = AssestsDict[self._stopwords] if self._stopwords in AssestsDict.keys() else None
                self._Inputs.MaxWordsInCloud = AssestsDict[self._maxWordsInCloud] if self._maxWordsInCloud in AssestsDict.keys() else None
                self._Inputs.MaxStopwordLength = AssestsDict[self._maxStopwordLen] if self._maxStopwordLen in AssestsDict.keys() else None

        return self._Inputs