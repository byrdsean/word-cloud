class UserInput:

    #Html Template
    def set_HtmlTemplate(self, v):
        self._HtmlTemplate = v

    def get_HtmlTemplate(self):
        return self._HtmlTemplate

    #CSS Location
    def set_CssLocation(self, v):
        self._CssLocation = v

    def get_CssLocation(self):
        return self._CssLocation

    #SourceLocation
    def set_SourceLocation(self, v):
        self._SourceLocation = v

    def get_SourceLocation(self):
        return self._SourceLocation

    #OutputLocation
    def set_OutputLocation(self, v):
        self._OutputLocation = v

    def get_OutputLocation(self):
        return self._OutputLocation

    #Stopwords
    def set_Stopwords(self, v):
        self._Stopwords = v

    def get_Stopwords(self):
        return self._Stopwords

    #MaxWordsInCloud
    def set_MaxWordsInCloud(self, v):
        self._MaxWordsInCloud = v

    def get_MaxWordsInCloud(self):
        return self._MaxWordsInCloud

    #MaxStopwordLength
    def set_MaxStopwordLength(self, v):
        self._MaxStopwordLength = v

    def get_MaxStopwordLength(self):
        return self._MaxStopwordLength

    # Properties
    HtmlTemplate = property(get_HtmlTemplate, set_HtmlTemplate)
    SourceLocation = property(get_SourceLocation, set_SourceLocation)
    CssLocation = property(get_CssLocation, set_CssLocation)
    OutputLocation = property(get_OutputLocation, set_OutputLocation)
    Stopwords = property(get_Stopwords, set_Stopwords)
    MaxWordsInCloud = property(get_MaxWordsInCloud, set_MaxWordsInCloud)
    MaxStopwordLength = property(get_MaxStopwordLength, set_MaxStopwordLength)

    # Init method
    def __init__(self):
        self._SourceLocation = None