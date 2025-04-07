import re, json

class FileProcessor:
    def __init__(self,file):
        self.file = file
        self.data = ""
        self.regexExpresion = r""
        self.resultFindAll = ""

    def openFilesAndGenerators(self):
        with open(self.file) as f:
            self.data = f.read()
    
    def regexExtractorDataFunction(self,regexExpresion=r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"):
        self.regexExpresion = regexExpresion
        self.resultFindAll=re.findall(self.regexExpresion,self.data)

    def printDataTest(self):
        print(json.dumps(self.resultFindAll,indent=4))

