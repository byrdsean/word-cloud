import sys
import json

# Get source location from package.json
def GetSourceLocationFromConfig():
    Source = None
    with open('package.json') as f:
        ConfigData = json.load(f)
        if(ConfigData != None):
            Source = ConfigData["assests"]["Source"]
    return Source

# Get source location from argv
def GetSourceLocationFromArgv():
    return ''

# Read file data into string variable and return
def ReadFileFromSource(Source):
    FileData = None
    if(Source != None):
        with open(Source) as contents:
            FileData = contents.read()
    return FileData 

# Read the file data from the source
FileData = None
if(__name__ == '__main__'):
    Source = GetSourceLocationFromConfig()
    FileData = ReadFileFromSource(Source)
else:
    Source = GetSourceLocationFromArgv()
    FileData = ReadFileFromSource(Source)




print(FileData)