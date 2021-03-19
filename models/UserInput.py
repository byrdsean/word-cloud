class UserInput:

    # Property - SourceLocation
    def set_SourceLocation(self, v):
        self._SourceLocation = v

    def get_SourceLocation(self):
        return self._SourceLocation

    SourceLocation = property(get_SourceLocation, set_SourceLocation)

    # Init method
    def __init__(self):
        self._SourceLocation = None